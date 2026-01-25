import flet as ft
from all_rooms import AllRoomsView

def main(page: ft.Page):
    VIEWS_WIDTH = page.width *0.8
    VIEWS_HEIGTH = 800

    photo_list = [
        ft.Image(src="../../media/img/photo_views/photo1.jpg", border_radius=15,width=VIEWS_WIDTH, height=VIEWS_HEIGTH, fit="COVER"),
        ft.Image(src="../../media/img/photo_views/photo2.jpg", border_radius=15,width=VIEWS_WIDTH, height=VIEWS_HEIGTH, fit="COVER"),
        ft.Image(src="../../media/img/photo_views/photo3.jpg", border_radius=15,width=VIEWS_WIDTH, height=VIEWS_HEIGTH, fit="COVER"),
        ft.Image(src="../../media/img/photo_views/photo4.jpg", border_radius=15,width=VIEWS_WIDTH, height=VIEWS_HEIGTH, fit="COVER"),
        ft.Image(src="../../media/img/photo_views/photo5.jpg", border_radius=15,width=VIEWS_WIDTH, height=VIEWS_HEIGTH, fit="COVER")
    ]
    page.title = "Tenerife Grand Hotel"
    page.bgcolor = "white"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.MainAxisAlignment.START
    page.scroll = ft.ScrollMode.AUTO
    page.padding = 0

    # TOP BAR
    nombre =  ft.Text(
        value="Tenerife\nGrand Hotel", 
        size=20 ,color="black", 
        weight="bold", 
        align=ft.Alignment.TOP_LEFT)
    reservas = ft.Text(
        value="Mis reservas", 
        color="black",size=18 ,
        align=ft.Alignment.TOP_LEFT)
    habitaciones = ft.TextButton(
        content="Habitaciones",
        style=ft.ButtonStyle(
            color="black",  # Texto negro
            text_style=ft.TextStyle(size=18), # Tamaño 18
            overlay_color="transparent" # Opcional: quita el efecto gris al pasar el mouse si no lo quieres
        ),
        on_click=lambda _: page.push_route("/all_rooms")
    )

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
    
    top_var_container_mobile = ft.Container(
        width=float("inf"),
        height=float("inf"),
        bgcolor="white",
        visible=False,
        content=ft.Column(
            controls=[
                ft.TextButton("Inicio"),
                ft.TextButton("Mis Reservas"),
                ft.TextButton("Habitaciones"),

                ft.ElevatedButton("Log in", bgcolor="blue", color="white", width=float("inf")),
                ft.OutlinedButton("Sign up", width=float("inf"))
            ]
        )
    )
    
    def openMobileMenu(e):
        top_var_container_mobile.visible = True
        page.update()

    icon_menu =ft.IconButton(
            icon = ft.Image(
                src= "../../media/icons/icon_menu.png",
                height=50,
                width=50,    
                ),   
            on_click = openMobileMenu
    )

    top_bar_container = ft.Container(
        padding=30,
        content=
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
    

    # COVER
    cover_text_title = ft.Text(
                        value="Bienvenido al paraiso",
                        size=40,
                        color="white",
                        weight="bold",
                        text_align="center"
                    )
    cover_text_description = ft.Text(
                        value="Encuentra tu habitacion perfecta, hecha para ti",
                        size=15,
                        color="white",
                        weight="bold",
                        text_align="center"
                    )
    cover_img_container = ft.Container(
        margin=ft.margin.only(left=20, right=20, bottom=50),
        border_radius=20,
        width=float("inf"),
        height=300,
        image=ft.DecorationImage(
            src= "../../media/img/cover_photo.jpg",
            fit = "COVER",
        ),
    
        content=ft.Container(
            ft.Column(
                controls=[
                    cover_text_title,
                    cover_text_description
                ],
                alignment=ft.MainAxisAlignment.CENTER, 
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True 
                
            ),
            bgcolor=ft.Colors.with_opacity(0.3, "black")
        )
    )

    # BEST ROOMS
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
    
    cards_list = [CreateRoomCard(hab["Luxury"][data]) for data in hab["Luxury"]]

    card_carrusel = ft.Row(
        expand=True,
        controls=cards_list,
        scroll = ft.ScrollMode.HIDDEN,
        spacing=10,
    )

    desplazamiento = 340 * 2
    async def leftCardScroll(e):
        await card_carrusel.scroll_to(delta=(-desplazamiento), duration=500, curve="easeOut")

    async def rigthCardScroll(e):
        await card_carrusel.scroll_to(delta=desplazamiento, duration=500, curve="easeOut")

    btn_lef= ft.Container(
        height=40,
        expand=True,
        content = ft.Image(
            src="../../media/icons/icon_left.png",
            fit="COVER"
        ),
        on_click= leftCardScroll
    )

    btn_rig = ft.Container(
        height=40,
        expand=True,
        content = ft.Image(
            src="../../media/icons/icon_right.png",
            fit="COVER"
            ),
        on_click= rigthCardScroll
    )

    best_valued_rooms_container = ft.Container(
        margin=ft.margin.only(right=30, left=30),
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
                                margin=ft.margin.only(right=10)
                                ),
                            card_carrusel,
                            ft.Container(
                                content=btn_rig,
                                align=ft.Alignment.CENTER_LEFT,
                                padding=10,
                                width=60,
                                margin=ft.margin.only(left=10)
                                ),
                            ]
                        )
                    ] 
            )
        )
    )

    
    photo_carrusel = ft.Row(
        expand=True,
        controls=photo_list,
        scroll = ft.ScrollMode.HIDDEN,
        
        spacing=0,
    )
    
    async def leftPhotoScroll(e):
        await photo_carrusel.scroll_to(delta=-VIEWS_WIDTH, duration=600, curve="easeOut")

    async def RigthPhotoScroll(e):
        await photo_carrusel.scroll_to(delta=VIEWS_WIDTH, duration=600, curve="easeOut")

    btn_photo_lef= ft.Container(
        height=40,
        expand=True,
        content = ft.Image(
            src="../../media/icons/icon_left.png",
            fit="COVER"
        ),
        on_click= leftPhotoScroll
    )

    btn_photo_rig = ft.Container(
        height=40,
        expand=True,

        content = ft.Image(
            src="../../media/icons/icon_right.png",
            fit="COVER"
            ),
        on_click= RigthPhotoScroll
    )

    views_container = ft.Container(
        height=VIEWS_HEIGTH,
        width=float("inf"),
        alignment=ft.Alignment.CENTER,
        margin=ft.margin.only(top=80),
        
        content = ft.Container(
                    height=VIEWS_HEIGTH,
                    width=VIEWS_WIDTH,
                    alignment=ft.Alignment.CENTER,
                    content=ft.Column(
                        controls=[
                            ft.Text(
                                    value="Bienvenido a tu paraiso, Bienvenido a Tenerife",
                                    color=ft.Colors.BLACK,
                                    weight="bold",
                                    size=25
                                ),
                            ft.Container(
                                shadow= ft.BoxShadow(
                                    blur_radius=10,
                                    color=ft.Colors.BLACK,
                                ),
                                content=ft.Stack(
                                        alignment=ft.Alignment.CENTER,
                                        controls=[
                                            photo_carrusel,
                                            
                                            ft.Container(
                                                content=btn_photo_lef,
                                                left=10,  
                                                top=380,
                                                bgcolor=ft.Colors.WHITE_30,
                                                ),
                                            
                                            ft.Container(
                                                content=btn_photo_rig,
                                                right=10,     
                                                top=380,
                                                bgcolor=ft.Colors.WHITE_30
                                                ),
                                            ],
                                    )
                            ),
                            
                        ]
                    )
                        
                    
                )
    )

    footer_container = ft.Container(
        margin=ft.margin.only(top=100),
        padding=ft.padding.only(left=30, right=30, top=20, bottom=20),
        bgcolor=ft.Colors.BLACK_12,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Column(
                    controls=[
                        ft.Text(
                            value= "Tenerife Grand Hotel",
                            weight="bold",
                            color=ft.Colors.BLACK,
                            size=18
                        ),
                        ft.Text(
                            value= "El paraiso en la tierra solo para ti\ndesde 2006",
                            color=ft.Colors.BLACK,
                            size=18
                        ),
                    ],
                    alignment=ft.Alignment.CENTER_LEFT
                ),
                ft.Column(
                    controls=[
                        ft.Text(
                            value= "Ayuda",
                            weight="bold",
                            color=ft.Colors.BLACK,
                            size=18,
                            text_align=ft.TextAlign.END
                        ),
                        ft.Text(
                            value= "FAQ",
                            color=ft.Colors.BLACK,
                            size=18,
                            text_align=ft.TextAlign.END
                        ),
                        ft.Text(
                            value= "Contactanos",
                            color=ft.Colors.BLACK,
                            size=18,
                            text_align=ft.TextAlign.END
                        ),
                    ],


                )
            ]
        )
    )
    icon_menu.visible = False

    # Addings
    page.add(top_bar_container)
    page.add(cover_img_container)
    page.add(best_valued_rooms_container)
    page.add(views_container)
    page.add(footer_container)
    
    page.overlay.append(top_var_container_mobile)

    def responsive(e):
        is_mobile = page.width < 800
        
        signup.visible = False if is_mobile else True
        login.visible = False if is_mobile else True
        reservas.visible = False if is_mobile else True
        habitaciones.visible = False if is_mobile else True
        
        icon_menu.visible = True if is_mobile else False

        page.update()

    page.on_resize = responsive
    responsive(None)

ft.app(main)
