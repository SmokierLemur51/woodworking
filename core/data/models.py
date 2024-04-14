"""
file:   core/data/models.py

    SQLAlchemy models defined for this application. 

author: Logan Lee
"""
from typing import List
from typing import Optional
from sqlalchemy import (
    DeclarativeBase,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import 
(
    Mapped,
    mapped_column,
    relationship,
)


class Base(DeclarativeBase):
    pass


class Lumber(Base):
    __tablename__ = "lumber"
    id: Mapped[int] = mapped_column(primary_key=True)
    thickness: Mapped[int] = mapped_column(Integer)
    width: Mapped[int] = mapped_column(Integer)
    length: Mapped[int] = mapped_column(Integer)

    def __repr__(self) -> str:
        return "{}x{}x{}".format(self.thickness, self.width, self.length)


class Supplier(Base):
    __tablename__ = "supplier"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120))
    street: Mapped[str] = mapped_column(String(120), unique=True)

    def __repr__(self) -> str:
        return "{} -- {}".format(self.name, self.street)


class ProjectEstimate(Base):
    __tablename__ = "project"
    id: Mapped[int] = mapped_column(primary_key=True)
    codename: Mapped[str] = mapped_column(String(120))


    def __repr__(self) -> str:
        return "Project {}".format(self.codename)
    
    def calculate_cost() -> float:
        return 0.0


class ProjectBlueprint(Base):
    pass


class Order(Base):
    pass

