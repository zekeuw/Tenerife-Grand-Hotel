import flet as ft
from src.components.navigation_bar import NavigationBar
from datetime import datetime 

def allRooms(page: ft.Page):
    menu = NavigationBar(page)

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

    menu_filter = ft.Container(
        padding=20,
        content= ft.Column(
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
                                    on_change=lambda e: print(f"Estado Wifi: {e.control.value}"),
                                    check_color="white", 
                                    fill_color={
                                            ft.ControlState.SELECTED: "blue",  
                                            ft.ControlState.DEFAULT: "white",  
                                        },
                                ),
                                ft.Checkbox(
                                    label= ft.Text(value="Matrimonio", color="black", size=12, text_align=ft.Alignment.TOP_CENTER), 
                                    value=False,
                                    on_change=lambda e: print(f"Estado Wifi: {e.control.value}"),
                                    check_color="white", 
                                    fill_color={
                                            ft.ControlState.SELECTED: "blue",  
                                            ft.ControlState.DEFAULT: "white",  
                                        },
                                ),
                                ft.Checkbox(
                                    label= ft.Text(value="Individual", color="black", size=12, text_align=ft.Alignment.TOP_CENTER), 
                                    value=False,
                                    on_change=lambda e: print(f"Estado Wifi: {e.control.value}"),
                                    check_color="white", 
                                    fill_color={
                                            ft.ControlState.SELECTED: "blue",  
                                            ft.ControlState.DEFAULT: "white",  
                                        },
                                ),
                                ft.Checkbox(
                                    label= ft.Text(value="Cuna", color="black", size=12, text_align=ft.Alignment.TOP_CENTER), 
                                    value=False,
                                    on_change=lambda e: print(f"Estado Wifi: {e.control.value}"),
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
                                    on_change=lambda e: print(f"Estado Wifi: {e.control.value}"),
                                    check_color="white", 
                                    fill_color={
                                            ft.ControlState.SELECTED: "blue",  
                                            ft.ControlState.DEFAULT: "white",  
                                        },
                                ),
                                ft.Checkbox(
                                    label= ft.Text(value="Luxury", color="black", size=12, text_align=ft.Alignment.TOP_CENTER), 
                                    value=False,
                                    on_change=lambda e: print(f"Estado Wifi: {e.control.value}"),
                                    check_color="white", 
                                    fill_color={
                                            ft.ControlState.SELECTED: "blue",  
                                            ft.ControlState.DEFAULT: "white",  
                                        },
                                ),
                                ft.Checkbox(
                                    label= ft.Text(value="Privacy", color="black", size=12, text_align=ft.Alignment.TOP_CENTER), 
                                    value=False,
                                    on_change=lambda e: print(f"Estado Wifi: {e.control.value}"),
                                    check_color="white", 
                                    fill_color={
                                            ft.ControlState.SELECTED: "blue",  
                                            ft.ControlState.DEFAULT: "white",  
                                        },
                                ),
                                ft.Checkbox(
                                    label= ft.Text(value="Apartment", color="black", size=12, text_align=ft.Alignment.TOP_CENTER), 
                                    value=False,
                                    on_change=lambda e: print(f"Estado Wifi: {e.control.value}"),
                                    check_color="white", 
                                    fill_color={
                                            ft.ControlState.SELECTED: "blue",  
                                            ft.ControlState.DEFAULT: "white",  
                                        },
                                ),
                                ft.Checkbox(
                                    label= ft.Text(value="Regular", color="black", size=12, text_align=ft.Alignment.TOP_CENTER), 
                                    value=False,
                                    on_change=lambda e: print(f"Estado Wifi: {e.control.value}"),
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
                                    on_change=lambda e: print(f"Estado Wifi: {e.control.value}"),
                                    check_color="white", 
                                    fill_color={
                                            ft.ControlState.SELECTED: "blue",  
                                            ft.ControlState.DEFAULT: "white",  
                                        },
                                ),
                                ft.Checkbox(
                                    label= ft.Text(value="Wifi", color="black", size=12, text_align=ft.Alignment.TOP_CENTER), 
                                    value=False,
                                    on_change=lambda e: print(f"Estado Wifi: {e.control.value}"),
                                    check_color="white", 
                                    fill_color={
                                            ft.ControlState.SELECTED: "blue",  
                                            ft.ControlState.DEFAULT: "white",  
                                        },
                                ),
                                ft.Checkbox(
                                    label= ft.Text(value="TV", color="black", size=12, text_align=ft.Alignment.TOP_CENTER), 
                                    value=False,
                                    on_change=lambda e: print(f"Estado Wifi: {e.control.value}"),
                                    check_color="white", 
                                    fill_color={
                                            ft.ControlState.SELECTED: "blue",  
                                            ft.ControlState.DEFAULT: "white",  
                                        },
                                ),
                                ft.Checkbox(
                                    label= ft.Text(value="Cuna", color="black", size=12, text_align=ft.Alignment.TOP_CENTER), 
                                    value=False,
                                    on_change=lambda e: print(f"Estado Wifi: {e.control.value}"),
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
                                    on_change=lambda e: print(f"Estado Wifi: {e.control.value}"),
                                    check_color="white", 
                                    fill_color={
                                            ft.ControlState.SELECTED: "blue",  
                                            ft.ControlState.DEFAULT: "white",  
                                        },
                                ),
                                ft.Checkbox(
                                    label= ft.Text(value="50€ - 100€", color="black", size=12, text_align=ft.Alignment.TOP_CENTER), 
                                    value=False,
                                    on_change=lambda e: print(f"Estado Wifi: {e.control.value}"),
                                    check_color="white", 
                                    fill_color={
                                            ft.ControlState.SELECTED: "blue",  
                                            ft.ControlState.DEFAULT: "white",  
                                        },
                                ),
                                ft.Checkbox(
                                    label= ft.Text(value="100€ - 150€", color="black", size=12, text_align=ft.Alignment.TOP_CENTER), 
                                    value=False,
                                    on_change=lambda e: print(f"Estado Wifi: {e.control.value}"),
                                    check_color="white", 
                                    fill_color={
                                            ft.ControlState.SELECTED: "blue",  
                                            ft.ControlState.DEFAULT: "white",  
                                        },
                                ),
                                ft.Checkbox(
                                    label= ft.Text(value="100€ - 200€", color="black", size=12, text_align=ft.Alignment.TOP_CENTER), 
                                    value=False,
                                    on_change=lambda e: print(f"Estado Wifi: {e.control.value}"),
                                    check_color="white", 
                                    fill_color={
                                            ft.ControlState.SELECTED: "blue",  
                                            ft.ControlState.DEFAULT: "white",  
                                        },
                                ),
                                ft.Checkbox(
                                    label= ft.Text(value="+200€", color="black", size=12, text_align=ft.Alignment.TOP_CENTER), 
                                    value=False,
                                    on_change=lambda e: print(f"Estado Wifi: {e.control.value}"),
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
    )

    all_rooms_layout = ft.GridView(
        expand=True,
        runs_count=5,
        max_extent=300,
        child_aspect_ratio=1.0,
        spacing=10,
        run_spacing=10,
    )

    def responsive(e):
        if not page.width: return
        is_mobile = page.width < 800
        
        menu.resize(page.width)

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
        controls=[
            ft.Stack(
                
                expand=True,
                controls=[
                    ft.Column(
                        scroll=ft.ScrollMode.AUTO, 
                        expand=True,
                        controls=[
                                menu,
                                ft.Divider(),
                                ft.Row(
                                    expand=True,
                                    controls=[
                                        ft.Container(
                                            content=menu_filter,
                                            width=350,
                                            padding=20,
                                            alignment=ft.Alignment.TOP_LEFT,
                                            border=ft.Border.only(
                                                right=ft.BorderSide(width=1, color="grey")
                                            ),
                                        ),
                                        ft.Container(
                                            content=all_rooms_layout,
                                            expand=True
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