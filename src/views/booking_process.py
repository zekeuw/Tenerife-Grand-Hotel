import flet as ft
from src.components.navigation_bar import NavigationBar

def BookProcess(page: ft.Page):
    if page.username:
         # Si hay usuario, mostramos menú de logueado
         print(f"Usuario detectado: {page.session}") # Debug
         menu = NavigationBar(page, state="logged_in")
    else:
         # Si no, menú normal
         menu = NavigationBar(page)
    
    user_data_container = ft.Container(
        border=ft.Border.all(width=1, color=ft.Colors.BLACK_38),
        border_radius=15,
        expand=True, 
        padding=ft.Padding.only(left=40, right=40, top=10, bottom=20), 
        content=ft.Column(
            scroll=ft.ScrollMode.AUTO,
            spacing=10, 
            controls=[
                ft.Text(value="Proceso de Reserva", size=24, weight="bold", color="black"),

                ft.Text(value="Paso 1: Tu habitación", size=18, weight="bold", color="black"),
                ft.Container(
                    width=page.width*0.4,
                    padding=10,
                    content=ft.Column([
                        ft.Text(value="Propiedades seleccionadas:", weight="bold", color="black"),
                        ft.Text(value="Wifi, TV, Piscina", color="black"),
                        ft.Row([ft.Icon(ft.Icons.BED, color="black"), ft.Text("2 Camas King", color="black")]),
                    ])
                ),

                ft.Text(value="Paso 2: Tus datos personales", size=18, weight="bold", color="black"),
                
                ft.TextField(label="Nombre y apellidos", hint_text="Ana Perez Perez", icon=ft.Icons.PERSON, color="black"),
                ft.TextField(label="Correo electrónico", hint_text="correo@dominio.com" , icon=ft.Icons.EMAIL, color="black"),
                ft.TextField(label="Número de teléfono", hint_text="+34 999 999 999", icon=ft.Icons.PHONE, color="black"),
                
                ft.Divider(height=20, color="transparent"),

                ft.Text(value="Paso 3: Datos de facturación", size=18, weight="bold", color="black"),
                ft.TextField(label="Nombre en la tarjeta", hint_text="Como aparece en la tarjeta", icon=ft.Icons.PERSON, color="black"),
                ft.TextField(label="Número de la tarjeta", hint_text="xxxx xxxxx xxxxx xxxxx", icon=ft.Icons.CREDIT_CARD, color="black"),
                
                ft.Row(

                    controls=[
                        ft.TextField(label="Caducidad", hint_text="MM/AA", width=170, icon=ft.Icons.CALENDAR_MONTH_OUTLINED, margin=ft.Margin.only(bottom=20), color="black"),
                        ft.TextField(label="CVC", hint_text="***", width=120, password=True, icon=ft.Icons.NUMBERS, max_length=3, color="black"),
                    ]
                ),

                ft.Text(value="Normas de la habitación  ", size=18, weight="bold", color="black"),
                ft.Row(
                    controls=[
                        ft.Text(value="Check in: 15:00 pm", size=15,  color="black"),
                        ft.Text(value="Check out: 11:00 am ", size=15, color="black"),
                    ]
                ),
                ft.Row(
                    controls=[
                        ft.Text(value="No mascotas", size=15,  color="black"),
                        ft.Text(value="No fumar", size=15, color="black"),
                        ft.Text(value="No fiestas", size=15, color="black"),
                    ]
                ),

            ]
        )
    )

    room_data_container = ft.Container(
        border=ft.Border.all(width=1, color=ft.Colors.BLACK_38),
        border_radius=15,
        expand=True, 
        padding=ft.Padding.only(left=40, right=40, top=10, bottom=20), 
        content=ft.Column(
            controls=[
                ft.Image(src="/media/img/Rooms/Apartments/Apartment1.jpg", fit="COVER", width=page.width*0.45, height=page.height*0.25, border_radius=15),
                ft.Text(value="Tipo habitacion", color="black", size=18, weight="bold"),
                ft.Text(value="Pequeña descripcion de la habitacion", color="black", size=14),
                ft.Row(
                    controls=[
                        ft.Text(value="Check in: ", color="black", size=14, weight="bold"),
                        ft.Text(value="Lunes, 16 de noviembre 2026", color="black", size=14)
                    ]
                ),
                ft.Row(
                    controls=[
                        ft.Text(value="Check out: ", color="black", size=14, weight="bold"),
                        ft.Text(value="Lunes, 16 de noviembre 2026", color="black", size=14)
                    ]
                ),
            
                ft.Text(value="Precios de la habitacion", color="black", size=18, weight="bold"),
                ft.Row(
                    controls=[
                        ft.Text(value="Precio por noche: ", color="black", size=15),
                        ft.Text(value="100€", color="black", size=17, weight="bold")
                    ]
                ),
                ft.Row(
                    controls=[
                        ft.Text(value="5 noches: ", color="black", size=15),
                        ft.Text(value="500€", color="black", size=17, weight="bold")
                    ]
                ),
                ft.Row(
                    controls=[
                        ft.Text(value="IVA 21%: ", color="black", size=15),
                        ft.Text(value=" 105€", color="black", size=17, weight="bold")
                    ]
                ),
                ft.Row(
                    controls=[
                        ft.Text(value="TOTAL: ", color="black", size=15),
                        ft.Text(value=" 605€", color="black", size=17, weight="bold")
                    ]
                ),
            ]
            
        )
    )
    data_container_mobile = ft.Column(
                        controls = [
                            user_data_container,
                            room_data_container
                        ]
                    )
    data_container_mobile.visible=False
    data_container = ft.Row(
                        spacing=300,
                        vertical_alignment=ft.CrossAxisAlignment.START,
                        controls = [
                            user_data_container,
                            room_data_container
                        ]
                    )

    def responsive(e):
        is_mobile = page.width < 800
        data_container_mobile.visible = True if is_mobile else False
        data_container.visible = False if is_mobile else True
        menu.resize(page.width)

    page.on_resize = responsive
    if page.width: responsive(None)

    return ft.View(
        route="/processBooking", 
        bgcolor="white",
        padding=0,
        controls=[
            ft.Column(
                expand=True,
                scroll=ft.ScrollMode.AUTO, 
                controls=[
                    menu,
                    data_container,
                    data_container_mobile
                ]
            )
        ]
    )