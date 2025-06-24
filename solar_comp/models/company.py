from sqlmodel import Field, Relationship, SQLModel
from typing import Optional, List
import datetime
import uuid

class Company(SQLModel, table=True):
    """Modelo para empresas."""
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    name: str = Field(index=True)
    description: Optional[str] = None
    cnpj: str = Field(unique=True, index=True)
    address: Optional[str] = None
    city: str = Field(index=True)
    state: str = Field(index=True)
    phone: Optional[str] = None
    email: Optional[str] = None
    website: Optional[str] = None
    logo_url: Optional[str] = None
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)
    updated_at: datetime.datetime = Field(default_factory=datetime.datetime.now)
    is_active: bool = Field(default=True)
    is_verified: bool = Field(default=False)
    
    # Métricas
    average_rating: float = Field(default=0.0)
    total_reviews: int = Field(default=0)
    
    # Relacionamentos
    users: List["User"] = Relationship(back_populates="company")
    services: List["CompanyService"] = Relationship(back_populates="company")
    projects: List["CompanyProject"] = Relationship(back_populates="company")
    reviews: List["Review"] = Relationship(back_populates="company")

class CompanyService(SQLModel, table=True):
    """Modelo para serviços oferecidos por empresas."""
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    company_id: uuid.UUID = Field(foreign_key="company.id")
    name: str
    description: Optional[str] = None
    price_range: Optional[str] = None
    is_active: bool = Field(default=True)
    
    # Relacionamento
    company: Company = Relationship(back_populates="services")

class CompanyProject(SQLModel, table=True):
    """Modelo para projetos realizados por empresas."""
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    company_id: uuid.UUID = Field(foreign_key="company.id")
    title: str
    description: Optional[str] = None
    location: str
    completion_date: datetime.date
    power_capacity: float  # em kWp
    image_urls: Optional[str] = Field(default=None)  # URLs separadas por vírgula
    
    # Relacionamento
    company: Company = Relationship(back_populates="projects")
