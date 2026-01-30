import flet as ft
from src.components.navigation_bar import NavigationBar

def singleRoom(page: ft.Page):

    menu = NavigationBar(page)

    def add_image(dir_img, altura):
        return ft.Container(
        content=ft.Image(
            src=dir_img
        ),
        border_radius=15,
        height=altura,
    )

    imagenes_habitacion = ft.ResponsiveRow(
            controls=[
                ft.Column(
                    col={"sm": 12, "md": 6},
                    controls=[
                        add_image("media/img/Rooms/Apartments/Apartment1.jpg", 410)
                    ],
                ),
                ft.Column(
                    controls=[
                        ft.ResponsiveRow(
                            controls=[
                                ft.Column(col=6, controls=[add_image("media/img/Rooms/Apartments/Apartment1.jpg", 200)]),
                                ft.Column(col=6, controls=[add_image("media/img/Rooms/Apartments/Apartment1.jpg", 200)]),
                                ft.Column(col=6, controls=[add_image("media/img/Rooms/Apartments/Apartment1.jpg", 200)]),
                                ft.Column(col=6, controls=[add_image("media/img/Rooms/Apartments/Apartment1.jpg", 200)]),
                            ],
                            spacing=10,
                            run_spacing=10,
                        )
                    ]
                )
            ])

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