import flet as ft
from src.Backend.UsersManagement import logIn as loggIn
from src.components.navigation_bar import NavigationBar

def logIn(page: ft.Page):

    menu = NavigationBar(page)

    usuario = ft.TextField(
                        label="Nombre de usuario", 
                        color="#000000",
                        hint_text="Introduzca su nombre de usuario...", 
                        label_style=ft.TextStyle(color=ft.Colors.BLACK), 
                        hint_style=ft.TextStyle(color=ft.Colors.BLACK),
                        focused_border_color="black",
                        margin=15
                        )
    
    contra = ft.TextField(
                        label="Contraseña",
                        color="black",
                        hint_text="Introduzca su contraseña...", 
                        password=True,
                        label_style=ft.TextStyle(color=ft.Colors.BLACK), 
                        hint_style=ft.TextStyle(color=ft.Colors.BLACK),
                        focused_border_color="black",
                        margin=15,
                        on_submit=lambda e: buffer(usuario.value, contra.value)
                        )
    
    error = ft.Text("Usuario o contraseña no válido", visible=False, color="red")

    central_container = ft.Container(
        expand=True,
        content= ft.Container(
            content=ft.Column(
                [
                    ft.Text("🌴 Tu estancia en Tenerife empieza aquí 🌴", size=30, weight="bold", color="black"),
                    usuario,
                    contra,
                    error,
                    ft.Button(content="Iniciar sesión", color="white", bgcolor="blue", scale=1.5, margin=10, on_click=lambda e: buffer(usuario.value, contra.value)),
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

    def buffer(usuario, contra):
        if loggIn(usuario, contra):
            page.username = usuario
            page.go("/")
        else:
            error.visible = True

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
                                central_container
                        ]
                    ),
                ]
            )
        ]
    )