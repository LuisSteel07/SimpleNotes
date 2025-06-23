import flet as ft

from Components.AlertPanel import AlertPanel
from Components.Task import Task
from controler import get_notes, add_note, delete_note


class TodoApp(ft.Column):
    # application's root control is a Column containing all other controls
    def __init__(self, root: ft.Page):
        super().__init__()
        self.new_task = ft.TextField(hint_text="Whats needs to be done?", expand=True)
        self.text_task = ft.TextField(hint_text="Task information", expand=True)
        self.tasks = ft.Column()
        self.root = root

        if len(get_notes()) != 0:
            for i in get_notes():
                print(i[2])
                self.tasks.controls.append(Task(i[1], i[2], self.task_status_change, self.task_delete))

        self.filter = ft.Tabs(
            selected_index=0,
            on_change=self.tabs_changed,
            tabs=[ft.Tab(text="all"), ft.Tab(text="active"), ft.Tab(text="completed")],
        )
        self.width = 600
        self.controls = [
            ft.Row(
                controls=[
                    self.new_task,
                    self.text_task,
                    ft.FloatingActionButton(
                        icon=ft.Icons.ADD, on_click=self.add_clicked
                    ),
                ],
            ),
            ft.Column(
                spacing=25,
                controls=[
                    self.filter,
                    self.tasks,
                ],
            ),
        ]

    def add_clicked(self, e):
        if self.new_task.value == "" or self.text_task.value == "":
            self.root.open(AlertPanel(self.root, "Debe de colocar los valores requeridos."))
        else:
            task = Task(self.new_task.value, self.text_task.value, self.task_status_change, self.task_delete)
            add_note(self.new_task.value, self.text_task.value)
            self.tasks.controls.append(task)
            self.new_task.value = ""
            self.text_task.value = ""
            self.update()

    def task_status_change(self):
        self.update()

    def task_delete(self, task):
        self.tasks.controls.remove(task)
        delete_note(task.id)
        self.update()

    def before_update(self):
        status = self.filter.tabs[self.filter.selected_index].text
        for task in self.tasks.controls:
            task.visible = (
                status == "all"
                or (status == "active" and task.completed == False)
                or (status == "completed" and task.completed)
            )

    def tabs_changed(self, e):
        self.update()

