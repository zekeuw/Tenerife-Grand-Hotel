import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import flet as ft
from src.components.navigation_bar import NavigationBar

def singleRoom(page: ft.Page):

    menu = NavigationBar(page)

    def img(src, expand=1):
        return ft.Container(
            expand=expand,
            border_radius=16,
            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
            content=ft.Image(
                src=src,
                fit=ft.BoxFit.COVER,
            ),
        )

    imagenes_habitacion = ft.Row(
        spacing=12,
        controls=[
            # Imagen grande izquierda
            img("media/img/Rooms/Apartments/Apartment1.jpg", expand=1),

            # Columna derecha
            ft.Column(
                spacing=12,
                expand=1,
                controls=[
                    ft.Row(
                        spacing=12,
                        expand=1,
                        controls=[
                            img("media/img/Rooms/Apartments/Apartment1.jpg"),
                            img("media/img/Rooms/Apartments/Apartment1.jpg"),
                        ],
                    ),
                    ft.Row(
                        spacing=12,
                        expand=1,
                        controls=[
                            img("media/img/Rooms/Apartments/Apartment1.jpg"),
                            img("media/img/Rooms/Apartments/Apartment1.jpg"),
                        ],
                    ),
                ],
            ),
        ],
    )

    def responsive(e):
        if not page.width: return
        menu.resize(page.width)

    page.on_resize = responsive
    if page.width:
        responsive(None)

    return ft.View(
        route="/logIn",
        bgcolor="white",
        padding=20,
        controls=[
            ft.Stack(
                expand=True,
                controls=[
                    ft.Column(
                        scroll=ft.ScrollMode.AUTO, 
                        expand=True,
                        controls=[
                                menu,
                                imagenes_habitacion
                        ]
                    ),
                ]
            )
        ]
     )