import flet as ft
from Components.TodoApp import TodoApp


def main(page: ft.Page):
    page.title = "To-Do App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    # create application instance
    app = TodoApp(page)

    # add application's root control to the page
    page.add(app)


ft.app(target=main)