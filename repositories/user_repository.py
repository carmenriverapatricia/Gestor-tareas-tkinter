"""Se encarga de gestionar el almacenamiento de los datos en memoria."""

from models.user import User
from uuid import UUID

class UserRepository:
    # Simula mi base de datos
    _users: list[User] = [
        User("Juan", "Santana", 22, "juan.santana@gmail.com"),
        User("Carlos", "Pérez", 18, "carlos.perez@gmail.com"),
        User("María", "Sosa", 32, "maria.sosa@hotmail.com"),
    ]

    def __init__(self) -> None:
        pass

    def find_all(self) -> list[User]:
        """Retorna todos los usuarios registrados."""
        return self._users

    def create_one(self, user: User):
        self._users.append(user)

    def delete_one(self, uuid: UUID):
        # current_users: list[User] = []
        # for user in self._users:
        #     if user.uuid != uuid:
        #         current_users.append(user)

        user = [user for user in self._users if user.uuid != uuid]
        self._users = user

    def update_user(self, uuid: UUID, fname: str, lname: str, age: int, email: str):
        user = [user for user in self._users if user.uuid == uuid]

        if user:
            user[0].fname = fname
            user[0].lname = lname
            user[0].age = age
            user[0].email = email
