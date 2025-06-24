"""Solar Marketplace - Aplicação Reflex."""

import reflex as rx
from sqlmodel import Session, SQLModel, create_engine
from . import styles
from .pages import *
from .models import *
from .state import AuthState

# Database setup
DATABASE_URL = "sqlite:///solar_marketplace.db"  # URL fixa para desenvolvimento
engine = create_engine(DATABASE_URL)

def create_db_and_tables():
    """Cria as tabelas do banco de dados."""
    SQLModel.metadata.create_all(engine)

# Create the app
app = rx.App(
    style=styles.base_style,
    stylesheets=styles.base_stylesheets,
    theme=rx.theme(
        appearance="light",
        accent_color="orange",
    ),
)

# Importar páginas
from .pages import index, login_page, register_page
from .pages.empresas import empresas_page

# Página inicial
app.add_page(
    index,
    route="/",
    title="Solar Marketplace - Encontre as Melhores Empresas de Energia Solar"
)

# Página de empresas
app.add_page(
    empresas_page,
    route="/empresas",
    title="Empresas de Energia Solar - Solar Marketplace"
)

# Rotas de autenticação
app.add_page(
    login_page,
    route="/login",
    title="Login - Solar Marketplace",
)

app.add_page(
    register_page,
    route="/register",
    title="Registro - Solar Marketplace",
)

# Criar tabelas (apenas em desenvolvimento)
# Em produção, use migrações adequadas
create_db_and_tables()
