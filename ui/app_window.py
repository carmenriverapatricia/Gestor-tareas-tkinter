"""Interfaz gráfica de la aplicación."""
import tkinter as tk
from tkinter import ttk
from services.task_service import TaskService


class AppWindow(tk.Tk):

    def __init__(self, service: TaskService) -> None:
        super().__init__()
        self.service = service

        self.title("Gestor de tareas")
        self.geometry("600x400")

        self.create_widgets()
        self.render_data_table()

    def create_widgets(self):
        tk.Label(self, text="Título de la tarea").pack()
        self.entry_title = tk.Entry(self, width=40)
        self.entry_title.pack()

        tk.Label(self, text="Descripción de la tarea").pack()
        self.entry_description = tk.Entry(self, width=40)
        self.entry_description.pack()

        self.create_btn = tk.Button(
            self,
            text="Crear tarea",
            command=self.create_task
        )
        self.create_btn.pack(pady=10)

        self.tree = ttk.Treeview(
            self,
            columns=("uuid", "title", "description"),
            show="headings"
        )

        self.tree.heading("uuid", text="ID")
        self.tree.heading("title", text="Título")
        self.tree.heading("description", text="Descripción")

        self.tree.column("uuid", width=150)
        self.tree.column("title", width=150)
        self.tree.column("description", width=250)

        self.tree.pack(fill="both", expand=True)

    def create_task(self):
        title = self.entry_title.get()
        description = self.entry_description.get()

        if not title or not description:
            return

        self.service.create_one(title, description)

        self.entry_title.delete(0, "end")
        self.entry_description.delete(0, "end")

        self.render_data_table()

    def render_data_table(self):
        tasks = self.service.find_all()

        for item in self.tree.get_children():
            self.tree.delete(item)

        for task in tasks:
            self.tree.insert(
                "",
                "end",
                values=(str(task.uuid), task.title, task.description)
            )