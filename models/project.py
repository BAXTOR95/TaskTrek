from .database import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Text, DateTime, ForeignKey, Boolean
from datetime import datetime, UTC
from typing import List


class Project(db.Model):
    """Represents a project in the database.

    Attributes:
        id (Mapped[int]): The unique identifier for the project.
        title (Mapped[str]): The title of the project.
        description (Mapped[str]): A description of the project.
        created_at (Mapped[datetime]): The creation timestamp of the project.
        updated_at (Mapped[datetime]): The last update timestamp of the project.
        is_active (Mapped[bool]): Whether the project is active or not.
        owner_id (Mapped[int]): Foreign key linking to the project's owner.
        tasks (relationship): A list of tasks related to the project.
        owner (Mapped["User"]): The owner of the project, defined by the relationship with the User model.
    """

    __tablename__ = 'projects'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=lambda: datetime.now(UTC)
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=lambda: datetime.now(UTC),
        onupdate=lambda: datetime.now(UTC),
    )
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    # Relationships
    owner_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'))
    tasks: Mapped[List["Task"]] = relationship("Task", back_populates="project")
    owner: Mapped["User"] = relationship("User", back_populates="projects")

    def __repr__(self):
        return f"<Project {self.title}>"
