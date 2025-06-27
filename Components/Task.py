import flet as ft

from controler import get_id, update_note


class Task(ft.Container):
    def __init__(self, task_name: str, text: str, color: str, task_status_change, task_delete):
        super().__init__()
        self.border_radius = 20
        self.padding = 20
        self.id = get_id() + 1
        self.completed = False
        self.task_name = task_name
        self.text = text
        self.bgcolor = color

        self.task_status_change = task_status_change
        self.task_delete = task_delete
        self.display_task = ft.Checkbox(
            value=False, label=self.task_name, on_change=self.status_changed
        )
        self.display_text = ft.Text(value=self.text)

        self.edit_name = ft.TextField(expand=1)
        self.edit_text = ft.TextField(expand=1)

        self.display_view = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Column([
                    self.display_task,
                    self.display_text
                ]),
                ft.Row(
                    spacing=10,
                    controls=[
                        ft.IconButton(
                            icon=ft.Icons.CREATE_OUTLINED,
                            tooltip="Edit To-Do",
                            on_click=self.edit_clicked,
                            icon_color=ft.colors.WHITE,
                            bgcolor=ft.colors.GREEN_900
                        ),
                        ft.IconButton(
                            ft.Icons.DELETE_OUTLINE,
                            tooltip="Delete To-Do",
                            on_click=self.delete_clicked,
                            icon_color=ft.colors.WHITE,
                            bgcolor=ft.colors.RED_900
                        ),
                    ],
                ),
            ],
        )

        self.edit_view = ft.Row(
            visible=False,
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                self.edit_name,
                self.edit_text,
                ft.IconButton(
                    icon=ft.Icons.DONE_OUTLINE_OUTLINED,
                    icon_color=ft.Colors.GREEN,
                    tooltip="Update To-Do",
                    on_click=self.save_clicked,
                ),
            ],
        )
        self.content = ft.Column([
            self.display_view,
            self.edit_view
        ])

    def edit_clicked(self, e):
        self.edit_name.value = self.display_task.label
        self.edit_text.value = self.text
        self.display_view.visible = False
        self.edit_view.visible = True
        self.update()

    def save_clicked(self, e):
        self.display_task.label = self.edit_name.value
        self.display_text.value = self.edit_text.value
        update_note(self.id, self.edit_name.value, self.edit_text.value, self.completed)
        self.display_view.visible = True
        self.edit_view.visible = False
        self.update()

    def status_changed(self, e):
        self.completed = self.display_task.value
        update_note(self.id, self.task_name, self.text, self.completed)
        self.task_status_change()

    def delete_clicked(self, e):
        self.task_delete(self)

