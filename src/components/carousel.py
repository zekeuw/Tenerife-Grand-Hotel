import flet as ft

class RoomCarousel(ft.Container):
    def __init__(self, page: ft.Page, rooms_data):
        super().__init__()
        # Cambiamos el nombre a 'main_page' para evitar el conflicto
        self.main_page = page 
        self.rooms_data = rooms_data
        self.desplazamiento = 280   
        
        # Referencia al Row para el scroll
        self.card_row = ft.Row(
            scroll=ft.ScrollMode.HIDDEN,
            spacing=10,
            expand=True,
        )

        # Llenamos las tarjetas
        self._build_cards()

        # Estructura visual
        self.content = ft.Column(
            width=1800,
            alignment=ft.Alignment.CENTER,
            controls= [
            ft.Stack(
                controls=[
                    # Capa 1: El carrusel de tarjetas (centrado)
                    ft.Container(
                        content=self.card_row,
                        padding=ft.padding.symmetric(horizontal=40), # Espacio para que las flechas no tapen el texto
                    ),
                    # Capa 2: Flecha Izquierda (Pegada al borde)
                    ft.Container(
                        content=ft.IconButton(
                            icon=ft.Icons.ARROW_BACK_IOS_ROUNDED,
                            on_click=self.scroll_left,
                            icon_size=25,
                        ),
                        left=0,
                        top=120, # Ajusta esto para centrarla verticalmente respecto a tu imagen
                    ),
                    # Capa 3: Flecha Derecha (Pegada al borde)
                    ft.Container(
                        content=ft.IconButton(
                            icon=ft.Icons.ARROW_FORWARD_IOS_ROUNDED,
                            on_click=self.scroll_right,
                            icon_size=25,
                        ),
                        right=0,
                        top=120,
                    ),
                ],
                width=self.main_page.width, # Ocupa todo el ancho del móvil
                height=350, # Altura total del área del carrusel
            )]
        )

    def _build_cards(self):
        cards = []
        for room_type, rooms in self.rooms_data.items():
            for data in rooms:
                cards.append(
                    ft.Container(
                        width=240, height=320, padding=10, margin=15,
                        bgcolor="white", border_radius=15,
                        shadow=ft.BoxShadow(blur_radius=5, color=ft.Colors.BLACK),
                        ink=True,
                        on_click=lambda e, datos=data, tipo=room_type: self.go_to_room(datos, tipo),
                        content=ft.Column([
                            ft.Image(src=data.get("main_image"), height=180, width=240, fit="COVER", border_radius=5),
                            ft.Text(f"{data['category']}", color="black", size=16),
                            ft.Text(f"Valoraciones: {data['avg_rating']}", color="black"),
                            ft.Text(f"Desde {data['price']}$/noche", color="black", weight="bold")
                        ])
                    )
                )
        self.card_row.controls = cards

    def go_to_room(self, data, room_type):
        setattr(self.main_page, "selected_room_data", {"data": data, "type": room_type, "foto_portada": data.get("main_image")})
        
        if self.main_page.route == "/singleRoom":
            self.main_page.go("/reloading")
        else:
            self.main_page.go("/singleRoom")

    async def scroll_left(self, e):
        await self.card_row.scroll_to(delta=-self.desplazamiento, duration=500, curve="easeOut")

    async def scroll_right(self, e):
        await self.card_row.scroll_to(delta=self.desplazamiento, duration=500, curve="easeOut")