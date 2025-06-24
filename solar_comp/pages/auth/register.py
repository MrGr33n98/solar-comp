"""Página de registro da aplicação."""

import reflex as rx
from ...state.auth import AuthState
from ...components.navbar_new import navbar

def register_form() -> rx.Component:
    """Formulário de registro."""
    return rx.vstack(
        rx.heading("Criar Conta", size="4", mb=6),
        
        rx.input(
            placeholder="Nome Completo",
            value=AuthState.full_name,
            on_change=AuthState.set_full_name,
            mb=4,
        ),
        
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
        
        rx.input(
            type_="password",
            placeholder="Confirmar Senha",
            value=AuthState.confirm_password,
            on_change=AuthState.set_confirm_password,
            mb=4,
        ),
        
        rx.button(
            "Registrar",
            on_click=AuthState.register,
            width="100%",
            bg="orange.500",
            color="white",
            mb=4,
        ),
        
        rx.cond(
            AuthState.form_error,
            rx.text(
                AuthState.form_error,
                color="red.500",
                size="sm",
                mb=4,
            ),
        ),
        
        rx.hstack(
            rx.text("Já tem uma conta?"),
            rx.link(
                "Faça login",
                href="/login",
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

def register_page() -> rx.Component:
    """Página de registro."""
    return rx.vstack(
        navbar(),
        rx.center(
            register_form(),
            width="100%",
            min_height="calc(100vh - 64px)",  # altura total menos navbar
            bg="gray.50",
        ),
        width="100%",
        spacing=0,
    )
