import flet as ft
from src.components.navigation_bar import NavigationBar
from src.Backend.RoomsManagement import TakeAllRooms, TakeRandomPhotoByRoomType, FilterRooms
import random

def CreateRoomCard(room_data, on_click_handler=None):
    room_id = room_data.get("id", room_data.get("_id", "Unknown"))
    room_type = room_data.get("category", "Regular") 
    price = room_data.get("price", 0)
    description = room_data.get("description", "Sin descripción")
    
    img_src = f"{TakeRandomPhotoByRoomType(room_type)}"

    return ft.Container(
        width=300,
        height=320,
        padding=5,
        margin=15,
        bgcolor="white",
        border_radius=15,
        shadow=ft.BoxShadow(
            blur_radius=5,
            color=ft.Colors.BLACK,
        ),
        ink=True,
        on_click=lambda e: print(f"Click en habitación: {room_id}"), 
        content=ft.Column(
            controls=[
                ft.Image(
                    src=img_src,
                    width=float("inf"),
                    height=180,
                    border_radius=5,
                    fit="COVER",
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
    menu = NavigationBar(page)
    
    active_filters = [] 
    
    grid_rooms = ft.GridView(
        expand=True,
        runs_count=5, 
        max_extent=350,
        child_aspect_ratio=0.8,
        spacing=20,
        run_spacing=20,
        controls=[] 
    )

    
    def load_cards(rooms_data, should_update=False):
        cards = []
        for room in rooms_data:
            cards.append(CreateRoomCard(room))
        
        grid_rooms.controls = cards
        
        if should_update:
            grid_rooms.update()

    def on_filter_change(e):
        label = e.control.label.value
        is_checked = e.control.value

        if is_checked:
            if label not in active_filters:
                active_filters.append(label)
        else:
            if label in active_filters:
                active_filters.remove(label)
        
        print(f"Filtros activos: {active_filters}")
        
        if not active_filters:
            rooms = TakeAllRooms()
        else:
            rooms = FilterRooms(active_filters)
        
        load_cards(rooms, should_update=True)


    initial_rooms = TakeAllRooms()
    load_cards(initial_rooms, should_update=False)


    def actualizar_fecha(e):
        input_fecha.value = datepicker.value.strftime("%d-%m-%Y")
        input_fecha.update()

    datepicker = ft.DatePicker(
        on_change=actualizar_fecha,
        cancel_text="Cancelar",
        confirm_text="Confirmar"
    )

    if datepicker not in page.overlay:
        page.overlay.append(datepicker)

    input_fecha = ft.TextField(
        border_radius=35,
        height=30,
        label=ft.Text(value="Fecha entrada", size=10),
        hint_text="DD-MM-AAAA",
        width=300,
        read_only=True,  
        on_click=lambda e: page.show_dialog(datepicker) 
    )

    def create_checkbox(label_text):
        return ft.Checkbox(
            label=ft.Text(value=label_text, color="black", size=12),
            value=False,
            on_change=on_filter_change, 
            check_color="white",
            fill_color={ft.ControlState.SELECTED: "blue", ft.ControlState.DEFAULT: "white"}
        )

    filters_column = ft.Column(
            alignment=ft.Alignment.TOP_CENTER,
            scroll=ft.ScrollMode.AUTO, 
            controls=[
                ft.Text(value="Busca tu mejor habitación", color="black", size=20, weight="bold", text_align=ft.TextAlign.CENTER),
                ft.Divider(),
                ft.Text(value="Fechas", color="black", weight="bold"),
                input_fecha,
                ft.TextField(
                    border_radius=35, height=30,
                    label=ft.Text(value="Numero de personas", size=10),
                    keyboard_type=ft.KeyboardType.NUMBER,
                    input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9]", replacement_string="")
                ),
                ft.Button(content="Buscar Disponibilidad", bgcolor="blue", color="white", width=float("inf")),
                ft.Divider(),
                
                ft.Row(
                    vertical_alignment=ft.CrossAxisAlignment.START,
                    controls=[
                        ft.Column(controls=[
                            ft.Text(value="Tipo de cama", color="black", weight="bold", size=16),
                            create_checkbox("King"),
                            create_checkbox("Matrimonio"),
                            create_checkbox("Individual"),
                            create_checkbox("Cuna")
                        ]),
                        ft.Column(controls=[
                            ft.Text(value="Categoría", color="black", weight="bold", size=16),
                            create_checkbox("Presidential"),
                            create_checkbox("Luxury"),
                            create_checkbox("Privacy"),
                            create_checkbox("Apartment"),
                            create_checkbox("Regular"),
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
                            create_checkbox("Garaje"),
                            create_checkbox("Wifi"),
                            create_checkbox("TV"),
                            create_checkbox("Jacuzzi")
                        ]),
                        ft.Column(controls=[
                            ft.Text(value="Precio", color="black", weight="bold", size=16),
                            create_checkbox("0€ - 50€"),
                            create_checkbox("50€ - 100€"),
                            create_checkbox("100€ - 150€"),
                            create_checkbox("100€ - 200€"),
                            create_checkbox("+200€"),
                        ]),                   
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                )
            ],
        )

    desktop_filter_container = ft.Container(
        width=350,
        padding=20,
        alignment=ft.Alignment.TOP_LEFT,
        border=ft.border.only(right=ft.BorderSide(width=1, color="grey")),
        content=filters_column 
    )

    mobile_filter_drawer = ft.NavigationDrawer(
        controls=[
            ft.Container(padding=20, content=filters_column) 
        ],
        bgcolor="white",
    )

    async def open_filters_mobile(e):
        page.end_drawer = mobile_filter_drawer
        mobile_filter_drawer.open = True
        await page.update_async()

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
        
        if page.width < 600: grid_rooms.runs_count = 1
        elif page.width < 900: grid_rooms.runs_count = 2
        elif page.width < 1200: grid_rooms.runs_count = 3
        else: grid_rooms.runs_count = 4

        try:
            page.update()
        except:
            pass

    page.on_resize = responsive
    
    if page.width: responsive(None)

    return ft.View(
        route="/allRooms",
        bgcolor="white",
        padding=0,
        end_drawer=mobile_filter_drawer, 
        floating_action_button=fab_filters,
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
            )
        ]
    )