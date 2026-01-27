import flet as ft


def main(page: ft.Page):
    page.title = "Tenerife Grand Hotel"
    page.bgcolor = "white"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.MainAxisAlignment.START
    page.padding = 20

    nombre =  ft.Text(
        value="Tenerife\nGrand Hotel", 
        size=20 ,color="black", 
        weight="bold", 
        align=ft.Alignment.TOP_LEFT)

    login = ft.Button(
        content="Log in", 
        align=ft.Alignment.TOP_RIGHT,
        color="white",
        bgcolor="blue"
        )
    
    signup = ft.OutlinedButton(
        content="Sign up", 
        align=ft.Alignment.TOP_RIGHT,
        style=ft.ButtonStyle(
            side=ft.BorderSide(width=1, color=ft.Colors.BLUE),
            color="blue"
        )
    )

    icon_menu = ft.Image(
        src= "/icons/icon_menu.png",
        height=50,
        width=50,
        align=ft.Alignment.TOP_RIGHT
    )

    top_bar_container = ft.Container(
        ft.Row(controls=[
            ft.Row(
                controls=[
                    nombre,
                ],
                spacing=50  
            ),
            ft.Row(controls=[
                signup,
                login
            ])
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
    )

    central_container = ft.Container(
        content=ft.Column(
            [
                ft.Text("Bienvenido al Lujo", size=30, weight="bold", color="black"),
                ft.Text("Tu estancia en Tenerife empieza aquí", color="grey")
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        alignment=ft.Alignment(0, 0), 
        expand=True, 
        bgcolor="#f5f5f5",
        border_radius=10,
    )

    def responsive(e):
        # Modo móvil
        if page.width < 400:
            print("estoy en movil")
            login.visible = False
            signup.visible = False
            icon_menu.visible = True
            page.padding = 20
        # Modo PC
        else:
            login.visible = True
            signup.visible = True
            page.padding = 20
        page.update()

    page.on_resize = responsive

    page.add(top_bar_container)
    page.add(central_container)

ft.app(main)