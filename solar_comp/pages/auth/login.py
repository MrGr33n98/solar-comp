"""Página de login da aplicação."""

import reflex as rx
from ...state.auth import AuthState
from ...components.navbar_new import navbar

def login_form() -> rx.Component:
    """Formulário de login."""
    return rx.vstack(
        rx.heading("Login", size="4", mb=6),
        
        rx.input(
            placeholder="Email",
            value=AuthState.email,
            on_change=AuthState.set_email,
            mb=4,
        ),
        
        rx.input(
            type_="password",
            placeholder="Senha",
            value=AuthState.password,
            on_change=AuthState.set_password,
            mb=4,
        ),
        
        rx.button(
            "Entrar",
            on_click=AuthState.login,
            width="100%",
            bg="orange.500",
            color="white",
            mb=4,
        ),
        
        rx.cond(
            AuthState.login_error,
            rx.text(
                AuthState.login_error,
                color="red.500",
                size="sm",
                mb=4,
            ),
        ),
        
        rx.hstack(
            rx.text("Ainda não tem uma conta?"),
            rx.link(
                "Registre-se",
                href="/register",
                color="orange.500",
            ),
            spacing="2",
        ),
        
        width="100%",
        max_width="400px",
        padding=8,
        bg="white",
        border_radius="lg",
        box_shadow="lg",
    )

def login_page() -> rx.Component:
    """Página de login."""
    return rx.vstack(
        navbar(),
        rx.center(
            login_form(),
            width="100%",
            min_height="calc(100vh - 64px)",  # altura total menos navbar
            bg="gray.50",
        ),
        width="100%",
        spacing=0,
    )
