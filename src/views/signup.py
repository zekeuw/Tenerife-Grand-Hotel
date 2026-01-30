import flet as ft
from src.components.navigation_bar import NavigationBar

def signUp(page: ft.Page):

    menu = NavigationBar(page)

    user_name = ft.TextField(
                        label="Nombre de usuario", 
                        color="#000000",
                        hint_text="Introduzca su nombre de usuario...", 
                        label_style=ft.TextStyle(color=ft.Colors.BLACK), 
                        hint_style=ft.TextStyle(color=ft.Colors.BLACK),
                        focused_border_color="black",
                        margin=15
                        )
    
    name = ft.TextField(
                        label="Nombre", 
                        color="#000000",
                        hint_text="Introduzca su nombre...", 
                        label_style=ft.TextStyle(color=ft.Colors.BLACK), 
                        hint_style=ft.TextStyle(color=ft.Colors.BLACK),
                        focused_border_color="black",
                        margin=15
                        )
    
    last_names = ft.TextField(
                        label="Apellidos", 
                        color="#000000",
                        hint_text="Introduzca su(s) apellido(s)...", 
                        label_style=ft.TextStyle(color=ft.Colors.BLACK), 
                        hint_style=ft.TextStyle(color=ft.Colors.BLACK),
                        focused_border_color="black",
                        margin=15
                        )
    
    passwd = ft.TextField(
                        label="Contraseña",
                        color="black",
                        hint_text="Introduzca su contraseña...", 
                        password=True,
                        label_style=ft.TextStyle(color=ft.Colors.BLACK), 
                        hint_style=ft.TextStyle(color=ft.Colors.BLACK),
                        focused_border_color="black",
                        margin=15
                        )
    
    validate_passwd = ft.TextField(
                        label="Repita la contraseña",
                        color="black",
                        hint_text="Introduzca de nuevo su contraseña...", 
                        password=True,
                        label_style=ft.TextStyle(color=ft.Colors.BLACK), 
                        hint_style=ft.TextStyle(color=ft.Colors.BLACK),
                        focused_border_color="black",
                        margin=15
                        )


    central_container = ft.Container(
        expand=True,
        content= ft.Container(
            content=ft.Column(
                [
                    ft.Text("🌴 Tu estancia en Tenerife empieza aquí 🌴", size=30, weight="bold", color="black"),
                    ft.Text("Registro", size=30, weight="bold", color="black"),
                    user_name,
                    name,
                    last_names,
                    passwd,
                    validate_passwd,
                    ft.Button(content="Crear cuenta", color="white", bgcolor="blue", scale=1.5, margin=10),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            width=page.width,
            height=page.height,
            bgcolor="#d1d1d1",
            border_radius=10,
        ),
        alignment=ft.Alignment.CENTER, 
    )

    

    return ft.View(
        route="/signUp",
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
                                central_container
                        ]
                    ),
                ]
            )
        ]
    )