import flet as ft

class RoomCarousel(ft.Container):
    def __init__(self, page: ft.Page, rooms_data):
        super().__init__()
        # Cambiamos el nombre a 'main_page' para evitar el conflicto
        self.main_page = page 
        self.rooms_data = rooms_data
        self.desplazamiento = 340 * 2
        
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
            align=ft.Alignment.CENTER,
            controls=[
                ft.Text(size=24, weight="bold", color="black", margin=ft.margin.only(left=40)),
                ft.Row(
                    controls=[
                        ft.IconButton(
                            icon=ft.Icons.ARROW_BACK_IOS_ROUNDED, 
                            on_click=self.scroll_left
                        ),
                        self.card_row,
                        ft.IconButton(
                            icon=ft.Icons.ARROW_FORWARD_IOS_ROUNDED, 
                            on_click=self.scroll_right
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            ]
        )

    def _build_cards(self):
        cards = []
        for room_type, rooms in self.rooms_data.items():
            for data in rooms:
                cards.append(
                    ft.Container(
                        width=300, height=320, padding=5, margin=15,
                        bgcolor="white", border_radius=15,
                        shadow=ft.BoxShadow(blur_radius=5, color=ft.Colors.BLACK),
                        on_click=lambda e, d=data, t=room_type: self.go_to_room(d, t),
                        content=ft.Column([
                            ft.Image(src=data.get("main_image"), height=180, width=300, fit="COVER", border_radius=5),
                            ft.Text(f"{data['category']}", color="black", size=16),
                            ft.Text(f"Valoraciones: {data['avg_rating']}", color="black"),
                            ft.Text(f"Desde {data['price']}$/noche", color="black", weight="bold")
                        ])
                    )
                )
        self.card_row.controls = cards

    def go_to_room(self, data, room_type):
        # Usamos self.main_page que definimos arriba
        setattr(self.main_page, "selected_room_data", {"data": data, "type": room_type})
        self.main_page.go("/singleRoom")

    async def scroll_left(self, e):
        await self.card_row.scroll_to(delta=-self.desplazamiento, duration=500, curve="easeOut")

    async def scroll_right(self, e):
        await self.card_row.scroll_to(delta=self.desplazamiento, duration=500, curve="easeOut")