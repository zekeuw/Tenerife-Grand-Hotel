import flet as ft
from src.components.navigation_bar import NavigationBar
from src.Backend.BookingManagement import createBooking
from datetime import datetime

def BookProcess(page: ft.Page):
    if page.username:
         menu = NavigationBar(page, state="logged_in")
    else:
         menu = NavigationBar(page)
        
    data = getattr(page, "booking_data", None)

    print(page.username)

    # Extraemos los datos de la habitación
    ini_date = data["fechaIni"]
    fin_Date = data["fechaFin"]
    room_id = data["roomId"]
    price = data["price"]
    room_type = data["type"]
    description= data["description"]
    bed= data["bed"]
    content = data["content"]
    main_img = data["main_img"]

    tf_nombre = ft.TextField(label="Nombre y apellidos", hint_text="Ana Perez Perez", icon=ft.Icons.PERSON, color="black")
    tf_email = ft.TextField(label="Correo electrónico", hint_text="correo@dominio.com" , icon=ft.Icons.EMAIL, color="black")
    tf_telefono = ft.TextField(label="Número de teléfono", hint_text="+34 999 999 999", icon=ft.Icons.PHONE, color="black")
    
    tf_tarjeta_nombre = ft.TextField(label="Nombre en la tarjeta", hint_text="Como aparece en la tarjeta", icon=ft.Icons.PERSON, color="black")
    tf_tarjeta_num = ft.TextField(label="Número de la tarjeta", hint_text="xxxx xxxxx xxxxx xxxxx", icon=ft.Icons.CREDIT_CARD, color="black")
    tf_caducidad = ft.TextField(label="Caducidad", hint_text="MM/AA", width=170, icon=ft.Icons.CALENDAR_MONTH_OUTLINED, margin=ft.Margin.only(bottom=20), color="black")
    tf_cvc = ft.TextField(label="CVC", hint_text="***", width=120, password=True, icon=ft.Icons.NUMBERS, max_length=3, color="black")

    fields_to_validate = [tf_nombre, tf_email, tf_telefono, tf_tarjeta_nombre, tf_tarjeta_num, tf_caducidad, tf_cvc]

    user_data_container = ft.Container(
        border=ft.Border.all(width=1, color=ft.Colors.BLACK_38),
        border_radius=15,
        expand=True, 
        margin=ft.Margin.only(left=40),
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
                        ft.Text(value=content, color="black"),
                        ft.Row([ft.Icon(ft.Icons.BED, color="black"), ft.Text(bed, color="black")]),
                    ])
                ),
                ft.Text(value="Paso 2: Tus datos personales", size=18, weight="bold", color="black"),
                tf_nombre, tf_email, tf_telefono,
                ft.Divider(height=20, color="transparent"),
                ft.Text(value="Paso 3: Datos de facturación", size=18, weight="bold", color="black"),
                tf_tarjeta_nombre, tf_tarjeta_num,
                ft.Row(controls=[tf_caducidad, tf_cvc]),
                ft.Text(value="Normas de la habitación", size=18, weight="bold", color="black"),
                ft.Row(controls=[ft.Text("Check in: 15:00 pm", color="black"), ft.Text("Check out: 11:00 am", color="black")]),
            ]
        )
    )

    nigths = int(fin_Date.split("-")[0]) - int(ini_date.split("-")[0])
    
    room_data_container = ft.Container(
        border=ft.Border.all(width=1, color=ft.Colors.BLACK_38),
        border_radius=15,
        expand=True, 
        margin=ft.Margin.only(right=40),
        padding=ft.Padding.only(left=40, right=40, top=10, bottom=20), 
        content=ft.Column(
            controls=[
                ft.Image(src=main_img, fit="COVER", width=page.width*0.45, height=page.height*0.25, border_radius=15),
                ft.Text(value=room_type, color="black", size=18, weight="bold"),
                ft.Text(value=description, color="black", size=14),
                ft.Row(
                    controls=[
                        ft.Text(value="Check in: ", color="black", size=14, weight="bold"),
                        ft.Text(value=ini_date, color="black", size=14)
                    ]
                ),
                ft.Row(
                    controls=[
                        ft.Text(value="Check out: ", color="black", size=14, weight="bold"),
                        ft.Text(value=fin_Date, color="black", size=14)
                    ]
                ),
            
                ft.Text(value="Precios de la habitacion", color="black", size=18, weight="bold"),
                ft.Row(
                    controls=[
                        ft.Text(value="Precio por noche: ", color="black", size=15),
                        ft.Text(value=f"{price}€", color="black", size=17, weight="bold")
                    ]
                ),
                ft.Row(
                    controls=[
                        ft.Text(value=f"{nigths} noches: ", color="black", size=15),
                        ft.Text(value=f"{price*nigths}€", color="black", size=17, weight="bold")
                    ]
                ),
                ft.Row(
                    controls=[
                        ft.Text(value="IVA 21%: ", color="black", size=15),
                        ft.Text(value=f"{(price*nigths)*0.21}€", color="black", size=17, weight="bold")
                    ]
                ),
                ft.Row(
                    controls=[
                        ft.Text(value="TOTAL: ", color="black", size=15),
                        ft.Text(value=f"{(price*nigths)*1.21}€", color="black", size=17, weight="bold")
                    ]
                ),
            ]
            
        )
    )


    def confirmar_reserva(e):
        error_found = False
        
        for field in fields_to_validate:
            if not field.value or str(field.value).strip() == "":
                field.label = ft.Text(field.label, weight="bold", color="red") if isinstance(field.label, str) else field.label
                error_found = True
        if error_found: return
    

        try:
            ini_obj = datetime.strptime(ini_date, "%d-%m-%Y")
            new_ini = ini_obj.strftime("%Y-%m-%d")
            fin_obj = datetime.strptime(fin_Date, "%d-%m-%Y")
            new_fin = fin_obj.strftime("%Y-%m-%d")

            createBooking(room_id, new_ini, new_fin, page.username)
            page.go("/MyBookings")
        except Exception as ex:
            print(f"Error: {ex}")

    confirm = ft.ElevatedButton("Confirmar Reserva", bgcolor="blue", color="white", on_click=confirmar_reserva)

    data_container_mobile = ft.Column(visible=False, controls=[user_data_container, room_data_container])
    room_confirm = ft.Column(controls=[room_data_container, confirm])
    data_container = ft.Row(spacing=300, vertical_alignment=ft.CrossAxisAlignment.START, controls=[user_data_container, room_confirm])

    def responsive(e):
        is_mobile = page.width < 800
        data_container_mobile.visible = is_mobile
        data_container.visible = not is_mobile
        menu.resize(page.width)
        page.update()

    page.on_resize = responsive
    if page.width: responsive(None)

    return ft.View(
        route="/processBooking", 
        bgcolor="white",
        padding=0,
        controls=[ft.Column(expand=True, scroll=ft.ScrollMode.AUTO, controls=[menu, data_container, data_container_mobile])]
    )