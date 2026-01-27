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
        label="Fecha de entrada",
        hint_text="DD-MM-AAAA",
        width=300,
        read_only=True,  
        on_click=lambda e: page.show_dialog(datepicker) 
    )

    menu_filter = ft.Column(
        controls=[
            ft.Text(value="Busca tu mejor habitacion", color="black", size=20, weight="bold"),
            ft.Text(value="Check-in date", color="black"),
            
            input_fecha 
        ]
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
                                            alignment=ft.Alignment.TOP_LEFT
                                        ),
                                        ft.VerticalDivider(width=8),
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