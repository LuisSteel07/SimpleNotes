import flet as ft

class AlertPanel(ft.AlertDialog):
    def __init__(self, root: ft.Page, info: str):
        super().__init__()
        self.root = root
        self.info = info

        self.title = ft.Text("Ha ocurrido un error")

        self.content = ft.Container(
            content=ft.Text(f"{info}")
        )

        self.actions = [
            ft.IconButton(
                icon=ft.icons.CLOSE_ROUNDED,
                bgcolor=ft.colors.RED_700,
                icon_color=ft.colors.RED_100,
                on_click=lambda e: self.root.close(self)
            )
        ]
