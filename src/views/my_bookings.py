import flet as ft
import datetime

from src.Backend.BookingManagement import UpdateBooking, GetBookingsOfUser, DeleteBookings
from src.Backend.Utils.Exceptions import NotFoundError
from src.components.navigation_bar import NavigationBar
from src.Backend.ReviewsManagement import createReview, returnReview

def MyBookingsPage(page: ft.Page):
    
    page.overlay.clear()
    page.title = "Tenerife Grand Hotel"
    page.theme_mode = ft.ThemeMode.LIGHT
    
    if not page.username:
        page.go("/logIn")
        return ft.Container()

    menu = NavigationBar(page, state="logged_in")
    data = GetBookingsOfUser(page.username)
    
    cards_column = ft.Column(spacing=20)
    
    no_data = ft.Text(
        value="No has hecho ninguna reserva", 
        visible=False, 
        color="red",
        size=16,
        text_align=ft.TextAlign.CENTER
    )

    if not data:
        no_data.visible = True
    else:
        for elemento in data:
            card = BookingCard(page, elemento, cards_column)
            cards_column.controls.append(card)

    content = ft.Container(
        expand=True,
        bgcolor="white",
        padding=20,
        content=ft.Column(
            scroll=ft.ScrollMode.ADAPTIVE,
            controls=[
                menu, 
                ft.Divider(height=20, color="transparent"),
                no_data,
                cards_column
            ]
        )
    )

    return ft.View(
        route="/MyBookings",
        bgcolor="white",
        controls=[
            content
        ]
    )


class StarRating(ft.Row):
    def __init__(self, initial_rating=0):
        super().__init__()
        self.value = initial_rating
        self.alignment = ft.MainAxisAlignment.CENTER
        self.spacing = 5
        
        self.star_buttons = []
        for i in range(1, 6):
            btn = ft.IconButton(
                icon=ft.Icons.STAR if i <= self.value else ft.Icons.STAR_BORDER,
                icon_color=ft.Colors.AMBER if i <= self.value else ft.Colors.GREY_400,
                icon_size=30,
                tooltip=f"{i} Estrellas",
                on_click=lambda e, score=i: self.set_rating(score)
            )
            self.star_buttons.append(btn)
        
        self.controls = self.star_buttons

    def set_rating(self, score):
        self.value = score
        for i, btn in enumerate(self.star_buttons):
            if (i + 1) <= score:
                btn.icon = ft.Icons.STAR
                btn.icon_color = ft.Colors.AMBER
            else:
                btn.icon = ft.Icons.STAR_BORDER
                btn.icon_color = ft.Colors.GREY_400
        self.update()

class BookingCard(ft.Container):
    def __init__(self, page_ref: ft.Page, booking_data, parent_column: ft.Column):
        super().__init__()

        self.main_page = page_ref 
        self.booking_data = booking_data
        self.parent_column = parent_column 
        
        self.room_id = booking_data.get("RoomId", "N/A")

        raw_ini = booking_data.get("IniDate")
        raw_fin = booking_data.get("FinDate")
        self.date_ini_obj = self.parse_date(raw_ini)
        self.date_fin_obj = self.parse_date(raw_fin)

        today = datetime.datetime.now().date()
        booking_end_date = self.date_fin_obj.date()

        self.is_editable = booking_end_date >= today

        self.padding = 20
        self.border_radius = 15
        self.bgcolor = "white"
        self.shadow = ft.BoxShadow(blur_radius=5, color=ft.Colors.with_opacity(0.2, "black"))
        self.margin = ft.Margin(left=20, right=20, top=5, bottom=5)

        self.error_log = ft.Text(value="", color="#fe0f13", visible=False, size=12)

        self.data = returnReview(self.main_page.username, self.room_id, self.booking_data["IniDate"])
        if self.data:
            self.is_review = True
        else:
            self.is_review = False

        self.entry_datepicker = ft.DatePicker(
            on_change=self.update_entry_date_ui,
            cancel_text="Cancelar",
            confirm_text="Confirmar",
            help_text="Fecha de llegada",
            value=self.date_ini_obj,
            first_date=datetime.datetime.now()
        )
        
        self.exit_datepicker = ft.DatePicker(
            on_change=self.update_exit_date_ui,
            cancel_text="Cancelar",
            confirm_text="Confirmar",
            help_text="Fecha de salida",
            value=self.date_fin_obj,
            first_date=datetime.datetime.now() + datetime.timedelta(days=1)
        )

        self.main_page.overlay.extend([self.entry_datepicker, self.exit_datepicker])

        self.input_entrada = ft.TextField(
            value=self.date_ini_obj.strftime("%d-%m-%Y") if self.date_ini_obj else "",
            label="Fecha Entrada",
            hint_text="DD-MM-AAAA",
            width=140,
            height=40,
            text_size=13,
            read_only=True, 
            disabled=not self.is_editable, 
            suffix_icon=ft.Icons.CALENDAR_MONTH,
            border=ft.InputBorder.NONE,
            on_click=lambda _: self.open_date_picker(self.entry_datepicker)
        )

        self.input_salida = ft.TextField(
            value=self.date_fin_obj.strftime("%d-%m-%Y") if self.date_fin_obj else "",
            label="Fecha Salida",
            hint_text="DD-MM-AAAA",
            width=140,
            height=40,
            text_size=13,
            read_only=True,
            disabled=not self.is_editable, 
            suffix_icon=ft.Icons.CALENDAR_TODAY,
            border=ft.InputBorder.NONE,
            on_click=lambda _: self.open_date_picker(self.exit_datepicker)
        )

        self.btn_modificar = ft.ElevatedButton(
            "Modificar", 
            bgcolor="blue", color="white",
            height=35,
            visible=self.is_editable, 
            on_click=self.toggle_edit_mode
        )

        self.btn_cancelar = ft.TextButton(
            "Cancelar", 
            icon=ft.Icons.CLOSE, icon_color="red",
            visible=False,
            on_click=self.cancel_edit
        )
        
        self.btn_guardar = ft.ElevatedButton(
            "Guardar", 
            icon=ft.Icons.CHECK, bgcolor="green", color="white",
            visible=False,
            height=35,
            on_click=self.confirm_update
        )

        self.btn_eliminar = ft.IconButton(
            icon=ft.Icons.DELETE_OUTLINE, 
            icon_color="red", 
            tooltip="Eliminar reserva",
            visible=self.is_editable, 
            on_click=self.delete_booking
        )

        self.btn_review = ft.ElevatedButton(
            "Dejar Reseña",
            icon=ft.Icons.RATE_REVIEW,
            bgcolor="orange", color="white",
            height=35,
            visible=(not self.is_editable and not self.is_review),
            on_click=self.open_review_modal
        )

        status_indicator = ft.Container()
        if not self.is_editable:
            status_indicator = ft.Container(
                content=ft.Text("Finalizada", color="grey", italic=True, size=12),
                padding=ft.padding.only(right=10)
            )

        info_column = ft.Column([
             ft.Row([
                ft.Container(
                    width=50, height=50, 
                    bgcolor="#f0f0f0", border_radius=10,
                    alignment=ft.Alignment.CENTER,
                    content=ft.Icon(ft.Icons.HOTEL, color="black54")
                ),
                ft.Column([
                    ft.Text(f"Habitación {self.room_id}", weight="bold", size=16),
                    ft.Text(f"Ref: {self.room_id}", size=12, color="grey"),
                ], spacing=2)
            ])
        ])

        controls_column = ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.END,
            controls=[
                ft.Row([self.input_entrada, self.input_salida], alignment=ft.MainAxisAlignment.END),
                self.error_log,
                ft.Row(
                    alignment=ft.MainAxisAlignment.END,
                    controls=[
                        status_indicator,
                        self.btn_review,   
                        self.btn_eliminar, 
                        self.btn_modificar,
                        self.btn_cancelar,
                        self.btn_guardar
                    ]
                )
            ]
        )

        self.content = ft.ResponsiveRow(
            controls=[
                ft.Column(col={"xs": 12, "md": 5}, controls=[info_column]),
                ft.Column(col={"xs": 12, "md": 7}, controls=[controls_column]),
            ]
        )

    def parse_date(self, date_val):
        if isinstance(date_val, str):
            try:
                return datetime.datetime.strptime(date_val, "%Y-%m-%d")
            except ValueError:
                try: 
                    return datetime.datetime.strptime(date_val, "%d-%m-%Y")
                except:
                    return datetime.datetime.now()
        elif isinstance(date_val, (datetime.date, datetime.datetime)):
            if isinstance(date_val, datetime.date) and not isinstance(date_val, datetime.datetime):
                 return datetime.datetime(date_val.year, date_val.month, date_val.day)
            return date_val
        return datetime.datetime.now()

    def open_date_picker(self, picker):
        if self.btn_guardar.visible and self.is_editable:
            picker.open = True      
            self.main_page.update() 

    def update_entry_date_ui(self, e):
        if self.entry_datepicker.value:
            date = self.entry_datepicker.value.replace(tzinfo=None)
            self.input_entrada.value = date.strftime("%d-%m-%Y")
            
            min_exit = date + datetime.timedelta(days=1)
            self.exit_datepicker.first_date = min_exit 
            
            current_exit_val = self.exit_datepicker.value
            if current_exit_val: current_exit_val = current_exit_val.replace(tzinfo=None)

            if current_exit_val and current_exit_val <= date:
                self.exit_datepicker.value = None
                self.input_salida.value = ""
                self.input_salida.error_text = "Selecciona fecha"
            
            self.input_entrada.update()
            self.input_salida.update()
            self.exit_datepicker.update()

    def update_exit_date_ui(self, e):
        if self.exit_datepicker.value:
            safe_date = self.exit_datepicker.value.replace(tzinfo=None)
            self.input_salida.value = safe_date.strftime("%d-%m-%Y")
            self.input_salida.error_text = None
            self.input_salida.update()

    def toggle_edit_mode(self, e):
        if not self.is_editable: return
        self.btn_modificar.visible = False
        self.btn_eliminar.visible = False
        self.btn_cancelar.visible = True
        self.btn_guardar.visible = True
        
        self.input_entrada.border = ft.InputBorder.OUTLINE
        self.input_entrada.border_color = "blue"
        self.input_salida.border = ft.InputBorder.OUTLINE
        self.input_salida.border_color = "blue"
        self.update()

    def cancel_edit(self, e):
        self.input_entrada.value = self.date_ini_obj.strftime("%d-%m-%Y")
        self.input_salida.value = self.date_fin_obj.strftime("%d-%m-%Y")
        self.input_salida.error_text = None
        self.error_log.visible = False
        
        self.btn_modificar.visible = True
        self.btn_eliminar.visible = True
        self.btn_cancelar.visible = False
        self.btn_guardar.visible = False
        
        self.input_entrada.border = ft.InputBorder.NONE
        self.input_salida.border = ft.InputBorder.NONE
        self.update()

    def confirm_update(self, e):
        if not self.input_entrada.value or not self.input_salida.value:
            self.error_log.value = "Selecciona ambas fechas"
            self.error_log.visible = True
            self.update()
            return

        try:
            val_ini = self.entry_datepicker.value
            if val_ini: val_ini = val_ini.replace(tzinfo=None)
            
            val_fin = self.exit_datepicker.value
            if val_fin: val_fin = val_fin.replace(tzinfo=None)

            new_ini = val_ini or datetime.datetime.strptime(self.input_entrada.value, "%d-%m-%Y")
            new_fin = val_fin or datetime.datetime.strptime(self.input_salida.value, "%d-%m-%Y")
            
            str_ini = new_ini.strftime("%Y-%m-%d")
            str_fin = new_fin.strftime("%Y-%m-%d")
            
            UpdateBooking(self.room_id, self.booking_data["IniDate"], str_ini, str_fin)
            
            self.date_ini_obj = new_ini
            self.date_fin_obj = new_fin
            self.booking_data["IniDate"] = str_ini 
            self.booking_data["FinDate"] = str_fin 
            
            self.main_page.snack_bar = ft.SnackBar(ft.Text("Reserva modificada correctamente"), bgcolor="green")
            self.main_page.snack_bar.open = True
            self.main_page.update()
            
            self.cancel_edit(None) 
            
        except Exception as ex:
            self.error_log.value = f"Error: {str(ex)}"
            self.error_log.visible = True
            self.update()

    def delete_booking(self, e):
        try:
            DeleteBookings(self.booking_data["RoomId"], self.booking_data["IniDate"])
            
            self.parent_column.controls.remove(self)
            self.parent_column.update()
            
            self.main_page.snack_bar = ft.SnackBar(ft.Text("Reserva eliminada"), bgcolor="red")
            self.main_page.snack_bar.open = True
            self.main_page.update()

        except Exception as ex:
            self.error_log.value = str(ex)
            self.error_log.visible = True
            self.update()

    def open_review_modal(self, e):

        star_rating_widget = StarRating()

        review_title = ft.TextField(
            label="Titulo",
            multiline=False,
            hint_text="Escribe un titulo para la reseña..."
        )

        review_input = ft.TextField(
            label="Comentarios (opcional)",
            multiline=True,
            max_lines=5,
            hint_text="Cuéntanos más sobre tu experiencia..."
        )
        error_text = ft.Text("", color="red", size=12, visible=False)

        def close_dlg(e):
            dialog.open = False
            self.main_page.update()

        def send_review_action(e):
            rating = star_rating_widget.value 
            
            if rating == 0:
                error_text.value = "Por favor, selecciona una puntuación."
                error_text.visible = True
                dialog.update() 
                return
            
            title = review_title.value

            if title == "":
                error_text.value = "El titulo es un campo obligatorio"
                self.btn_review.visible = False
                error_text.visible = True
                dialog.update()
                return
            
            today_date = datetime.datetime.now()
            date_text = today_date.strftime("%Y-%m-%d")
            
            try:
                createReview(title, self.room_id, review_input.value, rating, self.main_page.username, self.booking_data["IniDate"], date_text)
                close_dlg(None)
                
            except Exception as ex:
                print(f"Error reseña: {ex}")

        dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text(f"Valorar Habitación {self.room_id}", text_align=ft.TextAlign.CENTER),
            content=ft.Container(
                width=400, 
                content=ft.Column([
                    ft.Text("¿Qué nota le pones?", size=16),
                    ft.Divider(color="transparent", height=10),
                    star_rating_widget,
                    ft.Divider(color="transparent", height=5),
                    error_text,
                    ft.Divider(),
                    review_title,
                    ft.Divider(color="transparent", height=5),
                    review_input
                ], tight=True, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
            ),
            actions=[
                ft.TextButton("Cancelar", on_click=close_dlg),
                ft.ElevatedButton("Enviar", on_click=send_review_action, bgcolor="blue", color="white"),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )

        self.main_page.overlay.append(dialog)
        dialog.open = True
        self.main_page.update()