import flet as ft
from Utils.Colors import Colors, list_colors_code


class OptionColor(ft.Row):
    def __init__(self, color: Colors):
        super().__init__()
        self.color = color

        self.controls = [
            ft.Text(self.color.name),
            ft.Container(
                bgcolor=self.color.value,
                border_radius=100,
                width=20,
                height=20,
            )
        ]

class DropdownColor(ft.Dropdown):
    def __init__(self):
        super().__init__()
        self.options = []
        self.create_options()
        self.width = 200

    def create_options(self):
        for color in list_colors_code:
            self.options.append(
                ft.dropdown.Option(
                    text=color.name,
                    content=OptionColor(color),
                )
            )

    def get_color_code(self):
        for color in list_colors_code:
            if self.value == color.name:
                return color.value