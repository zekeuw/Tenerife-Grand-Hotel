import sys
import os
import datetime 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import flet as ft


from src.components.navigation_bar import NavigationBar
from src.components.carousel import RoomCarousel
import src.Backend.RoomsManagement as rm
from src.Backend.BookingManagement import DateAvailable
from src.Backend.ReviewsManagement import getAllReviewsFromRoom 

def singleRoom(page: ft.Page):

    room_info = getattr(page, "selected_room_data", None)
    
    if not room_info:
        page.go("/404")
        return ft.View(controls=[ft.Text("Error: No room selected")])
    
    data = room_info["data"]
    current_room_id = data.get("_id") or data.get("id")
    
    room_type_name = room_info["type"]
    foto_portada = room_info.get("foto_portada")

    if page.username:
         menu = NavigationBar(page, state="logged_in")
    else:
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
    
        if not DateAvailable(current_room_id, str_fecha_in, str_fecha_out):
            errorLog.visible = True
            errorLog.value = "Habitacion ya reservada durante las fechas introducidas"
            page.update()
        else:
            if page.username:
                booking_data = {
                    "fechaIni": input_fecha_entrada.value, 
                    "fechaFin": input_fecha_salida.value, 
                    "roomId": current_room_id,
                    "price": data["price"],
                    "type": data["category"],
                    "description": data["description"],
                    "bed": data["bed"],
                    "content": data["content"],
                    "main_img": data["main_image"]
                }
                setattr(page, "booking_data", booking_data)
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
                                ft.Container(col={"sm": 6, "md": 6}, content=img(rm.TakeRandomPhotoByRoomType(room_type_name), h=200)),
                                ft.Container(col={"sm": 6, "md": 6}, content=img(rm.TakeRandomPhotoByRoomType(room_type_name), h=200)),
                                ft.Container(col={"sm": 6, "md": 6}, content=img(rm.TakeRandomPhotoByRoomType(room_type_name), h=200)),
                                ft.Container(col={"sm": 6, "md": 6}, content=img(rm.TakeRandomPhotoByRoomType(room_type_name), h=200))
                            ]
                        )
                    ]
                ),
            ],
        )
    )

    propiedades = ft.Container(
        padding=ft.padding.only(bottom=20),
        content=ft.Row(
            alignment=ft.MainAxisAlignment.CENTER, 
            wrap=True,
            spacing=30,     
            run_spacing=10,
            controls=[
                ft.Container(
                    content=ft.Row(
                        controls=[ft.Text(item, color="black", size=14)],
                        spacing=5,
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                ) for item in data["content"]
            ],
        )
    )

    info_section = ft.Container(
        alignment=ft.Alignment.CENTER,
        padding=ft.padding.symmetric(horizontal=20, vertical=40),
        content=ft.ResponsiveRow(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.START,
            run_spacing=50,
            controls=[
                ft.Container(
                    width=400,
                    content=ft.Column(
                        col={"sm": 12, "md": 6},
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=15,
                        controls=[
                            ft.Text("Propiedades de la habitación", size=28, weight="bold", text_align=ft.TextAlign.CENTER, color="black"),
                            propiedades
                        ]
                    )
                ),
                ft.Container(
                    width=400,
                    content=ft.Column(
                        col={"sm": 12, "md": 6},
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=15,
                        controls=[
                            ft.Text("Reserva tu estancia", size=28, weight="bold", text_align=ft.TextAlign.CENTER, color="black"),
                            ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                wrap=True,
                                spacing=10,
                                controls=[input_fecha_entrada, input_fecha_salida]
                            ),
                            errorLog,
                            ft.ElevatedButton("Confirmar Reserva", bgcolor="blue", color="white", on_click=confirmar_reserva)
                        ]
                    )
                )
            ]
        )
    )

    best_rooms = rm.TakeMostValuedRooms()
    mi_carrusel = RoomCarousel(page=page, rooms_data=best_rooms)

    try:
        reviews_list_data = getAllReviewsFromRoom(current_room_id)
        if not reviews_list_data:
            reviews_list_data = []
    except Exception as e:
        print(f"Error cargando reseñas: {e}")
        reviews_list_data = []

    total_reviews = len(reviews_list_data)
    average_score = 0
    if total_reviews > 0:
        suma_notas = sum([r.get("mark", 0) for r in reviews_list_data])
        average_score = round(suma_notas / total_reviews, 1)

    score_display_text = f"{average_score} / 5" if total_reviews > 0 else "N/A"

    def ReviewItem(title, author, comment, score, date=""):
        if score >= 5:
            score_label = "Excelente"
            score_color = "green"
        elif score >= 3:
            score_label = "Bueno"
            score_color = "orange"
        else:
            score_label = "Malo"
            score_color = "red"
        
        if date:
            isdate = True
        else:
            isdate = False

        return ft.Column([
            ft.Row([
                ft.Column([
                    ft.Text(title, weight="bold", size=16, color="black"),
                    ft.Text(f"Por: {author}", size=12, color="grey"),
                    ft.Text(comment, size=14, color="black"),
                ], expand=True),
                
                ft.Column([
                    ft.Row([
                        ft.Text(score_label, color=score_color, weight="bold"),
                        ft.Container(
                            content=ft.Text(str(score), weight="bold", color="black"),
                            bgcolor=ft.Colors.with_opacity(0.1, score_color),
                            padding=10,
                            border_radius=10
                        )
                    ], alignment=ft.MainAxisAlignment.END),
                    ft.Text(f"Fecha:\n{date}", size=11, color="black", text_align=ft.TextAlign.RIGHT, visible=isdate)
                ], horizontal_alignment=ft.CrossAxisAlignment.END)
            ]),
            ft.Divider(height=40, thickness=1, color=ft.Colors.BLACK_12)
        ])

    reviews_controls_list = []
    
    if total_reviews == 0:
        reviews_controls_list.append(
            ft.Text("No hay reseñas todavía para esta habitación.", italic=True, color="grey")
        )
    else:
        for r in reviews_list_data[-2:]:
            reviews_controls_list.append(
                ReviewItem(
                    title=r.get("title", "Sin título"),
                    author=r.get("id_Client", "Usuario"), 
                    comment=r.get("description", ""),
                    score=r.get("mark", 0),
                    date=r.get("reviewDate", "")
                )
            )

    reviews_section = ft.Container(
        padding=40,
        content=ft.ResponsiveRow( 
        vertical_alignment=ft.CrossAxisAlignment.START,
        controls=[
            ft.Column([
                ft.Text("Reseñas", size=45, weight="bold", color="black"),
                ft.Text(score_display_text, size=40, weight="bold", color=ft.Colors.BLUE_800),
                ft.Text(f"Basado en {total_reviews} opiniones", color="grey")
            ], col={"sm": 12, "md": 4}),

            # Lista Derecha
            ft.Column(
                controls=reviews_controls_list,
                col={"sm": 12, "md": 8}
            )
        ])
    )

    def responsive(e):
        if not page.width: return
        menu.resize(page.width)

    page.on_resize = responsive
    if page.width: responsive(None)

    return ft.View(
        route="/singleRoom", 
        bgcolor="white",
        padding=20,
        controls=[
            ft.Column(
                scroll=ft.ScrollMode.AUTO, 
                expand=True,
                controls=[
                    menu,
                    imagenes_habitacion,
                    info_section,
                    mi_carrusel,
                    reviews_section
                ]
            ),
        ]
     )