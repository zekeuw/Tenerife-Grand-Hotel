import flet as ft

class NavigationBar(ft.Container):
    def __init__ (self, page:ft.Page):
        super().__init__()
        self.main_page = page
        self.padding = 30 

        self.hotel_name =  ft.TextButton(
            content=ft.Text("Tenerife\nGrand Hotel", weight="bold" ,size=20, color="black"),
            style=ft.ButtonStyle(
                color="black", 
                text_style=ft.TextStyle(size=18), 
                overlay_color="transparent"
            ),
            on_click=lambda _: page.go("/")
            )
        
        self.bookings = ft.Text(
            value="Mis reservas", 
            color="black",size=18 ,
            align=ft.Alignment.TOP_LEFT)
        
        self.rooms = ft.TextButton(
            content=ft.Text("Habitaciones", size=18, color="black"),
            style=ft.ButtonStyle(
                color="black", 
                text_style=ft.TextStyle(size=18), 
                overlay_color="transparent"
            ),
            on_click=lambda _: page.go("/allRooms")
        )

        self.login_button = ft.Button(
            content="Log in", 
            align=ft.Alignment.TOP_RIGHT,
            color="white",
            bgcolor="blue"
            )
        self.signup_button = ft.OutlinedButton(
            content="Sign up", 
            align=ft.Alignment.TOP_RIGHT,
            style=ft.ButtonStyle(
                side=ft.BorderSide(width=1, color=ft.Colors.BLUE),
                color="blue"
            )
        ) 
        

        self.top_var_container_mobile = ft.Stack(
            expand=True, 
            controls=[
                ft.Container(
                    bgcolor=ft.Colors.with_opacity(0.5, "black"),
                    expand=True,
                    on_click=self.closeMobileMenu
                ),
                ft.Container(
                    width=250,
                    bgcolor="white",
                    right=0,     
                    top=0,       
                    bottom=0,    
                    padding=20,
                    shadow=ft.BoxShadow(blur_radius=10, color=ft.Colors.BLACK),
                    content=ft.Column(
                        controls=[
                            ft.Row(
                                alignment=ft.MainAxisAlignment.END,
                                controls=[
                                    ft.IconButton(
                                        icon=ft.Image(src="/media/icons/close.png", width=20, height=20),
                                        on_click=self.closeMobileMenu 
                                    )
                                ]
                            ),
                            ft.Divider(),
                            ft.TextButton("Inicio", on_click=lambda _: self.NavigateAndClose("/")), 
                            ft.TextButton("Mis Reservas"),
                            ft.TextButton("Habitaciones", on_click=lambda _: self.NavigateAndClose("/allRooms")),
                            ft.Divider(),
                            ft.ElevatedButton("Log in", bgcolor="blue", color="white", width=float("inf")),
                            ft.OutlinedButton("Sign up", width=float("inf"))
                        ]
                    )
                )
            ]
        )
        
        self.icon_menu =ft.IconButton(
              visible=False,
                icon = ft.Image(
                    src= "media/icons/icon_menu.png",
                    height=50,
                    width=50,    
                    ),   
                on_click = self.openMobileMenu
        )

        self.content = ft.Row(
             controls=[
                ft.Row(
                    controls=[self.hotel_name, self.bookings, self.rooms],
                    spacing=50  
                ),
                ft.Row(
                    controls=[self.signup_button, self.login_button,self.icon_menu
                ])
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
        
        
    
    def closeMobileMenu(self, e=None):
        self.top_var_container_mobile.visible = False
        if self.top_var_container_mobile in self.main_page.overlay:
            self.main_page.overlay.remove(self.top_var_container_mobile)
        self.main_page.update()
    
    def openMobileMenu(self, e=None):
        self.top_var_container_mobile.visible = True
        if self.top_var_container_mobile not in self.main_page.overlay:
            self.main_page.overlay.append(self.top_var_container_mobile)
        self.main_page.update()
    
    def NavigateAndClose(self, route):
        self.closeMobileMenu()
        self.main_page.go(route)

    def resize(self, width):
        if not width: return 
        
        is_mobile = width < 800
        
        self.bookings.visible = False if is_mobile else True
        self.rooms.visible = not is_mobile
        self.login_button.visible = not is_mobile
        self.signup_button.visible = not is_mobile
        
        self.icon_menu.visible = is_mobile
