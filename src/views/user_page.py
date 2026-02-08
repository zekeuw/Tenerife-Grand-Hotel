import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import flet as ft
import datetime

from src.components.navigation_bar import NavigationBar

from src.Backend.UsersManagement import deleteUser, updateUser, logIn
from src.Backend.Utils.Validations import retrieveUser


def userPage(page: ft.Page):
    data = retrieveUser(page.username)
    menu = NavigationBar(page, state="user_page")

    def open_entry_picker(e):
        if not txtBirth.read_only:
            entry_datepicker.open = True
            entry_datepicker.update()

    #---------------------- TextFields ---------------------------
    txtUserName = ft.TextField(value=data["username"], read_only=True, border=ft.InputBorder.NONE, text_size=15, color="#555555", text_align=ft.TextAlign.CENTER)
    txtName = ft.TextField(value=data["name"], read_only=True, border=ft.InputBorder.NONE, text_size=15, color="#555555", text_align=ft.TextAlign.CENTER)
    txtSurname = ft.TextField(value=data["surname"], read_only=True, border=ft.InputBorder.NONE, text_size=15, color="#555555", text_align=ft.TextAlign.CENTER)
    txtPhone = ft.TextField(value=data["phone"], read_only=True, border=ft.InputBorder.NONE, text_size=15, color="#555555", text_align=ft.TextAlign.CENTER)

    txtBirth = ft.TextField(
        value=data["birth"],
        read_only=True,
        border=ft.InputBorder.NONE,
        text_size=15,
        color="#555555",
        on_click= open_entry_picker,
        text_align=ft.TextAlign.CENTER
    )


    def UpdateEntryDate(e):
        if entry_datepicker.value:
            fecha_entrada = entry_datepicker.value
            fecha_str = fecha_entrada.strftime("%Y-%m-%d")

            txtBirth.value = fecha_str

    entry_datepicker = ft.DatePicker(
        on_change=UpdateEntryDate,
        cancel_text="Cancelar",
        confirm_text="Confirmar Entrada",
        help_text="Selecciona fecha de llegada",
        last_date= datetime.datetime.today()
    )

    page.overlay.append(entry_datepicker)
    page.update()

    txtFieldNewPass = ft.TextField(
        label="Nueva Contraseña", 
        password=True, 
        can_reveal_password=True, 
        width=300, 
        bgcolor="white", 
        border_color="#0f62fe", 
        text_size=15, 
        visible=False, 
        text_align=ft.TextAlign.CENTER
    )

    errorLog = ft.Text(value="", color="#fe0f13", visible=False)
    
    chgeDesc = ft.Text(value="*Deje en blanco o sin tocar para no modificar los campos.", color="#888888")
    #creamos un contenedor que va a ser invisible por defecto, que luego se mostrara al darle click al boton de modificar datos
    txtNewPass = ft.Text("Nueva Contraseña:", size=15, weight="bold", color="#0f62fe", width=160, visible=False)


    # estos botones/rows van a estar apareciendo y desapareciendo continuamente, por eso los creamos en variables y los ponemos aqui
    btn_editar = ft.ElevatedButton(
                                    "Editar Perfil",
                                    bgcolor="#0f62fe",
                                    color="white",
                                    on_click=lambda e: toggle_edit(modo_edicion=True)
                                )
    
    btn_logout = ft.ElevatedButton(
                                    "Cerrar sesión",
                                    bgcolor="#fe0f0f",
                                    color="white",
                                    on_click=lambda e: logout()
                                )
    
    btn_eliminar = ft.ElevatedButton(
                                    "Borrar la cuenta",
                                    bgcolor="#000000",
                                    color="white",
                                    on_click=lambda e: manageDelete(page, page.username)
                                )
    
    row_botones_accion = ft.Column(
        visible=False,
        controls=[
            ft.Row([
                ft.OutlinedButton("Cancelar", style=ft.ButtonStyle(color="#fe0f13"), on_click=lambda e: toggle_edit(False)),
                ft.ElevatedButton("Guardar", bgcolor="#198754", color="white", on_click=lambda e: confirmChanges()),
            ], alignment=ft.MainAxisAlignment.CENTER),
            chgeDesc
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )


    txtFields = [txtUserName, txtName, txtSurname, txtPhone, txtBirth] #almacenamos todos los textfields para cambiarle los estilos al darle al boton de editar

    columna_izquierda = ft.Column(
        col={"sm": 12, "md": 6}, # 12 en móvil (pantalla completa), 6 en escritorio (mitad)
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Text("Nombre de Usuario:", size=15, weight="bold", color="#000000"),
            txtUserName,
            ft.Text("Nombre:", size=15, weight="bold", color="#000000"),
            txtName,
            ft.Text("Apellidos:", size=15, weight="bold", color="#000000"),
            txtSurname,
        ]
    )

    columna_derecha = ft.Column(
        col={"sm": 12, "md": 6},
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Text("Teléfono:", size=15, weight="bold", color="#000000"),
            txtPhone,
            ft.Text("Fecha de nacimiento:", size=15, weight="bold", color="#000000"),
            txtBirth,
            txtNewPass,
            txtFieldNewPass
        ]
    )
    
    central_container = ft.Container(
            padding=20,
            bgcolor="#d1d1d1",
            border_radius=10,
            content = ft.Column(
                scroll=ft.ScrollMode.AUTO,
                tight=True,
                controls=[
                    ft.Text("Datos Personales", size=24, weight="bold", color="#888888"),
                    ft.Text("Consulta y edita tus datos personales", color="#888888"),

                    ft.ResponsiveRow(
                        spacing=20,
                        controls=[columna_izquierda, columna_derecha]
                    ),
                    
                    ft.Divider(height=20, color="transparent"),
                    
                    ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls=[errorLog]),
                    ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls=[btn_editar, btn_logout]),
                    ft.Row(alignment=ft.MainAxisAlignment.CENTER, controls=[btn_eliminar]),
                    row_botones_accion # Botones guardar/cancelar
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=10
            )
    )
    
    def manageDelete(page: ft.Page, username):
        
        def confirm_delete(e):
            deleteUser(username)
            page.username = None
            confirm_dialog.open = False
            page.go("/")
            page.update()

        # Función para cerrar el diálogo si cancela
        def close_dlg(e):
            confirm_dialog.open = False
            page.update()

        confirm_dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Confirmar eliminación"),
            content=ft.Text(f"¿Estás seguro de que deseas eliminar la cuenta de {username}? Esta acción no se puede deshacer."),
            actions=[
                ft.TextButton("Confirmar", on_click=confirm_delete),
                ft.TextButton("Cancelar", on_click=close_dlg),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )

        page.overlay.append(confirm_dialog)
        confirm_dialog.open = True
        page.update()
    
    def logout():
        page.username = None
        page.go("/")

    def toggle_edit(modo_edicion):
        '''Esta funcion tiene dos modos (dados por la variable modo_edicion), en true el usuario esta modificando los datos, por lo que el textField de la contrasña esta visible y se ven los botones de cambio y confirmacion
           En el otro modo, el usuario solo esta viendo los datos, por lo que solo se ve el boton de editar y los campos que puede ver el usuario'''
        
        btn_editar.visible = not modo_edicion
        btn_logout.visible = not modo_edicion
        btn_eliminar.visible = not modo_edicion

        row_botones_accion.visible = modo_edicion
        

        txtFieldNewPass.visible = modo_edicion
        txtNewPass.visible = modo_edicion


        for field in txtFields:
            field.read_only = not modo_edicion
            
            if modo_edicion:
                field.border = ft.InputBorder.OUTLINE
                field.bgcolor = "white"
                field.border_color = "#0f62fe"
                field.border_radius = 5
            else:
                field.border = ft.InputBorder.NONE
                field.bgcolor = ft.Colors.TRANSPARENT 
                field.border_color = "transparent"
        
        if modo_edicion == False:
            txtUserName.value = data["username"]
            txtName.value = data["name"]
            txtSurname.value = data["surname"]
            txtPhone.value = data["phone"]
            txtBirth.value = data["birth"]
            txtNewPass.value = ""
            errorLog.value = ""
            errorLog.visible = modo_edicion

        page.update()

    def confirmChanges():
        '''Se llama al pulsar el boton de confirmar cambios, recorre los datos escritos por el usuario y los prepara para mandarlos a la funcion del backend'''
        '''Mas concretamente se preparan 6 variables que alternan entre input/None, none si no se ha cambiado el dato'''
        nonlocal data

        try: #la funcion update user tiene varias excepciones, si las levanta las controlaremos y mandaremos un mensaje al usuario

            #si el campo esta vacio o es igual que el que ya estaba antes la variable se iguala a None
            if txtUserName.value == "" or txtUserName.value == data["username"]:
                username = None
            else: username = txtUserName.value
            
            if txtName.value == "" or txtName.value == data["name"]:
                name = None
            else: name = txtName.value

            if txtSurname.value == "" or txtSurname.value == data["surname"]:
                surname = None
            else: surname = txtSurname.value

            if txtPhone.value == "" or  txtPhone.value == data["phone"]:
                phone = None
            else: phone = txtPhone.value

            if txtBirth.value == "" or txtBirth.value == data["birth"]:
                birth = None
            else: birth = txtBirth.value
            
            if txtFieldNewPass.value == "" or logIn(data["username"], txtFieldNewPass.value):
                password = None
            
            else: 
                password = txtFieldNewPass.value
                

            if username == None and name == None and surname == None and phone == None and birth == None and password == None:
                raise Exception("Debe modificar al menos un campo")
            
            updateUser(data["username"], username, password, name, surname, phone, birth)
            if username:
                data = retrieveUser(username)
            else:
                data = retrieveUser(data["username"])
            page.username = data["username"]
            toggle_edit(False)

            
        except Exception as e:
            errorLog.value = str(e)
            errorLog.visible = True
            page.update()
    
    def responsive(e):
        if not page.width: return
 
        if page.width > 850:
            central_container.width = 800
        else:
            central_container.width = page.width - 40 
        
        menu.resize(page.width)
        page.update()

    page.on_resize = responsive

    vista = ft.View(
        route="/user",
        bgcolor="white",
        padding=0,
        scroll=ft.ScrollMode.AUTO, # Permite scroll en toda la página
        controls=[
            menu,
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER, # Centra el contenido horizontalmente
                controls=[
                    ft.Column(
                        # Forzamos a que la columna principal no se estire innecesariamente
                        tight=True, 
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Divider(height=20, color="transparent"), # Espaciado superior
                            central_container,
                            ft.Divider(height=20, color="transparent"), # Espaciado inferior
                        ],
                    )
                ]
            )
        ]
    )

    if page.width:
        responsive(None)

    return vista