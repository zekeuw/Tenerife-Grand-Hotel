import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import flet as ft
from src.components.navigation_bar import NavigationBar
import src.Backend.RoomsManagement as rm
from random import choice

def singleRoom(page: ft.Page):

    room_info = getattr(page, "selected_room_data", None)
    
    data = room_info["data"]
    room_type_name = room_info["type"]
    foto_portada = room_info.get("foto_portada")

    menu = NavigationBar(page)

    def img(src, h=200):
        return ft.Container(
            border_radius=16,
            height=h,
            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
            content=ft.Image(src=src, fit=ft.BoxFit.COVER),
        )

    # Contenedor principal adaptable
    imagenes_habitacion = ft.Container(
        # Esto centra el bloque en PC y deja margen en móvil
        alignment=ft.Alignment.CENTER,
        padding=ft.padding.all(20),
        content=ft.ResponsiveRow(
            spacing=12,
            run_spacing=12,
            controls=[
                # IMAGEN PRINCIPAL: 12 columnas en móvil (sm), 8 en PC (md)
                ft.Container(
                    col={"sm": 12, "md": 8},
                    # En móvil bajamos la altura para que no ocupe toda la pantalla
                    content=img(foto_portada, h=300 if page.width < 600 else 412),
                ),
                
                # BLOQUE DERECHO: Se va abajo en móvil automáticamente
                ft.Column(
                    col={"sm": 12, "md": 4},
                    spacing=12,
                    controls=[
                        # Usamos otra fila responsive para las pequeñas
                        ft.ResponsiveRow(
                            spacing=12,
                            run_spacing=12,
                            controls=[
                                # En móvil: 2 fotos por fila (col=6). En PC: 1 por fila (col=12)
                                ft.Container(col={"sm": 6, "md": 12}, content=img(choice(room_info["data"]["category_images"]), h=200)),
                                ft.Container(col={"sm": 6, "md": 12}, content=img(choice(room_info["data"]["category_images"]), h=200)),
                            ]
                        )
                    ]
                ),
            ],
        )
    )

    tipo_habitacion = ft.Text(
            value=room_type_name,
            color="black",
            size=32,
            weight="bold",
    )

    propiedades_text = ft.Text(
            value=f"Propiedades de la habitación", 
            color="black",
            size=32,
            weight="bold",
    )

    propiedades = ft.ResponsiveRow(
        spacing=10,
        run_spacing=10,
        controls=[
            ft.Container(
                col={"sm": 6, "md": 4}, # Esto es para el responsive
                content=ft.Row([
                    ft.Text(item, color="black")
                ]),
                padding=5,
            ) for item in data["content"]
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
                                imagenes_habitacion,
                                tipo_habitacion,
                                propiedades_text,
                                propiedades
                        ]
                    ),
                ]
            )
        ]
     )