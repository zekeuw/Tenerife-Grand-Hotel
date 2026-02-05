import flet as ft
from datetime import datetime


from src.Backend.BookingManagement import UpdateBooking, GetBookingsOfUser, DeleteBookings
from src.Backend.Utils.Exceptions import NotFoundError
from src.components.navigation_bar import NavigationBar

def MyBookingsPage(page: ft.Page):
    page.title = "Tenerife Grand Hotel"
    page.theme_mode = ft.ThemeMode.LIGHT
    menu = NavigationBar(page, state="logged_in")
    if not page.username:
        page.go("/logIn")
    data = GetBookingsOfUser(page.username)
    
    no_data = ft.Text(
        value="No has hecho ninguna reserva", 
        visible=False, 
        color="red",
        size=16,
        margin=ft.Margin.only(left=40)
        
    )
    cards = []
    if not data:
        no_data.visible = True
        no_data.value = "No has hecho ninguna reserva"
    else:
        for elemento in data:
            tarjeta = BookingCard(page, elemento)
            cards.append(tarjeta)


    contenido = ft.Container(
        expand=True,
        bgcolor="white",
        content = ft.Column(
            controls= [
                menu, 
                no_data,
                *cards
            ]
        )
    )

    return contenido
    

def BookingCard(page: ft.Page, booking_data):
    room_id = booking_data["RoomId"]
    current_ini = booking_data["IniDate"]
    current_fin = booking_data["FinDate"]

    # --- 1. Definición de Funciones (Callbacks) ---
    
    def toggle_edit_mode(editable: bool, updated = False):
        """Cambia entre modo lectura y modo edición"""
        # Alternar visibilidad de botones
        btn_modificar.visible = not editable
        row_botones_confirmacion.visible = editable
        
        # Activar/Desactivar campos de texto
        # El truco es cambiar 'read_only' y el 'border'
        inputEntrada.read_only = not editable
        inputSalida.read_only = not editable
        errorLog.visible = False
        
        if editable:
            inputEntrada.border = ft.InputBorder.OUTLINE
            inputSalida.border = ft.InputBorder.OUTLINE
            inputEntrada.border_color = "blue"
            inputSalida.border_color = "blue"
        else:
            # Si cancelamos, restauramos los valores originales
            inputEntrada.value = current_ini
            inputSalida.value = current_fin
            inputEntrada.border = ft.InputBorder.NONE
            inputSalida.border = ft.InputBorder.NONE
            
        page.update()

    def change_entry_date(e):
        if dp_entrada.value:
            inputEntrada.value = dp_entrada.value.strftime("%Y-%m-%d")
            inputEntrada.update()
            page.update()

    def change_exit_date(e):
        if dp_salida.value:
            inputSalida.value = dp_salida.value.strftime("%Y-%m-%d")
            inputSalida.update()
            page.update()

    def open_entry_picker(e):
        # Solo abrimos el calendario si estamos en modo edición (no read_only)
        if not inputEntrada.read_only:
            dp_entrada.open = True
            dp_entrada.update()

    def open_exit_picker(e):
        if not inputSalida.read_only:
            dp_salida.open = True
            dp_salida.update()

    def confirm_update(e):

        try:
        # Intentamos la actualización
            UpdateBooking(room_id, booking_data["IniDate"], inputEntrada.value, inputSalida.value)
            print("hola")
            # Si tiene éxito, cerramos el modo edición
            toggle_edit_mode(False)
            page.update()

        except Exception as e:
            errorLog.value = str(e)
            errorLog.visible = True

    def delete(e):
        try:
            DeleteBookings(booking_data["RoomId"], booking_data["IniDate"])
            tarjeta.visible = False
            page.update()

        except Exception as e:
            errorLog.value = e
            errorLog.visible = True


    dp_entrada = ft.DatePicker(on_change=change_entry_date)
    dp_salida = ft.DatePicker(on_change=change_exit_date)
    page.overlay.extend([dp_entrada, dp_salida])

    inputEntrada = ft.TextField(
        value=current_ini, label="Entrada", width=175, height=50,
        read_only=True, border=ft.InputBorder.NONE, # Empieza modo lectura
        on_click=open_entry_picker, icon=ft.Icons.CALENDAR_MONTH
    )

    inputSalida = ft.TextField(
        value=current_fin, label="Salida", width=175, height=50,
        read_only=True, border=ft.InputBorder.NONE, # Empieza modo lectura
        on_click=open_exit_picker, icon=ft.Icons.CALENDAR_TODAY
    )

    # El botón inicial
    btn_modificar = ft.ElevatedButton(
        "Modificar Fechas", 
        bgcolor="blue", color="white",
        on_click=lambda _: toggle_edit_mode(True)
    )

    # La fila de botones que aparece al editar
    row_botones_confirmacion = ft.Row(
        visible=False, # Invisible al principio
        controls=[
            ft.TextButton("Cancelar", icon=ft.Icons.CLOSE, icon_color="red", 
                          on_click=lambda _: toggle_edit_mode(False)),
            ft.ElevatedButton("Confirmar", icon=ft.Icons.CHECK, bgcolor="green", color="white",
                             on_click=confirm_update),
        ]
    )

    # --- 3. Construcción del Layout ---
    errorLog = ft.Text(color="red", visible=False, value="", size=10)

    row = ft.ResponsiveRow(
        columns=12,
        controls=[
            ft.Column(
                col={"xs": 12, "md": 6},
                controls=[
                    ft.Row([
                        ft.Container(width=50, height=50, bgcolor="#f0f0f0", content=ft.Icon(ft.Icons.HOTEL)),
                        ft.Column([
                            ft.Text(f"Habitación {room_id}", weight="bold"),
                            ft.Text(f"ID: {room_id}", size=10),
                        ])
                    ])
                ]
            ),
            
            ft.Column(
                col={"xs": 12, "md": 6},
                horizontal_alignment=ft.CrossAxisAlignment.END,
                controls=[
                    ft.Row([inputEntrada, inputSalida], alignment=ft.MainAxisAlignment.END),
                    ft.Container(height=10),
                    errorLog,
                    ft.Row(
                        alignment=ft.MainAxisAlignment.END,
                        controls=[
                            ft.IconButton(icon=ft.Icons.DELETE_OUTLINE, icon_color="red", on_click=delete),
                            btn_modificar,           # Botón normal
                            row_botones_confirmacion # Botones de confirmación
                        ]
                    )
                ]
            )
        ]
    )
    tarjeta = ft.Container(content=row, padding=20, margin=ft.Margin.only(right=40, left=40), border_radius=15, bgcolor="white", shadow=ft.BoxShadow(blur_radius=5))
    return tarjeta
