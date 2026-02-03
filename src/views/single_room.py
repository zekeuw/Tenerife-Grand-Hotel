import sys
import os
import datetime 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import flet as ft
from src.components.navigation_bar import NavigationBar
import src.Backend.RoomsManagement as rm
from src.Backend.BookingManagement import DateAvailable
from src.views.carousel import RoomCarousel

def singleRoom(page: ft.Page):

    room_info = getattr(page, "selected_room_data", None)
    
    if not room_info:
        page.go("/404")
    
    data = room_info["data"]
    room_type_name = room_info["type"]
    foto_portada = room_info.get("foto_portada")

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

            #---------------------------------------- AQUI FALTA LA PAGINA A LA QUE IR -----------------------------------
            page.go("/pagina")
        

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

    def responsive(e):
        if not page.width: return
        menu.resize(page.width)

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
                                mi_carrusel
                        ]
                    ),
                ]
            )
        ]
     )