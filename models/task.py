from dataclasses import dataclass, field
from uuid import UUID, uuid4

@dataclass
class Task:
    title: str
    description: str
    uuid: UUID = field(default_factory=uuid4)
