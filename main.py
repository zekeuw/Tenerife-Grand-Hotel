import flet as ft
from src.views.home_page import homePage
from src.views.all_rooms import allRooms
from src.views.user_page import userPage

def main(page: ft.Page):
    page.title = "Tenerife Grand Hotel"
    def route_change(route):

        print(f"Ruta actual: {page.route}") # Debug para ver qué pasa
        page.views.clear() if page.views  else None
        page.views.append(homePage(page))
        if page.route == "/userPage":
            page.views.append(userPage(page)) # Pa saltar directamente a users en debug
        if page.route == "/allRooms":
            page.views.append(allRooms(page))
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    
    route_change("/")
ft.run(main)