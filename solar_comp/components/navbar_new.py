"""Componente de navbar da aplicação."""

import reflex as rx
from ..state.auth import AuthState

def navbar() -> rx.Component:
    """Barra de navegação."""
    return rx.hstack(
        # Logo e nome
        rx.hstack(            rx.heading(
                "Solar Marketplace",
                size="4",  # Valores válidos são "1" a "9"
                color="orange.500",
            ),
            spacing="2",
            on_click=rx.redirect("/"),
            cursor="pointer",
        ),
        
        # Espaçador
        rx.spacer(),
        
        # Menu de navegação
        rx.hstack(
            rx.link("Início", href="/", color="gray.700"),
            rx.link("Empresas", href="/empresas", color="gray.700"),
            rx.link("Como Funciona", href="/como-funciona", color="gray.700"),
            spacing="6",
        ),
        
        # Espaçador
        rx.spacer(),
          # Área de autenticação
        rx.cond(
            AuthState.is_authenticated,
            # Usuário logado - menu simples
            rx.hstack(
                rx.text(f"Olá, {AuthState.user_name}", color="gray.700"),                rx.button(
                    "Perfil",
                    on_click=rx.redirect("/profile"),
                    variant="ghost",
                    size="2",
                ),
                rx.cond(
                    AuthState.user_type == "company",
                    rx.button(
                        "Dashboard",
                        on_click=rx.redirect("/dashboard/company"),
                        variant="ghost",
                        size="2",
                    ),
                ),
                rx.button(
                    "Sair",
                    on_click=AuthState.logout,
                    variant="outline",
                    color_scheme="red",
                    size="2",
                ),
                spacing="3",
            ),
            # Usuário não logado
            rx.hstack(
                rx.button(
                    "Entrar",
                    on_click=rx.redirect("/login"),
                    variant="outline",
                    color_scheme="orange",
                ),
                rx.button(
                    "Registrar",
                    on_click=rx.redirect("/register"),
                    bg="orange.500",
                    color="white",
                ),
                spacing="2",
            ),
        ),
        
        width="100%",
        padding_x=8,
        padding_y=4,
        bg="white",
        border_bottom="1px solid",
        border_color="gray.100",
        position="fixed",
        top="0",
        z_index="1000",
    )
