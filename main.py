import flet as ft
from src.views.home_page import homePage
from src.views.all_rooms import allRooms
from src.views.user_page import userPage
from src.views.login import logIn
from src.views.signup import signUp
from src.views.page_404 import connectionErrorPage
from src.views.single_room import singleRoom
from src.views.my_bookings import MyBookingsPage

def main(page: ft.Page):
    page.title = "Tenerife Grand Hotel"
    page.username = None

    
    def route_change(route):
        
        print(f"Ruta actual: {page.route}") # Debug para ver qué pasa
        page.views.clear() if page.views  else None
         # Pa s altar directamente a users en debug
        if page.route == "/":
            page.views.append(homePage(page))

        elif page.route == "/userPage":
            page.views.append(userPage(page))
        
        elif page.route == "/allRooms":
            page.views.append(allRooms(page))

        elif page.route == "/404":
            page.views.append(connectionErrorPage(page))

        elif page.route == "/logIn":
            page.views.append(logIn(page))

        elif page.route == "/signUp":
            page.views.append(signUp(page))

        elif page.route == "/singleRoom":
            page.views.append(singleRoom(page))
        
        elif page.route == "/MyBookings":
            page.views.append(MyBookingsPage(page)) # <--- ¡AÑADE LOS PARÉNTESIS!

        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    
    route_change("/")


ft.run(main)