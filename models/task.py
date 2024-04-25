from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Text, ForeignKey, DateTime, Boolean
from sqlalchemy import Enum as SQLEnum
from datetime import datetime, UTC
from enum import Enum, auto
from .database import db


class TaskStatus(Enum):
    TODO = auto()
    IN_PROGRESS = auto()
    DONE = auto()
    ARCHIVED = auto()


class PriorityLevel(Enum):
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()
    URGENT = auto()


class Task(db.Model):
    """Represents a task in the database.

    Attributes:
        id (Mapped[int]): The unique identifier for the task.
        title (Mapped[str]): The title of the task.
        description (Mapped[str]): A description of the task.
        status (Mapped[TaskStatus]): The current status of the task.
        priority (Mapped[PriorityLevel]): The priority of the task.
        created_at (Mapped[datetime]): The creation timestamp of the task.
        updated_at (Mapped[datetime]): The last update timestamp of the task.
        is_active (Mapped[bool]): Whether the task is active or not.
        project_id (Mapped[int]): Foreign key linking to the task's project.
        project (Mapped["Project"]): The project the task belongs to, defined by the relationship with the Project model.
    """

    __tablename__ = 'tasks'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    status: Mapped[TaskStatus] = mapped_column(
        SQLEnum(TaskStatus, name="task_status", create_type=False),
        default=TaskStatus.TODO.name,
    )
    priority: Mapped[PriorityLevel] = mapped_column(
        SQLEnum(PriorityLevel, name="priority_level", create_type=False),
        default=PriorityLevel.MEDIUM.name,
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=lambda: datetime.now(UTC)
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=lambda: datetime.now(UTC),
        onupdate=lambda: datetime.now(UTC),
    )
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    project_id: Mapped[int] = mapped_column(Integer, ForeignKey('projects.id'))

    # Relationships
    project: Mapped["Project"] = relationship("Project", back_populates="tasks")

    def __repr__(self):
        return f"<Task {self.title}>"
