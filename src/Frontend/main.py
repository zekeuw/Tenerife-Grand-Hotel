import flet as ft


def main(page: ft.Page):
    page.title = "Tenerife Grand Hotel"
    page.bgcolor = "white"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.MainAxisAlignment.START
    page.padding = 40

    nombre =  ft.Text(
        value="Tenerife\nGrand Hotel", 
        size=20 ,color="black", 
        weight="bold", 
        align=ft.Alignment.TOP_LEFT)
    reservas = ft.Text(
        value="Mis reservas", 
        color="black",size=18 ,
        align=ft.Alignment.TOP_LEFT)
    habitaciones = ft.Text(
        value="Habitaciones", 
        color="black", size=18 ,
        align=ft.Alignment.TOP_LEFT)

    login = ft.Button(
        content="Log in", 
        align=ft.Alignment.TOP_RIGHT,
        color="white",
        bgcolor="blue"
        )
    signup = ft.OutlinedButton(
        content="Sign up", 
        align=ft.Alignment.TOP_RIGHT,
        style=ft.ButtonStyle(
            side=ft.BorderSide(width=1, color=ft.Colors.BLUE),
            color="blue"
        )
    )

    icon_menu = ft.Image(
        src= "../../media/img/icon_menu.png",
        height=50,
        width=50,
        align=ft.Alignment.TOP_RIGHT
    )

    top_bar_container = ft.Container(
        ft.Row(controls=[
            ft.Row(
                controls=[
                    nombre,
                    reservas,
                    habitaciones
                ],
                spacing=50  
            ),
            ft.Row(controls=[
                signup,
                login,
                icon_menu
            ])
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
    )
    
    cover_img_container = ft.Container(
        border_radius=20,
        width=float("inf"),
        height=300,
        margin=ft.margin.only(bottom=50),
        image=ft.DecorationImage(
            src= "../../media/img/cover_photo.jpg",
            fit = "COVER",
        ),
    
        content=ft.Container(
            ft.Column(
                controls=[
                    ft.Text(
                        value="Bienvenido al paraiso",
                        size=40,
                        color="white",
                        weight="bold",
                        text_align="center"
                    ),
                    ft.Text(
                        value="Encuentra tu habitacion perfecta, hecha para ti",
                        size=15,
                        color="white",
                        weight="bold",
                        text_align="center"
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER, 
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True 
                
            ),
            bgcolor=ft.Colors.with_opacity(0.3, "black")
        )
    )

    
    hab = {
        "Luxury": {
            "LX_1": {
                "guests": 2,
                "bed": ["King"],
                "content": ["Wifi", "TV", "Vistas al Mar", "Cafetera Nespresso"],
                "price": 450,
                "description": "Lujo moderno sin complicaciones. Amplia cama King Size con sábanas de seda egipcia. Situada en la planta más alta, pero sin plaza de garaje asignada."
            },
            "LX_2": {
                "guests": 2,
                "bed": ["King"],
                "content": ["Wifi", "TV", "Domótica", "Baño de diseño"],
                "price": 420,
                "description": "Habitación inteligente controlada por voz. Ideal para parejas que buscan una experiencia tecnológica de alto standing."
            },
            "LX_3": {
                "guests": 2,
                "bed": ["King"],
                "content": ["Wifi", "TV", "Jacuzzi", "Minibar Premium"],
                "price": 440,
                "description": "Experiencia de relax total. Incluye un jacuzzi hidromasaje integrado en la habitación y un minibar con selección de licores premium incluidos."
            },
            "LX_4": {
                "guests": 2,
                "bed": ["Matrimonio"],
                "content": ["Wifi", "TV", "Terraza Privada", "Hamaca"],
                "price": 400,
                "description": "Lujo al aire libre. Disfruta de una terraza exclusiva de 20m2 con hamacas y zona chill-out. Ideal para ver el atardecer con total privacidad."
            },
            "LX_5": {
                "guests": 3,
                "bed": ["Matrimonio", "Sofa-cama"],
                "content": ["Wifi", "TV", "Balcón amplio"],
                "price": 380,
                "description": "Espacio de lujo con acabados en madera noble. Perfecta iluminación natural y servicio de habitaciones gourmet disponible."
            },
            "LX_6": {
                "guests": 2,
                "bed": ["King"],
                "content": ["Wifi", "TV 55'", "Vistas Panorámicas", "Ducha de lluvia"],
                "price": 410,
                "description": "Despierta con la mejor vista de la ciudad. Ducha efecto lluvia y amenities de alta gama. Sin garaje."
            },
            "LX_7": {
                "guests": 2,
                "bed": ["King"],
                "content": ["Wifi", "TV 60'", "Smart Home", "Cava de vinos"],
                "price": 460,
                "description": "Habitación tecnológica con pequeña selección de vinos premium incluida. Iluminación ajustable por app."
            },
            "LX_8": {
                "guests": 2,
                "bed": ["Matrimonio"],
                "content": ["Wifi", "TV", "Jacuzzi en terraza"],
                "price": 390,
                "description": "Romance puro. Jacuzzi situado en la terraza privada (planta alta). Privacidad visual total."
            }
        }
    }
    
    def CreateRoomCard(data):
        return ft.Container(
            width=300,
            height=320,
            padding= 5,
            margin=15,
            bgcolor="white",
            border_radius=15,
            shadow= ft.BoxShadow(
                blur_radius=5,
                color=ft.Colors.BLACK,
            ),
            ink=True,
            on_click=lambda e: print("pulsado sobre una tarjeta"),
            content= ft.Column(
                controls=[
                    ft.Image(
                        src="../../media/img/Rooms/Presidential/Presidential1.jpg",
                        width=float("inf"),
                        height=180,
                        border_radius=5,
                        fit= "COVER"
                    ),
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Text(value="Luxury", color="black", size=18),
                                ft.Text(value="Valoracion: 5", color="black"),
                                ft.Text(value=f"Desde {data["price"]}$/noche", color="black",weight="bold")
                            ]
                        )
                    )
                ]

            )
        )
    # When the backend is done, instead of range(10), it will be a list of json objects,
    # as same as the CreateRoomCard where the info will depend on that list
    
    for data in hab["Luxury"]: print(data,"\n\n")
    cards_list = [CreateRoomCard(hab["Luxury"][data]) for data in hab["Luxury"]]

    card_carrusel = ft.Row(
        expand=True,
        controls=cards_list,
        scroll = ft.ScrollMode.HIDDEN,
        spacing=10,
    )

    desplazamiento = 340 * 2
    async def scroll_izquierda(e):
        await card_carrusel.scroll_to(delta=(-desplazamiento), duration=500, curve="easeOut")

    async def scroll_derecha(e):
        await card_carrusel.scroll_to(delta=desplazamiento, duration=500, curve="easeOut")

    btn_lef= ft.Container(
        height=40,
        expand=True,
        content = ft.Image(
            src="../../media/icons/icon_left.png",
            fit="COVER"
        ),
        on_click= scroll_izquierda
    )

    btn_rig = ft.Container(
        height=40,
        expand=True,
        content = ft.Image(
            src="../../media/icons/icon_right.png",
            fit="COVER"
            ),
        on_click= scroll_derecha
    )

    best_valued_rooms_container = ft.Container(
        width=float("inf"),
        height=350,
        content=ft.Container(
            content= ft.Column(
                controls=[
                    ft.Container(
                        content=ft.Text("Habitaciones Mejor Valoradas", size=24, weight="bold", color="black"),
                        padding=ft.padding.only(left=80),
                        width=float("inf")
                    ),
                    ft.Row(
                        controls=[
                            ft.Container(
                                content=btn_lef,
                                align=ft.Alignment.CENTER_LEFT,
                                padding=10,
                                width=60,
                                ),
                            card_carrusel,
                            ft.Container(
                                content=btn_rig,
                                align=ft.Alignment.CENTER_LEFT,
                                padding=10,
                                width=60,
                                ),
                            ]
                        )
                    ] 
            )
        )
    )
    

    icon_menu.visible = False

    # Addings
    page.add(top_bar_container)
    page.add(cover_img_container)
    page.add(best_valued_rooms_container)



    def responsive(e):
        # Modo móvil
        if page.width < 800:
            print("estoy en movil")
            login.visible = False
            signup.visible = False
            habitaciones.visible = False
            reservas.visible = False
            icon_menu.visible = True
            page.padding = 20
        # Modo PC
        else:
            login.visible = True
            signup.visible = True
            habitaciones.visible = True
            reservas.visible = True
            icon_menu.visible = False
            page.padding = 40
        page.update()

    page.on_resize = responsive

ft.app(main)