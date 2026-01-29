import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import flet as ft
from src.components.navigation_bar import NavigationBar

# import src.Backend.UsersManagement

def userPage(page: ft.Page):
    menu = NavigationBar(page, state="user_page")

    menu_lateral = ft.Container(
        height= page.height,
        bgcolor="white",
        width= page.width * 0.20,
        padding= ft.padding.only(left=50, top=50),
        alignment=ft.Alignment.TOP_LEFT,
        content = ft.Column(
            spacing=50,
            
            controls=[ft.Container(
            ft.Image(
                src="/media/icons/icon_left.png",
                width= 25,
                height=25,
            ),
            on_click=lambda _: page.go("/")
            ),
            ft.Row(
                controls=[
                ft.Image(
                    src="/media/icons/user_logo.png",
                    height=20,
                    width=20

                ),
                ft.Text(
                value="Detalles Personales",
                color="#0f62fe",
                weight="bold",
                )
                ]
            ),
            ft.Container(expand=True),
            ft.Row(
                margin=ft.Margin.only(bottom=30),
                controls=[
                    ft.Image(
                        src="/media/icons/log_out.png",
                        height=20,
                        width=20

                    ),
                    ft.Text(
                    value="Cerrar sessión",
                    color="#fe0f13",
                    weight="bold",
                    ),
                    
                ]
            ),
            
        ]
        ),

        border= ft.border.only(
            right=ft.border.BorderSide(1, ft.Colors.GREY_300)
        )
    )
    
    vista = ft.View(
        route="/user",
        bgcolor="white",
        padding=0,
        controls=[
            ft.Column(
                expand=True,
                spacing=0,
                controls=[
                    menu,

                    ft.Row(
                        expand=True,
                        spacing=0,
                        controls=[
                            menu_lateral,
                        ]
                    )
                    
                ]
            )
        ]
    )
    def responsive(e):
        if not page.width: return
        is_mobile = page.width < 800
        global photo_moving
        
        menu.resize(page.width)

        
        desplazamiento = 340 if is_mobile else 340*2

        photo_height = 500 if is_mobile else 800
        photo_width = page.width * (0.95 if is_mobile else 0.8) 



        try:
            page.update()
        except Exception:
            pass

    page.on_resize = responsive
    if page.width:
        responsive(None)

    


    return vista

