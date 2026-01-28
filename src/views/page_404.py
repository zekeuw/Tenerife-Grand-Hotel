import flet as ft

def connectionErrorPage(page: ft.Page):
    print("Estoy llegando a 404")
    return ft.View(
        route="/404",
        bgcolor="white",
        padding=0,
        controls=[ 
            ft.Container(
                expand=True,
                alignment=ft.Alignment.CENTER, 
                content=ft.Column(
                    expand=True,
                    alignment=ft.MainAxisAlignment.CENTER, 
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Text(value="404", size=150, color="black", weight="bold"),
                        ft.Image(src="media/icons/error.png", height=100, width=100),
                        ft.Text("Página no encontrada", size=20, color="black") 
                    ],
                ),
            )
        ]
    )