import flet as ft
from datetime import datetime


from src.Backend.BookingManagement import UpdateBooking, GetBookingsOfUser, DeleteBookings
from src.Backend.Utils.Exceptions import NotFoundError
from src.components.navigation_bar import NavigationBar

#---------- Solo esta creado la tarjeta que se va a repetir en 

class BookingCard(ft.Container):
    def __init__(self, booking_data, page: ft.Page, on_update_callback, on_delete_callback):
        super().__init__()
        self.main_page = page 
        self.booking = booking_data
        self.on_update = on_update_callback
        self.on_delete = on_delete_callback
        

        self.room_id = booking_data.get("RoomId", "Unknown")
        self.current_ini = booking_data.get("IniDate", datetime.now().strftime("%Y-%m-%d"))
        self.current_fin = booking_data.get("FinDate", datetime.now().strftime("%Y-%m-%d"))
        booking_db_id = booking_data.get("_id", "---")


        self.bgcolor = "white"
        self.border_radius = 15
        self.padding = 20
        self.margin = ft.margin.only(bottom=20)
        self.shadow = ft.BoxShadow(
            spread_radius=1, blur_radius=5, 
            color=ft.Colors.with_opacity(0.2, "black"), offset=ft.Offset(0, 2)
        )


        try:
            dt_ini = datetime.strptime(self.current_ini, "%Y-%m-%d")
            dt_fin = datetime.strptime(self.current_fin, "%Y-%m-%d")
        except ValueError:
            dt_ini = datetime.now()
            dt_fin = datetime.now()

        self.dp_entrada = ft.DatePicker(first_date=datetime.now(), value=dt_ini, on_change=self.change_entry_date)
        self.dp_salida = ft.DatePicker(first_date=datetime.now(), value=dt_fin, on_change=self.change_exit_date)

        self.input_entrada = ft.TextField(
            value=self.current_ini, label="Entrada", width=130, height=40, 
            text_style=ft.TextStyle(size=12), read_only=True, 
            icon=ft.Icons.CALENDAR_MONTH, border_radius=8,
            on_click=self.open_entry_picker 
        )

        self.input_salida = ft.TextField(
            value=self.current_fin, label="Salida", width=130, height=40, 
            text_style=ft.TextStyle(size=12), read_only=True, 
            icon=ft.Icons.CALENDAR_TODAY, border_radius=8,
            on_click=self.open_exit_picker
        )

        self.content = ft.ResponsiveRow(
            columns=12,
            controls=[
                ft.Column(
                    col={"xs": 12, "md": 6},
                    controls=[
                        ft.Row([
                            ft.Container(
                                width=80, height=80, border_radius=10, bgcolor="#f0f0f0",
                                content=ft.Icon(ft.Icons.HOTEL, size=40, color="grey"),
                                alignment=ft.Alignment.CENTER
                            ),
                            ft.Column([
                                ft.Text(f"Habitación {self.room_id}", size=18, weight="bold"),
                                ft.Text(f"ID: {booking_db_id}", size=10, color="grey"),
                                ft.Text(f"{self.current_ini}  ➜  {self.current_fin}", size=12, weight="bold"),
                            ], spacing=2)
                        ])
                    ]
                ),
                ft.Column(
                    col={"xs": 12, "md": 6},
                    horizontal_alignment=ft.CrossAxisAlignment.END,
                    controls=[
                        ft.Row([self.input_entrada, self.input_salida], alignment=ft.MainAxisAlignment.END),
                        ft.Container(height=10),
                        ft.Row(
                            alignment=ft.MainAxisAlignment.END,
                            controls=[
                                ft.IconButton(
                                    icon=ft.Icons.DELETE_OUTLINE, 
                                    icon_color="red", tooltip="Cancelar Reserva",
                                    on_click=self.btn_delete_click
                                ),
                                ft.ElevatedButton(
                                    "Modificar Fechas", 
                                    bgcolor="blue", color="white",
                                    on_click=self.btn_update_click
                                )
                            ]
                        )
                    ]
                )
            ]
        )


    def open_entry_picker(e, self):
        self.input_entrada.open = True
        self.input_entrada.update()

    def open_exit_picker(e, self):
        self.input_salida.open = True
        self.input_salida.update()

    def did_mount(self):
        self.main_page.overlay.extend([self.dp_entrada, self.dp_salida])
        self.main_page.update()

    def change_entry_date(self, e):
        if self.dp_entrada.value:
            self.input_entrada.value = self.dp_entrada.value.strftime("%Y-%m-%d")
            self.input_entrada.update()

    def change_exit_date(self, e):
        if self.dp_salida.value:
            self.input_salida.value = self.dp_salida.value.strftime("%Y-%m-%d")
            self.input_salida.update()

    def btn_update_click(self, e):
        self.on_update(self.room_id, self.current_ini, self.input_entrada.value, self.input_salida.value)

    def btn_delete_click(self, e):
        self.on_delete(self.room_id, self.current_ini)
