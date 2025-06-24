from sqlmodel import Field, Relationship, SQLModel
from typing import Optional, Dict, Any
import datetime
import uuid

class Review(SQLModel, table=True):
    """Modelo para avaliações de empresas."""
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    company_id: uuid.UUID = Field(foreign_key="company.id")
    user_id: uuid.UUID = Field(foreign_key="user.id")
    rating: int = Field(ge=1, le=5)  # 1-5 estrelas
    comment: Optional[str] = None
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)
    
    # Relacionamentos
    company: "Company" = Relationship(back_populates="reviews")
    user: "User" = Relationship(back_populates="reviews")

class Lead(SQLModel, table=True):
    """Modelo para leads/contatos recebidos."""
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    company_id: uuid.UUID = Field(foreign_key="company.id")
    name: str
    email: str
    phone: Optional[str] = None
    message: str
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)
    status: str = Field(default="new")  # new, contacted, converted, closed

class Message(SQLModel, table=True):
    """Modelo para mensagens entre usuários e empresas."""
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    sender_id: uuid.UUID = Field(foreign_key="user.id")
    receiver_id: uuid.UUID = Field(foreign_key="user.id")
    content: str
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)
    read_at: Optional[datetime.datetime] = None
