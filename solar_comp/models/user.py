from sqlmodel import Field, Relationship, SQLModel
from typing import Optional, List
import datetime
import uuid

class User(SQLModel, table=True):
    """Modelo para usuários do sistema."""
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    email: str = Field(index=True)
    hashed_password: str
    full_name: str
    user_type: str = Field(default="consumer")  # consumer, company, admin
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)
    updated_at: datetime.datetime = Field(default_factory=datetime.datetime.now)
    is_active: bool = Field(default=True)
    
    # Relacionamentos (serão definidos posteriormente)
    company_id: Optional[uuid.UUID] = Field(default=None, foreign_key="company.id")
    reviews: List["Review"] = Relationship(back_populates="user")
