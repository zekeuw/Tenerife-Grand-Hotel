import flet as ft


def main(page: ft.Page):
    page.title = "Flet counter example"
    page.bgcolor = "white"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.MainAxisAlignment.START

    nombre =  ft.Text(value="NombreDelHotel", color="black", align=ft.Alignment.TOP_LEFT)
    reservas = ft.Text(value="Mis reservas", color="black", align=ft.Alignment.TOP_LEFT)
    habitaciones = ft.Text(value="Habitaciones", color="black", align=ft.Alignment.TOP_LEFT)

    login = ft.Button(content="Sign up", align=ft.Alignment.TOP_RIGHT)
    signup = ft.Button(content="Log in", align=ft.Alignment.TOP_RIGHT)

    hamburguesita = ft.Image(
        src= "./src/img/menu.png",
        height=50,
        width=50,
        align=ft.Alignment.TOP_RIGHT
    )

    hamburguesita.visible = False

    barra_superior = ft.Row(controls=[
            ft.Row(controls=[
                nombre,
                reservas,
                habitaciones
            ]),
            ft.Row(controls=[
                login,
                signup,
                hamburguesita
            ])
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    page.add(barra_superior)

    img = ft.Image(
        src= "./src/img/best-tenerife.jpg",
        width=1100,
        height=200,
        align=ft.Alignment.CENTER,
        fit="FILL"
    )

    page.add(img)

    page.add(ft.Text("Habitaciones mejor valoradas", color="black"))

    carousel = ft.Basic

    def responsive(e):
        # Modo móvil
        if page.width < 600:
            login.visible = False
            signup.visible = False
            habitaciones.visible = False
            reservas.visible = False
            hamburguesita.visible = True
        # Modo PC
        else:
            login.visible = True
            signup.visible = True
            habitaciones.visible = True
            reservas.visible = True
            hamburguesita.visible = False
        page.update()

    page.on_resize = responsive

ft.app(main)