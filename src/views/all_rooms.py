import flet as ft
from src.components.navigation_bar import NavigationBar
from src.Backend.RoomsManagement import TakeAllRooms, FilterRooms, TakeRoomImage
from src.Backend.BookingManagement import GetAvailableRooms
from random import sample
import datetime 
from datetime import date

def CreateRoomCard(page, room_data):
    room_id = room_data.get("id", room_data.get("_id"))
    room_type = room_data.get("category") 
    price = room_data.get("price")
    description = room_data.get("description")
    img_src = room_data.get("main_image")

    # this variable manages the active filters
    

    

    return ft.Container(
        width=300,
        height=320,
        padding=5,
        margin=15,
        bgcolor="white",
        border_radius=15,
        shadow=ft.BoxShadow(blur_radius=5, color=ft.Colors.BLACK),
        ink=True,
        on_click= lambda e: (
                setattr(page, "selected_room_data", {"data": room_data, "type": room_type, "foto_portada": img_src}),
                page.go("/singleRoom") if hasattr(page, "go") else page.session.set("route", "/singleRoom")
        ), 
        content=ft.Column(
            controls=[
                ft.Image(
                    src=img_src,
                    width=float("inf"),
                    height=180,
                    border_radius=5,
                    fit="COVER",
                    gapless_playback=True, 
                    cache_width=600,
                ),
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text(value=room_type, color="black", size=18, weight="bold"),
                            ft.Text(value=description, color="black", size=12, max_lines=2, overflow=ft.TextOverflow.ELLIPSIS, text_align=ft.TextAlign.JUSTIFY),
                            ft.Text(value=f"Desde {price}€/noche", color="black", weight="bold")
                        ]
                    )
                )
            ]
        )
    )

def allRooms(page: ft.Page):
    if page.username:
         print(f"Usuario detectado: {page.session}") 
         menu = NavigationBar(page, state="logged_in")
    else:
         menu = NavigationBar(page)
    
    active_filters = [] 
    entry_date_inputs = []
    exit_date_inputs = []

    state = {
        "pool_rooms": TakeAllRooms(), 
        "active_filters": [],               # checkbox filters
        "guest_number": 0,                   
        "Start_date": None,
        "End_date": None
    }

    grid_rooms = ft.GridView(
        expand=True,
        runs_count=5,
        child_aspect_ratio=1, 
        spacing=20,
        run_spacing=20,
        controls=[] 
    )

    def LoadCards(rooms_data, should_update=False):
        cards = []
        for room in rooms_data:
            cards.append(CreateRoomCard(page, room))

        if cards:
            grid_rooms.controls = sample(cards, len(cards))
        else:
            grid_rooms.controls = []
        
        if should_update:
            grid_rooms.update()

    def AplyFilter():
        '''Utiliza la variable de state para aplicar los filtros a las habitaciones'''
        
        result = []

        for room in state["pool_rooms"]:
            match = True # if a room doesn't match the filters it turns to false

            guests = room.get("guests") #gets the number of guests on the current room on the loop
            if state["guest_number"] > 0 and int(guests) < state["guest_number"]:
                match = False
            
            if match and state["active_filters"]:
                room_services = room.get("content")
                room_beds = room.get("bed")
                room_category = room.get("category")
                precio_room = float(room.get("price"))

                for filter in state["active_filters"]:

                    #if it has an euro, we use price logic
                    if "€" in filter:
                        match_precio = False
                        if filter == "0€ - 50€" and (0 <= precio_room <= 50): match_precio = True
                        elif filter == "50€ - 100€" and (50 < precio_room <= 100): match_precio = True
                        elif filter == "100€ - 150€" and (100 < precio_room <= 150): match_precio = True
                        elif filter == "150€ - 200€" and (150 < precio_room <= 200): match_precio = True
                        elif filter == "+200€" and (precio_room > 200): match_precio = True
                        
                        if not match_precio:
                            match = False
                    
                    # from now on we just go through a list of elifs and if the filter doesn't match any we use an else at the end to take the room out
                    elif room_category in state["active_filters"]:
                        pass

                    # since we're goin' through all filters, if any of 'em is not in the rooms services the room is already out
                    elif filter in room_services:
                        pass

                    elif filter in room_beds:
                        pass

                    else:
                        match = False
            
            # if all filters match with a room and the match variable isn't changed we append it to the result list
            if match:
                result.append(room)
        
        LoadCards(result)

    def FilterChange(e):
        '''Now this just changes the state filters and calls aply filter'''
        label = e.control.label.value 
        is_checked = e.control.value
        
        if is_checked:
            if label not in state["active_filters"]: 
                state["active_filters"].append(label)
        else:
            if label in state["active_filters"]: 
                state["active_filters"].remove(label)
        
        AplyFilter()


    today = datetime.datetime.now()

    def UpdateEntryDate(e):
        if entry_datepicker.value:
            fecha_entrada = entry_datepicker.value
            fecha_str = fecha_entrada.strftime("%d-%m-%Y")
            
            for text_field in entry_date_inputs:
                text_field.value = fecha_str
                text_field.update()

            min_exit_date = fecha_entrada + datetime.timedelta(days=1)
            exit_datepicker.first_date = min_exit_date
            
            if exit_datepicker.value and exit_datepicker.value <= fecha_entrada:
                exit_datepicker.value = None
                for text_field in exit_date_inputs:
                    text_field.value = ""
                    text_field.update()
            
            exit_datepicker.update()

    def UpdateExitDate(e):
        if exit_datepicker.value:
            fecha_str = exit_datepicker.value.strftime("%d-%m-%Y")
            for text_field in exit_date_inputs:
                text_field.value = fecha_str
                text_field.update()

    def Disponibility(e):
        '''Recoge los dos datos de los datepickers y busca las habitaciones disponibles'''
        
        if not entry_datepicker.value or not exit_datepicker.value:
            entry_datepicker.error_text = "Requerido"
            entry_datepicker.update()
            return
        
        new_ini = entry_datepicker.value.strftime("%Y-%m-%d")
        new_fin = exit_datepicker.value.strftime("%Y-%m-%d")

        try:
            # we get all the rooms available to narrow the filter's pool
            filtered_rooms = GetAvailableRooms(new_ini, new_fin)

            image_rooms = list(map(TakeRoomImage, filtered_rooms))

            state["pool_rooms"] = image_rooms

            AplyFilter()
        
        except Exception as e:
            print("Error de debug: ", e)

    def ChangePersons(e):
        try:
            if e.control.value:
                value = int(e.control.value)
                state["guest_number"] = value
                AplyFilter()
        except ValueError:
            pass
        



    entry_datepicker = ft.DatePicker(
        on_change=UpdateEntryDate,
        cancel_text="Cancelar",
        confirm_text="Confirmar Entrada",
        help_text="Selecciona fecha de llegada",
        first_date=today 
    )
    
    exit_datepicker = ft.DatePicker(
        on_change=UpdateExitDate,
        cancel_text="Cancelar",
        confirm_text="Confirmar Salida",
        help_text="Selecciona fecha de salida",
        first_date=today + datetime.timedelta(days=1)
    )


    page.overlay.extend([entry_datepicker, exit_datepicker])

    def open_entry_picker(e):
        entry_datepicker.open = True
        entry_datepicker.update()

    def open_exit_picker(e):
        exit_datepicker.open = True
        exit_datepicker.update()

    def create_filters_view():     
        input_fecha_entrada = ft.TextField(
            border_radius=35,
            height=30,
            label=ft.Text(value="Fecha Entrada", size=10),
            hint_text="DD-MM-AAAA",
            width=300,
            read_only=True,
            text_style=ft.TextStyle(color="black"),
            suffix_icon=ft.Icons.CALENDAR_MONTH,
            on_click=open_entry_picker 
        )
        
        input_fecha_salida = ft.TextField(
            border_radius=35,
            height=30,
            label=ft.Text(value="Fecha Salida", size=10),
            hint_text="DD-MM-AAAA",
            width=300,
            read_only=True,
            text_style=ft.TextStyle(color="black"), 
            suffix_icon=ft.Icons.CALENDAR_TODAY,
            on_click=open_exit_picker
        )

        entry_date_inputs.append(input_fecha_entrada)
        exit_date_inputs.append(input_fecha_salida)

        def create_checkbox_local(label_text):
            return ft.Checkbox(
                label=ft.Text(value=label_text, color="black", size=12),
                value=False,
                on_change=FilterChange, 
                fill_color={
                    ft.ControlState.HOVERED: "grey", 
                    ft.ControlState.FOCUSED: "grey", 
                    ft.ControlState.SELECTED: "blue", 
                    ft.ControlState.DEFAULT: "white",                
                },
                check_color="white" 
            )

        return ft.Column(
            alignment=ft.Alignment.TOP_CENTER,
            scroll=ft.ScrollMode.AUTO, 
            controls=[
                ft.Text(value="Busca tu mejor habitación", color="black", size=20, weight="bold", text_align=ft.TextAlign.CENTER),
                ft.Divider(),
                
                ft.Text(value="Fechas de Estancia", color="black", weight="bold"),
                ft.Container(height=10), 
                input_fecha_entrada,     
                ft.Container(height=5),  
                input_fecha_salida,      
                
                ft.Container(height=15), 
                
                ft.TextField(
                    border_radius=35, height=30,
                    label=ft.Text(value="Numero de personas", size=10),
                    keyboard_type=ft.KeyboardType.NUMBER,
                    input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9]", replacement_string=""),
                    on_change=ChangePersons

                ),
                ft.Container(height=10),
                ft.ElevatedButton(content=ft.Text("Buscar Disponibilidad"), bgcolor="blue", color="white", width=float("inf"), on_click=lambda e: Disponibility(e)),
                ft.Divider(),
                
                ft.Row(
                    vertical_alignment=ft.CrossAxisAlignment.START,
                    controls=[
                        ft.Column(controls=[
                            ft.Text(value="Tipo de cama", color="black", weight="bold", size=16),
                            create_checkbox_local("King"),
                            create_checkbox_local("Matrimonio"),
                            create_checkbox_local("Individual"),
                            create_checkbox_local("Cuna")
                        ]),
                        ft.Column(controls=[
                            ft.Text(value="Categoría", color="black", weight="bold", size=16),
                            create_checkbox_local("Presidential"),
                            create_checkbox_local("Luxury"),
                            create_checkbox_local("Privacy"),
                            create_checkbox_local("Apartment"),
                            create_checkbox_local("Regular"),
                        ]),                   
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                ft.Divider(),
                ft.Row(
                    vertical_alignment=ft.CrossAxisAlignment.START,
                    controls=[
                        ft.Column(controls=[
                            ft.Text(value="Servicios", color="black", weight="bold", size=16),
                            create_checkbox_local("Garaje"),
                            create_checkbox_local("Wifi"),
                            create_checkbox_local("TV"),
                            create_checkbox_local("Jacuzzi")
                        ]),
                        ft.Column(controls=[
                            ft.Text(value="Precio", color="black", weight="bold", size=16),
                            create_checkbox_local("0€ - 50€"),
                            create_checkbox_local("50€ - 100€"),
                            create_checkbox_local("100€ - 150€"),
                            create_checkbox_local("100€ - 200€"),
                            create_checkbox_local("+200€"),
                        ]),                   
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                )
            ],
        )

    desktop_filters_view = create_filters_view()
    mobile_filters_view = create_filters_view()

    desktop_filter_container = ft.Container(
        width=350,
        padding=20,
        alignment=ft.Alignment.TOP_LEFT,
        border=ft.Border(right=ft.BorderSide(width=1, color="grey")),
        content=desktop_filters_view 
    )

    def close_drawer(e):
        drawer_container.visible = False
        drawer_container.update()
    
    drawer_container = ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Text("Filtros", size=20, weight="bold", color="black"),
                        ft.IconButton(
                            icon=ft.Icons.CLOSE,
                            on_click=close_drawer,
                            icon_color="black"
                        )
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),
                ft.Divider(),
                mobile_filters_view
            ],
            scroll=ft.ScrollMode.AUTO,
        ),
        bgcolor="white",
        width=350,
        height=page.height if page.height else 600,
        padding=20,
        shadow=ft.BoxShadow(
            spread_radius=1,
            blur_radius=15,
            color=ft.Colors.BLACK54,
        ),
        visible=False,
        animate=ft.Animation(300, ft.AnimationCurve.EASE_OUT),
        right=0,
        top=0,
    )
    
    def open_filters_mobile(e):
        print("Abriendo menú...")
        drawer_container.visible = True
        drawer_container.update()
        print("Drawer debería estar abierto")

    fab_filters = ft.FloatingActionButton(
        icon=ft.Icons.FILTER_LIST,
        bgcolor="blue",
        content=ft.Text("Filtros"),
        visible=False, 
        on_click=open_filters_mobile
    )

    def responsive(e):
        if not page.width: return
        
        is_mobile = page.width < 800
        menu.resize(page.width)
        desktop_filter_container.visible = not is_mobile
        fab_filters.visible = is_mobile

        if page.width < 1000:
            grid_rooms.runs_count = 1 
        elif page.width < 1450:
            grid_rooms.runs_count = 2
        elif page.width < 1750:
            grid_rooms.runs_count = 3
        else:
            grid_rooms.runs_count = 4
            
        try: page.update()
        except: pass

    page.on_resize = responsive
    initial_rooms = TakeAllRooms()
    LoadCards(initial_rooms, should_update=False)

    if page.width: responsive(None)

    return ft.View(
        route="/allRooms",
        bgcolor="white",
        padding=0,
        floating_action_button=fab_filters,
        controls=[
            ft.Stack(
                expand=True,
                controls=[
                    ft.Column(
                        expand=True,
                        controls=[
                            menu,
                            ft.Divider(height=1),
                            ft.Row(
                                expand=True,
                                controls=[
                                    desktop_filter_container,
                                    ft.Container(
                                        expand=True,
                                        content=grid_rooms,
                                        padding=10
                                    )
                                ],
                                vertical_alignment=ft.CrossAxisAlignment.START
                            )
                        ]
                    ),
                    drawer_container
                ]
            )
        ]
    )