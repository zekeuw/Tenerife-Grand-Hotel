import sys
import os
import datetime 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import flet as ft
from src.components.navigation_bar import NavigationBar
import src.Backend.RoomsManagement as rm
from src.Backend.BookingManagement import DateAvailable
from src.components.carousel import RoomCarousel

def singleRoom(page: ft.Page):

    room_info = getattr(page, "selected_room_data", None)
    
    if not room_info:
        page.go("/404")
    
    data = room_info["data"]
    room_type_name = room_info["type"]
    foto_portada = room_info.get("foto_portada")

    if page.username:
         # Si hay usuario, mostramos menú de logueado
         print(f"Usuario detectado: {page.session}") # Debug
         menu = NavigationBar(page, state="logged_in")
    else:
         # Si no, menú normal
         menu = NavigationBar(page)

    def img(src, h=200):
        return ft.Container(
            border_radius=16,
            height=h,
            clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
            content=ft.Image(src=src, fit=ft.BoxFit.COVER),
        )
    
    today = datetime.datetime.now()
    
    entry_date_inputs = []
    exit_date_inputs = []

    def UpdateEntryDate(e):
        if entry_datepicker.value:
            fecha_entrada = entry_datepicker.value
            fecha_str = fecha_entrada.strftime("%d-%m-%Y")

            for text_field in entry_date_inputs:
                text_field.value = fecha_str
                text_field.update()

            min_exit_date = fecha_entrada + datetime.timedelta(days=1)
            exit_datepicker.first_date = min_exit_date
            
            if exit_datepicker.value and exit_datepicker.value <= fecha_entrada:
                exit_datepicker.value = None
                for text_field in exit_date_inputs:
                    text_field.value = ""
                    text_field.update()
            
            exit_datepicker.update()

    def UpdateExitDate(e):
        if exit_datepicker.value:
            fecha_str = exit_datepicker.value.strftime("%d-%m-%Y")
            for text_field in exit_date_inputs:
                text_field.value = fecha_str
                text_field.update()

    entry_datepicker = ft.DatePicker(
        on_change=UpdateEntryDate,
        cancel_text="Cancelar",
        confirm_text="Confirmar Entrada",
        help_text="Selecciona fecha de llegada",
        first_date=today 
    )
    
    exit_datepicker = ft.DatePicker(
        on_change=UpdateExitDate,
        cancel_text="Cancelar",
        confirm_text="Confirmar Salida",
        help_text="Selecciona fecha de salida",
        first_date=today + datetime.timedelta(days=1)
    )

    page.overlay.extend([entry_datepicker, exit_datepicker])

    errorLog = ft.Text(value="", color="#fe0f13", visible=False)

    def open_entry_picker(e):
        entry_datepicker.open = True
        entry_datepicker.update()

    def open_exit_picker(e):
        exit_datepicker.open = True
        exit_datepicker.update()

    input_fecha_entrada = ft.TextField(
        border_radius=35,
        height=30,
        label=ft.Text(value="Fecha Entrada", size=10),
        hint_text="DD-MM-AAAA",
        width=150,
        read_only=True,
        text_style=ft.TextStyle(color="black", size=12),
        suffix_icon=ft.Icons.CALENDAR_MONTH,
        on_click=open_entry_picker
    )

    input_fecha_salida = ft.TextField(
        border_radius=35,
        height=30,
        label=ft.Text(value="Fecha Salida", size=10),
        hint_text="DD-MM-AAAA",
        width=150,
        read_only=True, 
        text_style=ft.TextStyle(color="black", size=12), 
        suffix_icon=ft.Icons.CALENDAR_TODAY,
        on_click=open_exit_picker 
    )


    entry_date_inputs.append(input_fecha_entrada)
    exit_date_inputs.append(input_fecha_salida)

    def confirmar_reserva(e):
        
        fecha_in = entry_datepicker.value
        fecha_out = exit_datepicker.value

        
        if not fecha_in or not fecha_out:
            errorLog.visible = True
            errorLog.value = "Debe de elegir ambas fechas"
            page.update()
            return

        str_fecha_in = fecha_in.strftime("%Y-%m-%d")
        str_fecha_out = fecha_out.strftime("%Y-%m-%d")



        
        room_id = room_info["data"].get("_id") or room_info["data"].get("id")

        if not DateAvailable(room_id, str_fecha_in, str_fecha_out):
            errorLog.visible = True
            errorLog.value = "Habitacion ya reservada durante las fechas introducidas"
            page.update()
        else:

            if page.username:
                setattr(page, "booking_data", {"fechaIni": input_fecha_entrada.value, "fechaFin": input_fecha_salida.value, "roomId": room_id})
                page.go("/processBooking")
            else:
                page.go("/logIn")
        

    imagenes_habitacion = ft.Container(
        alignment=ft.Alignment.CENTER,
        padding=ft.padding.all(20),
        content=ft.ResponsiveRow(
            spacing=12,
            run_spacing=12,
            controls=[
                ft.Container(
                    col={"sm": 12, "md": 8},
                    content=img(foto_portada, h=300 if page.width < 600 else 412),
                ),
                ft.Column(
                    col={"sm": 12, "md": 4},
                    spacing=12,
                    controls=[
                        ft.ResponsiveRow(
                            spacing=12,
                            run_spacing=12,
                            controls=[
                                ft.Container(col={"sm": 6, "md": 6}, content=img(rm.TakeRandomPhotoByRoomType(room_info["type"]), h=200)),
                                ft.Container(col={"sm": 6, "md": 6}, content=img(rm.TakeRandomPhotoByRoomType(room_info["type"]), h=200)),
                                ft.Container(col={"sm": 6, "md": 6}, content=img(rm.TakeRandomPhotoByRoomType(room_info["type"]), h=200)),
                                ft.Container(col={"sm": 6, "md": 6}, content=img(rm.TakeRandomPhotoByRoomType(room_info["type"]), h=200))
                            ]
                        )
                    ]
                ),
            ],
        )
    )

    tipo_habitacion = ft.Text(
            value=room_type_name,
            color="black",
            size=32,
            weight="bold",
    )

    propiedades_text = ft.Text(
            value=f"Propiedades de la habitación", 
            color="black",
            size=32,
            weight="bold",
    )

    propiedades = ft.Container(
        width=600, 
        content=ft.ResponsiveRow(
            spacing=0,
            run_spacing=5,
            controls=[
                ft.Container(
                    col={"sm": 6, "md": 6}, 
                    content=ft.Row(
                        controls=[
                            ft.Text(item, color="black", size=14)
                        ],
                        spacing=5
                    ),
                    padding=ft.padding.only(top=2, bottom=2),
                ) for item in data["content"]
            ],
        )
    )
    
    seccion_info_mobile = ft.Column(
        spacing=50,
        controls=[
            propiedades,
            ft.Container(
                content=ft.Column([
                    ft.Text("Reserva tu estancia", weight="bold", size=16, color="black"),
                    
                    ft.Row([
                        input_fecha_entrada,
                        input_fecha_salida,
                    ], spacing=10),
                    errorLog,
                    ft.ElevatedButton("Confirmar Reserva", bgcolor="blue", color="white", on_click=lambda e: confirmar_reserva(e))
                ], spacing=15)
            )
        ]
    )
    seccion_info_mobile.visible = False

    seccion_info = ft.Row(
        vertical_alignment=ft.CrossAxisAlignment.START,
        spacing=50,
        controls=[
            propiedades,
            ft.Container(
                content=ft.Column([
                    ft.Text("Reserva tu estancia", weight="bold", size=16, color="black"),
                    
                    ft.Row([
                        input_fecha_entrada,
                        input_fecha_salida,
                    ], spacing=10),
                    errorLog,
                    ft.ElevatedButton("Confirmar Reserva", bgcolor="blue", color="white", on_click=lambda e: confirmar_reserva(e))
                ], spacing=15)
            )
        ]
    )

    best_rooms = rm.TakeMostValuedRooms()

    mi_carrusel = RoomCarousel(
        page=page, 
        rooms_data=best_rooms,
    )

    def ReviewItem(title, author, comment, score, score_label, score_color, pros=None, cons=None, date=""):
        # Lista de puntos positivos (Verde) o negativos (Rojo)
        points = []
        if pros:
            for p in pros:
                points.append(ft.Row([ft.Icon(ft.Icons.ADD, color="green", size=16), ft.Text(p, size=13)]))
        if cons:
            for c in cons:
                points.append(ft.Row([ft.Icon(ft.Icons.REMOVE, color="red", size=16), ft.Text(c, size=13)]))

        return ft.Column([
            ft.Row([
                ft.Column([
                    ft.Text(title, weight="bold", size=16),
                    ft.Text(author, size=12, color="grey"),
                    ft.Text(comment, size=14),
                    ft.Column(points, spacing=2),
                ], expand=True),
                ft.Column([
                    ft.Row([
                        ft.Text(score_label, color=score_color, weight="bold"),
                        ft.Container(
                            content=ft.Text(str(score), weight="bold"),
                            bgcolor=ft.Colors.with_opacity(0.1, score_color),
                            padding=10,
                            border_radius=10
                        )
                    ], alignment=ft.MainAxisAlignment.END),
                    ft.Text(f"Reviewed on\n{date}", size=11, color="grey", text_align=ft.TextAlign.RIGHT)
                ], horizontal_alignment=ft.CrossAxisAlignment.END)
            ]),
            ft.Divider(height=40, thickness=1, color=ft.Colors.BLACK_12)
        ])

    # SECCIÓN PRINCIPAL DE RESEÑAS
    reviews_section = ft.Container(
        padding=40,
        content=ft.Row(
            vertical_alignment=ft.CrossAxisAlignment.START,
            controls=[
                # LADO IZQUIERDO: Puntaje General
                ft.Column([
                    ft.Text("Reviews", size=45, weight="bold"),
                    ft.Text("9.6 / 10", size=40, weight="bold", color="blue"),
                ], width=300),

                # LADO DERECHO: Lista de comentarios
                ft.VerticalDivider(width=20, color="transparent"),
                ft.Column([
                    ReviewItem(
                        title="Excellent value for the price!",
                        author="Mark M.",
                        comment="We enjoyed our stay at this hotel. We will definitely come back!",
                        score=10,
                        score_label="Excellent",
                        score_color="green",
                        pros=["Great location!", "Service", "Bottle of champagne in the room!"],
                        date="20 September, 2022"
                    ),
                    ReviewItem(
                        title="Good hotel but noisy location",
                        author="Karena L.",
                        comment="Had room facing the street and it was super noisy. Unfortunately, we couldn't change room",
                        score=5.6,
                        score_label="Average",
                        score_color="orange",
                        cons=["Noise"],
                        date="10 September, 2022"
                    ),
                ], expand=True)
            ]
        )
    )

    def responsive(e):
        if not page.width: return
        is_mobile = page.width < 800
        menu.resize(page.width)
        seccion_info_mobile.visible = True if is_mobile else False
        seccion_info.visible = False if is_mobile else True

    page.on_resize = responsive
    if page.width:
        responsive(None)

    return ft.View(
        route="/singleRoom", 
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
                                imagenes_habitacion,
                                tipo_habitacion,
                                propiedades_text,
                                seccion_info,
                                mi_carrusel,
                                seccion_info_mobile,
                                reviews_section

                        ]
                    ),
                ]
            )
        ]
     )