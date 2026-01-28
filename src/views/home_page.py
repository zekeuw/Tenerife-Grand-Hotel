import flet as ft
from src.Backend.RoomsManagement import TakeMostValuedRooms, TakeRandomPhotoByRoomType
from src.components.navigation_bar import NavigationBar
from src.views.page_404 import connectionErrorPage

ROOMS_TYPES = ["Presidential", "Luxury", "Privacy", "Apartment", "Regular"]

desplazamiento = 340 * 2
photo_moving = 0

def homePage(page: ft.Page):
    global photo_moving
    VIEWS_WIDTH = page.width *0.8
    VIEWS_HEIGTH = 800
    page.assets_dir = "assets"
    photo_moving = VIEWS_WIDTH
    menu = NavigationBar(page)
    photo_list = [
        ft.Image(src="media/img/photo_views/photo1.jpg", border_radius=15,width=VIEWS_WIDTH, height=VIEWS_HEIGTH, fit="COVER"),
        ft.Image(src="media/img/photo_views/photo2.jpg", border_radius=15,width=VIEWS_WIDTH, height=VIEWS_HEIGTH, fit="COVER"),
        ft.Image(src="media/img/photo_views/photo3.jpg", border_radius=15,width=VIEWS_WIDTH, height=VIEWS_HEIGTH, fit="COVER"),
        ft.Image(src="media/img/photo_views/photo4.jpg", border_radius=15,width=VIEWS_WIDTH, height=VIEWS_HEIGTH, fit="COVER"),
        ft.Image(src="media/img/photo_views/photo5.jpg", border_radius=15,width=VIEWS_WIDTH, height=VIEWS_HEIGTH, fit="COVER")
    ]    

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
            src= "media/img/cover_photo.jpg",
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
    
    def CreateRoomCard(data, room_type):
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
            on_click=lambda e: print(data["id"]),
            content= ft.Column(
                controls=[
                    ft.Image(
                        src=f"{TakeRandomPhotoByRoomType(room_type)}",
                        width=float("inf"),
                        height=180,
                        border_radius=5,
                        fit= "COVER"
                    ),
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Text(value=room_type, color="black", size=18),
                                ft.Text(value=f"Valoracion: {data["avg_rating"]}", color="black"),
                                ft.Text(value=f"Desde {data["price"]}$/noche", color="black",weight="bold")
                            ]
                        )
                    )
                ]

            )
        )

    best_rooms = TakeMostValuedRooms()
    print("BESTO ROOMS", best_rooms)
    if best_rooms == None: 
        page.go("/404")
        return
    
    cards_list = []
    
    for room_type in ROOMS_TYPES:
        if room_type in best_rooms:
            for room_data in best_rooms[room_type]:
                card = CreateRoomCard(room_data, room_type)
                cards_list.append(card)

    card_carrusel = ft.Row(
        expand=True,
        controls=cards_list,
        scroll = ft.ScrollMode.HIDDEN,
        spacing=10,
    )
   
    async def leftCardScroll(e):
        await card_carrusel.scroll_to(delta=(-desplazamiento), duration=500, curve="easeOut")
    async def rigthCardScroll(e):
        await card_carrusel.scroll_to(delta=desplazamiento, duration=500, curve="easeOut")

    btn_lef= ft.Container(
        height=40,
        expand=True,
        content = ft.Image(
            src="media/icons/icon_left.png",
            fit="COVER"
        ),
        on_click= leftCardScroll,
        margin=ft.Margin.only(left=60)
    )
    btn_rig = ft.Container(
        height=40,
        expand=True,
        content = ft.Image(
            src="./media/icons/icon_right.png",
            fit="COVER"
            ),
        on_click= rigthCardScroll,
        margin=ft.Margin.only(right=60)
    )
    best_valued_rooms_text_container = ft.Container(
                                        content=ft.Text("Habitaciones Mejor Valoradas", size=24, weight="bold", color="black"),
                                        padding=ft.padding.only(left=80),
                                        width=float("inf")
                                    )
    best_valued_rooms_container = ft.Container(
        margin=ft.margin.only(right=30, left=30),
        width=float("inf"),
        height=350,
        content=ft.Container(
            content= ft.Column(
                controls=[
                    best_valued_rooms_text_container,
                    ft.Row(
                        controls=[
                            ft.Container(content=btn_lef, align=ft.Alignment.CENTER_LEFT,),
                            card_carrusel,
                            ft.Container( content=btn_rig, align=ft.Alignment.CENTER_LEFT, ),
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
        await photo_carrusel.scroll_to(delta=-photo_moving, duration=600, curve="easeOut")

    async def RigthPhotoScroll(e):
        await photo_carrusel.scroll_to(delta=photo_moving, duration=600, curve="easeOut")

    btn_photo_lef= ft.Container(
        height=40,
        expand=True,
        content = ft.Image(
            src="media/icons/icon_left.png",
            fit="COVER"
        ),
        on_click= leftPhotoScroll
    )
    btn_photo_rig = ft.Container(
        height=40,
        expand=True,

        content = ft.Image(
            src="media/icons/icon_right.png",
            fit="COVER"
            ),
        on_click= RigthPhotoScroll
    )
    views_text_container = ft.Text(
                                value="Bienvenido a tu paraiso, Bienvenido a Tenerife",
                                color=ft.Colors.BLACK,
                                width=float("inf"),
                                weight="bold",
                                size=25,
                                margin=ft.margin.only(bottom=40),
                            )
    views_btn_lef_container = ft.Container(
                                    content=btn_photo_lef,
                                    left=10,  
                                    top=380,
                                    bgcolor=ft.Colors.WHITE_30,
                                    )
    views_btn_rig_container = ft.Container(
                                    content=btn_photo_rig,
                                    right=10,     
                                    top=380,
                                    bgcolor=ft.Colors.WHITE_30
                                    )
    views_container = ft.Container(
        height=VIEWS_HEIGTH,
        width=float("inf"),
        alignment=ft.Alignment.CENTER,
        margin=ft.margin.only(top=80),
        
        content = ft.Container(            
                    width=VIEWS_WIDTH,
                    alignment=ft.Alignment.CENTER,
                    content=ft.Column(
                        controls=[
                            views_text_container,
                            ft.Container(
                                shadow= ft.BoxShadow(
                                    blur_radius=10,
                                    color=ft.Colors.BLACK,
                                ),
                                content=ft.Stack(
                                        alignment=ft.Alignment.CENTER,
                                        controls=[
                                            photo_carrusel,
                                            views_btn_lef_container,
                                            views_btn_rig_container,
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

    def responsive(e):
        if not page.width: return
        is_mobile = page.width < 800
        global photo_moving
        
        menu.resize(page.width)

        best_valued_rooms_container.margin = 0 if is_mobile else ft.margin.only(right=30, left=30)
        best_valued_rooms_text_container.padding= 0 if is_mobile else ft.padding.only(left=80)
        best_valued_rooms_text_container.alignment = ft.Alignment.CENTER if is_mobile else None
        btn_lef.margin = ft.Margin.only(left=7) if is_mobile else ft.Margin.only(right=60)
        btn_lef.width= 20
        btn_rig.margin = ft.Margin.only(right=7) if is_mobile else ft.Margin.only(right=60)
        btn_rig.width= 20
        desplazamiento = 340 if is_mobile else 340*2

        photo_height = 500 if is_mobile else 800
        photo_width = page.width * (0.95 if is_mobile else 0.8) 

        for img in photo_list:
            img.width = photo_width
            img.height = photo_height
            
        views_container.height = photo_height + 100
        views_text_container.margin = ft.Margin.only(bottom=20)
        views_text_container.text_align = ft.TextAlign.CENTER
        views_btn_rig_container.top = photo_height * 0.5
        views_btn_lef_container.top = photo_height * 0.5
        photo_moving = photo_width
        footer_container.padding = ft.Padding.only(bottom=50) if is_mobile else ft.padding.only(left=30, right=30, top=20, bottom=20)

        try:
            page.update()
        except Exception:
            pass

    page.on_resize = responsive
    if page.width:
        responsive(None)
    
    

    return ft.View(
        route="/",
        bgcolor="white",
        padding=0,
        controls=[
            ft.Stack(
                expand=True,
                controls=[
                    ft.Column(
                        scroll=ft.ScrollMode.AUTO, 
                        expand=True,
                        controls=[
                                menu,
                                cover_img_container,
                                best_valued_rooms_container,
                                views_container,
                                footer_container
                            ]
                        ),
                    ]
                )
            ]
        )