import flet as ft
import datetime

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
    
    date_inputs = []

    def UpdateEntryDate(e):
        if entry_datepicker.value:
            fecha_entrada = entry_datepicker.value
            fecha_str = fecha_entrada.strftime("%d-%m-%Y")

            for text_field in date_inputs:
                text_field.value = fecha_str
                text_field.update()


    entry_datepicker = ft.DatePicker(
        on_change=UpdateEntryDate,
        cancel_text="Cancelar",
        confirm_text="Confirmar Entrada",
        help_text="Selecciona fecha de llegada",
        last_date= datetime.datetime(2026, 1, 1)
    )

    page.overlay.append(entry_datepicker)
    page.update()

    def open_entry_picker(e):
        entry_datepicker.open = True
        entry_datepicker.update()

    input_fecha = ft.TextField(
        border_radius=35,
        height=50,
        width=300,
        label="Fecha Entrada",
        label_style=ft.TextStyle(color="black", size=14),
        hint_text="DD-MM-AAAA",
        hint_style=ft.TextStyle(color="black"),
        read_only=True,
        text_style=ft.TextStyle(color="black", size=12),
        suffix_icon=ft.Icons.CALENDAR_MONTH,
        on_click=open_entry_picker,
        color="black"
    )

    date_inputs.append(input_fecha)
    
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
                    input_fecha,
                    phone,
                    passwd,
                    validate_passwd,
                    error,
                    ft.Button(content="Crear cuenta", color="white", bgcolor="blue", scale=1.5, margin=10, 
                              on_click=lambda e: buffer(user_name.value, name.value, last_names.value, phone.value, entry_datepicker.value, passwd.value))
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
                error.value = str(e)
                error.visible = True
        else:
            error.value = "Las contraseñas no coinciden"
            error.visible = True
            page.update()

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