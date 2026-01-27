import flet as ft


def main(page: ft.Page):
    VIEWS_WIDTH = page.width * 0.8
    VIEWS_HEIGTH = 800

    page.bgcolor = "white"

    nombre =  ft.Text(
        value="Tenerife\nGrand Hotel", 
        size=20 ,color="black", 
        weight="bold", 
        align=ft.Alignment.TOP_LEFT
    )

    login = ft.Button(
        content="Log in", 
        align=ft.Alignment.TOP_RIGHT,
        color="white",
        bgcolor="blue"
    )
    
    btnsignup = ft.OutlinedButton(
        content="Sign up", 
        align=ft.Alignment.TOP_RIGHT,
        style=ft.ButtonStyle(
            side=ft.BorderSide(width=1, color=ft.Colors.BLUE),
            color="blue"
        )
    )

    top_var_container_mobile = ft.Container(
        width=float("inf"),
        height=float("inf"),
        bgcolor="white",
        visible=False,
        content=ft.Column(
            controls=[
                ft.ElevatedButton("Log in", bgcolor="blue", color="white", width=float("inf")),
                ft.OutlinedButton("Sign up", width=float("inf"))
            ]
        )
    )

    def openMobileMenu(e):
        top_var_container_mobile.visible = True
        page.update()

    icon_menu =ft.IconButton(
            icon = ft.Image(
                src= "../../media/icons/icon_menu.png",
                height=50,
                width=50,    
                ),   
            on_click = openMobileMenu
    )

    top_bar_container = ft.Container(
        padding=30,
        content=
        ft.Row(controls=[
            ft.Row(
                controls=[
                    nombre
                ],
                spacing=50  
            ),
            ft.Row(controls=[
                btnsignup,
                login,
                icon_menu
            ])
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
    )

    cabecera = ft.Text(
        value="Registro de usuario", 
        size=20 ,color="black", 
        weight="bold", 
        align=ft.Alignment.CENTER
    )

    full_name = ft.TextField (
        hint_text="Introduzca su nombre completo...",
        color="black",
        align=ft.Alignment.TOP_LEFT
    )

    location = ft.TextField (
        hint_text="Introduzca su pais...",
        color="black",
        align=ft.Alignment.TOP_LEFT
    )

    signup = ft.Container(
        padding=30,
        bgcolor="#f6f6f6",
        width=100,
        content=
        ft.Row(controls=[
            ft.Column(
                controls=[
                    cabecera,
                    full_name,
                    location
                ],
                spacing=50  
            )
        ], alignment=ft.Alignment.CENTER
        )
    )

    # Addings
    page.add(top_bar_container)
    page.add(signup)
    page.overlay.append(top_var_container_mobile)

    def responsive(e):
        is_mobile = page.width < 800
        
        btnsignup.visible = False if is_mobile else True
        login.visible = False if is_mobile else True
        
        icon_menu.visible = True if is_mobile else False

        page.update()

    page.on_resize = responsive
    responsive(None)

ft.app(main)