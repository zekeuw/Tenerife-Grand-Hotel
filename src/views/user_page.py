import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import flet as ft
from src.components.navigation_bar import NavigationBar

from src.Backend.UsersManagement import deleteUser, updateUser, logIn
from src.Backend.Utils.Validations import retrieveUser


def userPage(page: ft.Page):
    data = retrieveUser(page.username)
    menu = NavigationBar(page, state="user_page")


    #---------------------- TextFields ---------------------------
    txtUserName = ft.TextField(value=data["username"], read_only=True, border=ft.InputBorder.NONE, text_size=15, color="#555555", margin=ft.Margin.only(left=40))
    txtName = ft.TextField(value=data["name"], read_only=True, border=ft.InputBorder.NONE, text_size=15, color="#555555", margin=ft.Margin.only(left=40))
    txtSurname = ft.TextField(value=data["surname"], read_only=True, border=ft.InputBorder.NONE, text_size=15, color="#555555", margin=ft.Margin.only(left=40))
    txtPhone = ft.TextField(value=data["phone"], read_only=True, border=ft.InputBorder.NONE, text_size=15, color="#555555", margin=ft.Margin.only(left=40))
    txtBirth = ft.TextField(value=data["birth"], read_only=True, border=ft.InputBorder.NONE, text_size=15, color="#555555", margin=ft.Margin.only(left=40))

    txtNewPass = ft.TextField(label="Nueva Contraseña", password=True, can_reveal_password=True, width=300, bgcolor="white", border_color="#0f62fe", text_size=15, margin=ft.Margin.only(left=40))

    errorLog = ft.Text(value="", color="#fe0f13", visible=False)
    
    chgeDesc = ft.Text(value="*Deje en blanco o sin tocar para no modificar los campos.", color="#888888")
    #creamos un contenedor que va a ser invisible por defecto, que luego se mostrara al darle click al boton de modificar datos
    rowPass = ft.Row(
        visible=False, 
        controls=[
            ft.Text("Nueva Contraseña:", size=15, weight="bold", color="#0f62fe", width=160),
            txtNewPass
        ]
    )

    # estos botones/rows van a estar apareciendo y desapareciendo continuamente, por eso los creamos en variables y los ponemos aqui
    btn_editar = ft.ElevatedButton(
                                    "Editar Perfil",
                                    bgcolor="#0f62fe",
                                    color="white",
                                    on_click=lambda e: toggle_edit(modo_edicion=True)
                                )
    
    row_botones_accion= ft.Row(
                                visible=False,
                                controls=[
                                    
                                    ft.OutlinedButton(
                                        "Cancelar",
                                        style=ft.ButtonStyle(color="#fe0f13"),
                                        on_click=lambda e: toggle_edit(modo_edicion=False)
                                    ),
                                    ft.ElevatedButton(
                                        "Guardar Cambios",
                                        bgcolor="#198754",
                                        color="white",
                                        on_click=lambda e: confirmChanges()
                                    ),
                                    chgeDesc
                                ]
                            )


    txtFields = [txtUserName, txtName, txtSurname, txtPhone, txtBirth] #almacenamos todos los textfields para cambiarle los estilos al darle al boton de editar

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
            ft.Container(
                margin=ft.Margin.only(bottom=30),
                on_click=lambda e: logout(),
                content=ft.Row(
                        controls=[
                            ft.Image(
                                src="/media/icons/log_out.png",
                                height=20,
                                width=20
                            ),
                            ft.Text(
                                value="Cerrar sesión",
                                color="#fe0f13",
                                weight="bold",
                            ),
                        ]
                    )
                ),
            ft.Container(
                margin=ft.Margin.only(bottom=30),
                on_click=lambda e: manageDelete(page.username),
                content=ft.Row(
                        controls=[
                            ft.Image(
                                src="/media/icons/log_out.png",
                                height=20,
                                width=20
                            ),
                            ft.Text(
                                value="Borrar cuenta",
                                color="#fe0f13",
                                weight="bold",
                            ),
                        ]
                    )
                )       
                ]
                ),

                border= ft.border.only(
                    right=ft.border.BorderSide(1, ft.Colors.GREY_300)
                    )
                )
    
    main_content = ft.Container(
        expand=True,
        padding=ft.padding.all(40),
        content=ft.Column(
            controls=[
                ft.Text("Datos Personales", size=24, weight="bold", color="#888888"),
                ft.Text("Consulta y edita tus datos personales", color="#888888"),
                ft.Column(
                    margin=ft.Margin.only(top=30),
                    spacing=30,
                    controls=[
                        ft.Row(
                            controls=[
                                ft.Text("Nombre de Usuario:", size=15, weight="bold", color="#000000", width=160),
                                txtUserName
                            ]
                        ),
                        ft.Row(
                            controls=[
                            ft.Text("Nombre:", size=15, weight="bold", color="#000000", width=160),
                            txtName
                            ]     
                        ),
                        ft.Row(
                            controls=[
                            ft.Text("Apellidos:", size=15, weight="bold", color="#000000", width=160),
                            txtSurname
                            ]
                        ),
                        ft.Row(
                            controls=[
                            ft.Text("Teléfono:", size=15, weight="bold", color="#000000", width=160),
                            txtPhone
                            ]
                        ),
                        ft.Row(
                            controls=[
                            ft.Text("Fecha de nacimiento:", size=15, weight="bold", color="#000000", width=160),
                            txtBirth
                            ]
                        ),
                        rowPass, # linea invisible de contraseña
                        errorLog,
                        ft.Container(
                            margin=ft.Margin.only(top=20),
                            content=ft.Column(
                                controls=[
                                    btn_editar,
                                    row_botones_accion
                                ]
                            )
                        )
                    ]
                )
            ]
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
                            main_content
                        ]
                    )
                    
                ]
            )
        ]
    )

    def manageDelete(username):
        '''Devuelve al usuario a la pagina principal y cambia el usuario logueado a none'''
        deleteUser(username)
        page.username = None
        page.go("/")

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
    
    def logout():
        page.username = None
        page.go("/")

    def toggle_edit(modo_edicion):
        '''Esta funcion tiene dos modos (dados por la variable modo_edicion), en true el usuario esta modificando los datos, por lo que el textField de la contrasña esta visible y se ven los botones de cambio y confirmacion
           En el otro modo, el usuario solo esta viendo los datos, por lo que solo se ve el boton de editar y los campos que puede ver el usuario'''
        
        btn_editar.visible = not modo_edicion
        row_botones_accion.visible = modo_edicion
        

        rowPass.visible = modo_edicion


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
            
            if txtNewPass.value == "" or logIn(data["username"], txtNewPass.value):
                password = None
            else: password = txtNewPass.value

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


    page.on_resize = responsive
    if page.width:
        responsive(None)
    


    


    return vista

    
    