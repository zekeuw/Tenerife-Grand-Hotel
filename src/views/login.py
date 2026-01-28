import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import flet as ft
from src.components.navigation_bar import NavigationBar

def main(page: ft.Page):
    page.title = "Tenerife Grand Hotel"
    page.bgcolor = "white"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.MainAxisAlignment.START
    page.padding = 20

    menu = NavigationBar(page)

    central_container = ft.Container(
        expand=True,
        content= ft.Container(
            content=ft.Column(
                [
                    ft.Text("Tu estancia en Tenerife empieza aquí", size=30, weight="bold", color="black"),
                    ft.Text("Login", size=30, color="black"),
                    ft.TextField(label="Username", color="#000000", hint_text="Introduzca su nombre de usuario..."),
                    ft.Text("Registro", size=30, color="black"),
                    ft.TextField(label="Contrasena", color="black", hint_text="Introduzca su contraseña...", password=True),
                    ft.Button(content="Iniciar sesión", color="white", bgcolor="blue", scale=1.5, margin=10)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            width=page.width,
            height=page.height*0.75,
            bgcolor="#d1d1d1",
            border_radius=10,
        ),
        alignment=ft.Alignment.CENTER, 
    )
   

    page.add(menu)
    page.add(central_container)

ft.app(main)