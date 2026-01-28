import flet as ft
from src.views.home_page import homePage
from src.views.all_rooms import allRooms
from src.views.page_404 import connectionErrorPage

def main(page: ft.Page):
    page.title = "Tenerife Grand Hotel"
    def route_change(route):

        print(f"Ruta actual: {page.route}") # Debug para ver qué pasa
        page.views.clear() if page.views  else None
        if page.route == "/":
            page.views.append(homePage(page))
        
        elif page.route == "/allRooms":
            page.views.append(allRooms(page))

        elif page.route == "/404":
            page.views.append(connectionErrorPage(page))
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    
    route_change("/")
ft.run(main)