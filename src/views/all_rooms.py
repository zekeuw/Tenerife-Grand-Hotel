import flet as ft
from src.components.navigation_bar import NavigationBar
from datetime import datetime 
from src.Backend.RoomsManagement import TakeAllRooms, TakeRandomPhotoByRoomType, FilterRooms
import random

ROOMS_TYPES = ["Presidential", "Luxury", "Privacy", "Apartment", "Regular"]
cards_list = []
current_card_list = []
filters = []

def AllRoomCards():
    def CreateRoomCard(data, room_type, id_room):
        id_text = ft.Text(value=id_room)
        
        return ft.Container(
            width=300,
            height=320,
            padding= 5,
            margin=15,
            bgcolor="white",
            border_radius=15,
            shadow= ft.BoxShadow(
                blur_radius=5,
                color=ft.Colors.BLACK,
            ),
            ink=True,
            on_click=lambda e: print(id_room),
            content= ft.Column(
                controls=[
                    ft.Image(
                        src=f"{TakeRandomPhotoByRoomType(room_type)}",
                        width=float("inf"),
                        height=180,
                        border_radius=5,
                        fit= "COVER"
                    ),
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                id_text,
                                ft.Text(value=room_type, color="black", size=18),
                                ft.Text(value=f"{data['description']}", color="black",size=12, text_align=ft.TextAlign.JUSTIFY),
                                ft.Text(value=f"Desde {data['price']}$/noche", color="black",weight="bold")
                            ]
                        )
                    )
                ]

            )
        )

    list_all_rooms = TakeAllRooms()
    
    
    global cards_list

    for room_type in ROOMS_TYPES:
        if room_type in list_all_rooms[0]:
            type_data = list_all_rooms[0][room_type]
            for id_room in type_data:
                if id_room in ["images", "reviews"]: continue
                card = CreateRoomCard(list_all_rooms[0][room_type][id_room], room_type, id_room)
                cards_list.append(card)

def FilterRoomCards(filters):
    global current_card_list
    
    if not filters: current_card_list.copy(cards_list)
    else:   
        print("FILTEEER")
        print(card.id for card in cards_list)

        filtered_rooms = FilterRooms(filters=filters)
        

def allRooms(page: ft.Page):
    menu = NavigationBar(page)
    global filters

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

    filters_column = ft.Column(
            alignment=ft.Alignment.TOP_CENTER,
            controls=[
                ft.Text(value="Busca tu mejor habitacion", color="black", size=20, weight="bold", text_align=ft.TextAlign.CENTER, width=float("inf")),
                ft.Text(value="Check-in date", color="black"),
                input_fecha,
                ft.Text(value="Check-out date", color="black"),
                input_fecha,
                ft.TextField(
                    border_radius=35,
                    height=30,
                    label=ft.Text(value="Numero de personas", size=10),
                    keyboard_type=ft.KeyboardType.NUMBER,
                    input_filter=ft.InputFilter(allow=True, regex_string=r"[0-9]", replacement_string="")
                ),
                ft.Button(
                    content = "Buscar",
                    bgcolor = "blue",
                    color = "white",
                    width=float("inf")
                ),
                ft.Divider(),
                ft.Row(
                    vertical_alignment=ft.CrossAxisAlignment.START,
                    controls=[
                        ft.Column(
                            controls=[
                                ft.Text(value="Tipo de cama", color="black", weight="bold", size=18),
                                ft.Checkbox(
                                    label= ft.Text(value="King", color="black", size=12, text_align=ft.Alignment.CENTER), 
                                    value=False,
                                    on_change=lambda e: (filters.append(e.control.label.value) if e.control.value else filters.remove(e.control.label.value), FilterRoomCards(filters)),
                                    check_color="white", 
                                    fill_color={
                                            ft.ControlState.SELECTED: "blue",  
                                            ft.ControlState.DEFAULT: "white",  
                                        },
                                ),
                                ft.Checkbox(
                                    label= ft.Text(value="Matrimonio", color="black", size=12, text_align=ft.Alignment.TOP_CENTER), 
                                    value=False,
                                    on_change=lambda e: (filters.append(e.control.label.value) if e.control.value else filters.remove(e.control.label.value), FilterRoomCards(filters)),
                                    check_color="white", 
                                    fill_color={
                                            ft.ControlState.SELECTED: "blue",  
                                            ft.ControlState.DEFAULT: "white",  
                                        },
                                ),
                                ft.Checkbox(
                                    label= ft.Text(value="Individual", color="black", size=12, text_align=ft.Alignment.TOP_CENTER), 
                                    value=False,
                                    on_change=lambda e: (filters.append(e.control.label.value) if e.control.value else filters.remove(e.control.label.value), FilterRoomCards(filters)),
                                    check_color="white", 
                                    fill_color={
                                            ft.ControlState.SELECTED: "blue",  
                                            ft.ControlState.DEFAULT: "white",  
                                        },
                                ),
                                ft.Checkbox(
                                    label= ft.Text(value="Cuna", color="black", size=12, text_align=ft.Alignment.TOP_CENTER), 
                                    value=False,
                                    on_change=lambda e: (filters.append(e.control.label.value) if e.control.value else filters.remove(e.control.label.value), FilterRoomCards(filters)),
                                    check_color="white", 
                                    fill_color={
                                            ft.ControlState.SELECTED: "blue",  
                                            ft.ControlState.DEFAULT: "white",  
                                        },
                                )
                            ], 
                        ),
                        ft.Column(
                            controls=[
                                ft.Text(value="Tipo de Habitacion", color="black", weight="bold", size=18),
                                ft.Checkbox(
                                    label= ft.Text(value="Presidential", color="black", size=12, text_align=ft.Alignment.TOP_CENTER), 
                                    value=False,
                                    on_change=lambda e: (filters.append(e.control.label.value) if e.control.value else filters.remove(e.control.label.value), FilterRoomCards(filters)),
                                    check_color="white", 
                                    fill_color={
                                            ft.ControlState.SELECTED: "blue",  
                                            ft.ControlState.DEFAULT: "white",  
                                        },
                                ),
                                ft.Checkbox(
                                    label= ft.Text(value="Luxury", color="black", size=12, text_align=ft.Alignment.TOP_CENTER), 
                                    value=False,
                                    on_change=lambda e: (filters.append(e.control.label.value) if e.control.value else filters.remove(e.control.label.value), FilterRoomCards(filters)),
                                    check_color="white", 
                                    fill_color={
                                            ft.ControlState.SELECTED: "blue",  
                                            ft.ControlState.DEFAULT: "white",  
                                        },
                                ),
                                ft.Checkbox(
                                    label= ft.Text(value="Privacy", color="black", size=12, text_align=ft.Alignment.TOP_CENTER), 
                                    value=False,
                                    on_change=lambda e: (filters.append(e.control.label.value) if e.control.value else filters.remove(e.control.label.value), FilterRoomCards(filters)),
                                    check_color="white", 
                                    fill_color={
                                            ft.ControlState.SELECTED: "blue",  
                                            ft.ControlState.DEFAULT: "white",  
                                        },
                                ),
                                ft.Checkbox(
                                    label= ft.Text(value="Apartment", color="black", size=12, text_align=ft.Alignment.TOP_CENTER), 
                                    value=False,
                                    on_change=lambda e: (filters.append(e.control.label.value) if e.control.value else filters.remove(e.control.label.value), FilterRoomCards(filters)),
                                    check_color="white", 
                                    fill_color={
                                            ft.ControlState.SELECTED: "blue",  
                                            ft.ControlState.DEFAULT: "white",  
                                        },
                                ),
                                ft.Checkbox(
                                    label= ft.Text(value="Regular", color="black", size=12, text_align=ft.Alignment.TOP_CENTER), 
                                    value=False,
                                    on_change=lambda e: (filters.append(e.control.label.value) if e.control.value else filters.remove(e.control.label.value), FilterRoomCards(filters)),
                                    check_color="white", 
                                    fill_color={
                                            ft.ControlState.SELECTED: "blue",  
                                            ft.ControlState.DEFAULT: "white",  
                                        },
                                ),

                            ], 
                        ),                   
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    
                ),
                ft.Row(
                    vertical_alignment=ft.CrossAxisAlignment.START,
                    controls=[
                        ft.Column(
                            controls=[
                                ft.Text(value="Contenido", color="black", weight="bold", size=18),
                                ft.Checkbox(
                                    label= ft.Text(value="Garaje", color="black", size=12, text_align=ft.Alignment.CENTER), 
                                    value=False,
                                    on_change=lambda e: (filters.append(e.control.label.value) if e.control.value else filters.remove(e.control.label.value), FilterRoomCards(filters)),
                                    check_color="white", 
                                    fill_color={
                                            ft.ControlState.SELECTED: "blue",  
                                            ft.ControlState.DEFAULT: "white",  
                                        },
                                ),
                                ft.Checkbox(
                                    label= ft.Text(value="Wifi", color="black", size=12, text_align=ft.Alignment.TOP_CENTER), 
                                    value=False,
                                    on_change=lambda e: (filters.append(e.control.label.value) if e.control.value else filters.remove(e.control.label.value), FilterRoomCards(filters)),
                                    check_color="white", 
                                    fill_color={
                                            ft.ControlState.SELECTED: "blue",  
                                            ft.ControlState.DEFAULT: "white",  
                                        },
                                ),
                                ft.Checkbox(
                                    label= ft.Text(value="TV", color="black", size=12, text_align=ft.Alignment.TOP_CENTER), 
                                    value=False,
                                    on_change=lambda e: (filters.append(e.control.label.value) if e.control.value else filters.remove(e.control.label.value), FilterRoomCards(filters)),
                                    check_color="white", 
                                    fill_color={
                                            ft.ControlState.SELECTED: "blue",  
                                            ft.ControlState.DEFAULT: "white",  
                                        },
                                ),
                                ft.Checkbox(
                                    label= ft.Text(value="Cuna", color="black", size=12, text_align=ft.Alignment.TOP_CENTER), 
                                    value=False,
                                    on_change=lambda e: (filters.append(e.control.label.value) if e.control.value else filters.remove(e.control.label.value), FilterRoomCards(filters)),
                                    check_color="white", 
                                    fill_color={
                                            ft.ControlState.SELECTED: "blue",  
                                            ft.ControlState.DEFAULT: "white",  
                                        },
                                )
                            ], 
                        ),
                        ft.Column(
                            controls=[
                                ft.Text(value="Precio por noche", color="black", weight="bold", size=18),
                                ft.Checkbox(
                                    label= ft.Text(value="0€ - 50€", color="black", size=12, text_align=ft.Alignment.TOP_CENTER), 
                                    value=False,
                                    on_change=lambda e: (filters.append(e.control.label.value) if e.control.value else filters.remove(e.control.label.value), FilterRoomCards(filters)),
                                    check_color="white", 
                                    fill_color={
                                            ft.ControlState.SELECTED: "blue",  
                                            ft.ControlState.DEFAULT: "white",  
                                        },
                                ),
                                ft.Checkbox(
                                    label= ft.Text(value="50€ - 100€", color="black", size=12, text_align=ft.Alignment.TOP_CENTER), 
                                    value=False,
                                    on_change=lambda e: (filters.append(e.control.label.value) if e.control.value else filters.remove(e.control.label.value), FilterRoomCards(filters)),
                                    check_color="white", 
                                    fill_color={
                                            ft.ControlState.SELECTED: "blue",  
                                            ft.ControlState.DEFAULT: "white",  
                                        },
                                ),
                                ft.Checkbox(
                                    label= ft.Text(value="100€ - 150€", color="black", size=12, text_align=ft.Alignment.TOP_CENTER), 
                                    value=False,
                                    on_change=lambda e: (filters.append(e.control.label.value) if e.control.value else filters.remove(e.control.label.value), FilterRoomCards(filters)),
                                    check_color="white", 
                                    fill_color={
                                            ft.ControlState.SELECTED: "blue",  
                                            ft.ControlState.DEFAULT: "white",  
                                        },
                                ),
                                ft.Checkbox(
                                    label= ft.Text(value="100€ - 200€", color="black", size=12, text_align=ft.Alignment.TOP_CENTER), 
                                    value=False,
                                    on_change=lambda e: (filters.append(e.control.label.value) if e.control.value else filters.remove(e.control.label.value), FilterRoomCards(filters)),
                                    check_color="white", 
                                    fill_color={
                                            ft.ControlState.SELECTED: "blue",  
                                            ft.ControlState.DEFAULT: "white",  
                                        },
                                ),
                                ft.Checkbox(
                                    label= ft.Text(value="+200€", color="black", size=12, text_align=ft.Alignment.TOP_CENTER), 
                                    value=False,
                                    on_change=lambda e: (filters.append(e.control.label.value) if e.control.value else filters.remove(e.control.label.value), FilterRoomCards(filters)),
                                    check_color="white", 
                                    fill_color={
                                            ft.ControlState.SELECTED: "blue",  
                                            ft.ControlState.DEFAULT: "white",  
                                        },
                                ),

                            ], 
                        ),                   
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
        content=None 
    )

    mobile_filter_drawer = ft.NavigationDrawer(
        controls=[
            ft.Container(padding=20, content=None)
        ],
        bgcolor="white",
    )
    async def open_filters_mobile(e):
        print("Botón presionado")
        await page.show_end_drawer()
    fab_filters = ft.FloatingActionButton(
        icon=ft.Icons.FILTER_LIST,
        bgcolor="blue",
        content="Filtros",
        visible=False, 
        on_click=open_filters_mobile
    )

    if not cards_list: AllRoomCards()
    
    def responsive(e):
        if not page.width: return
        is_mobile = page.width < 800
        
        menu.resize(page.width)

        desktop_filter_container.content = None if is_mobile else filters_column
        desktop_filter_container.visible = False if is_mobile else True
        mobile_filter_drawer.controls[0].content = filters_column if is_mobile else None
        fab_filters.visible = True if is_mobile else False

        try:
            page.update()
        except Exception:
            pass

    page.on_resize = responsive
    if page.width:
        responsive(None)
    return ft.View(
        route="/allRooms",
        bgcolor="white",
        padding=0,
        end_drawer=mobile_filter_drawer, 
        floating_action_button=fab_filters,
        controls=[
            ft.Stack(   
                expand=True,
                controls=[
                    ft.Column(
                        expand=True,
                        controls=[
                                menu,
                                ft.Divider(),
                                ft.Row(
                                    expand=True,
                                    controls=[
                                        desktop_filter_container,
                                        ft.GridView(
                                                expand=True,
                                                controls= random.sample(cards_list, len(cards_list))[0:12],
                                                max_extent=400, 
                                                child_aspect_ratio=1,
                                                spacing=20,
                                                run_spacing=20
                                        )
                                    ],
                                    vertical_alignment=ft.CrossAxisAlignment.START
                                )
                            ]
                        ),
                        
                    ]
                )
            ]
        )