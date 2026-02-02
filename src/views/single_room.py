import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import flet as ft
from src.components.navigation_bar import NavigationBar
import src.Backend.RoomsManagement as rm

def singleRoom(page: ft.Page):

    room_info = getattr(page, "selected_room_data", None)
    
    data = room_info["data"]
    room_type_name = room_info["type"]
    foto_portada = room_info.get("foto_portada")

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
        height=400,
        spacing=12,
        controls=[
            img(foto_portada),
            # Columna derecha
            ft.Column(
                spacing=12,
                expand=1,
                controls=[
                    ft.Row(
                        spacing=12,
                        expand=1,
                        controls=[
                            img(rm.TakeRandomPhotoByRoomType(room_info["type"])),
                            img(rm.TakeRandomPhotoByRoomType(room_info["type"])),
                        ],
                    ),
                    ft.Row(
                        spacing=12,
                        expand=1,
                        controls=[
                            img(rm.TakeRandomPhotoByRoomType(room_info["type"])),
                            img(rm.TakeRandomPhotoByRoomType(room_info["type"])),
                        ],
                    ),
                ],
            ),
        ],
    )

    tipo_habitacion = ft.Text(
            value=room_type_name,
            color="black",
            size=32,
            weight="bold",
    )

    propiedades = ft.Text(
            value=f"Valoración: {data['avg_rating']} - Precio: {data['price']}$/noche" if room_info else "Cargando...", 
            color="black",
            size=16,
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
                                imagenes_habitacion,
                                tipo_habitacion,
                                propiedades
                        ]
                    ),
                ]
            )
        ]
     )