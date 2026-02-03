import flet as ft
from src.Backend.UsersManagement import createUser
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
                        
    phone = ft.TextField(
                        label="Teléfono", 
                        color="#000000",
                        hint_text="Introduzca su número de teléfono...", 
                        label_style=ft.TextStyle(color=ft.Colors.BLACK), 
                        hint_style=ft.TextStyle(color=ft.Colors.BLACK),
                        focused_border_color="black",
                        margin=15
                        )
    
    birth = ft.TextField(
                        label="Nacimiento",
                        color="black",
                        hint_text="Introduzca su fecha de nacimiento...", 
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
    
    error = ft.Text("", visible=False, color="red")


    central_container = ft.Container(
        expand=True,
        content= ft.Container(
            content=ft.Column(
                [
                    ft.Text("Registro", size=30, weight="bold", color="black"),
                    user_name,
                    name,
                    last_names,
                    birth,
                    phone,
                    passwd,
                    validate_passwd,
                    error,
                    ft.Button(content="Crear cuenta", color="white", bgcolor="blue", scale=1.5, margin=10, 
                              on_click=lambda e: buffer(user_name.value, name.value, last_names.value, phone.value, birth.value, passwd.value))
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            width=page.width,
            padding=40,
            bgcolor="#d1d1d1",
            border_radius=10,
        ),
        alignment=ft.Alignment.CENTER, 
    )

    def buffer(user_name, name, last_names, phone, birth, passwd):
        if validatePassword():
            try:
                data = {"username": user_name, "password": passwd, "name": name, "surname": last_names, "phone": phone, "birth": birth}
                createUser(data)
                page.username = user_name
                page.go("/userPage")
            except Exception as e:
                print(e)
                error.value = str(e)
                error.visible = True
        else:
            error.value = "Las contraseñas no coinciden"
            error.visible = True

    def validatePassword():
        return validate_passwd.value == passwd.value and passwd.value

    def responsive(e):
        if not page.width: return
        menu.resize(page.width)

    page.on_resize = responsive
    if page.width:
        responsive(None)

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