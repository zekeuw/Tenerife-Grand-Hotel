import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import flet as ft
from src.components.navigation_bar import NavigationBar

def userPage(page: ft.Page):
    menu = NavigationBar(page, state="logged_in")

    # Crea la vista completa
    vista = ft.View(
        route="/user",
        bgcolor="white",
        controls=[
            ft.Column(
                expand=True,
                controls=[
                    menu,  # <-- tu navbar
                    ft.Text("Hola Mundo")  # contenido de la página
                ]
            )
        ]
    )

    return vista

