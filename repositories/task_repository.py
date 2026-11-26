"""Se encarga de gestionar el almacenamiento de las tareas."""
from models.task import Task

class TaskRepository:
    """Simula una base de datos en memoria."""

    def __init__(self) -> None:
        self._tasks: list[Task] = []

    def find_all(self) -> list[Task]:
        """Retorna todas las tareas registradas."""
        return self._tasks

    def create_one(self, task: Task):
        """Agrega una tarea."""
        self._tasks.append(task)