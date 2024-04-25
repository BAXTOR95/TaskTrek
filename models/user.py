from .database import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Boolean, DateTime
from flask_login import UserMixin


class User(UserMixin, db.Model):
    """
    Represents a user in the system.

    Attributes:
        id (int): The unique identifier for the user.
        email (str): The email address of the user.
        password (str): The hashed password of the user.
        name (str): The name of the user.
        is_active (bool): Indicates whether the user is active or not.
        last_login (DateTime): The date and time of the user's last login (optional).

    """

    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(255))
    name: Mapped[str] = mapped_column(String(100))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    last_login: Mapped[DateTime] = mapped_column(DateTime)

    # Relationships
    projects: Mapped[list["Project"]] = relationship("Project", back_populates="owner")

    def __repr__(self):
        return f"<User {self.email}>"
