"""Componentes básicos reutilizáveis da aplicação."""

import reflex as rx
from typing import Optional, List

def card(
    title: str,
    content: str,
    image_url: Optional[str] = None,
    action_text: Optional[str] = None,
    action_href: Optional[str] = None,
    **props
) -> rx.Component:
    """Card reutilizável para diferentes tipos de conteúdo."""
    return rx.box(
        rx.vstack(
            rx.cond(
                image_url,
                rx.image(
                    src=image_url,
                    width="100%",
                    height="200px",
                    object_fit="cover",
                    border_radius="8px 8px 0 0",
                ),
            ),
            rx.box(
                rx.heading(title, size="3", mb=3),
                rx.text(content, color="gray.600", mb=4),
                rx.cond(
                    action_text and action_href,
                    rx.link(
                        rx.button(
                            action_text,
                            bg="orange.500",
                            color="white",
                            size="2",
                        ),
                        href=action_href,
                    ),
                ),
                padding="4",
            ),
            spacing="0",
        ),
        bg="white",
        border_radius="8px",
        box_shadow="0 2px 4px rgba(0,0,0,0.1)",
        overflow="hidden",
        transition="all 0.3s ease",
        _hover={
            "transform": "translateY(-2px)",
            "box_shadow": "0 4px 8px rgba(0,0,0,0.15)",
        },
        **props
    )

def section_container(
    children: List[rx.Component],
    title: Optional[str] = None,
    subtitle: Optional[str] = None,
    bg_color: str = "white",
    **props
) -> rx.Component:
    """Container padrão para seções da aplicação."""
    return rx.box(
        rx.container(
            rx.vstack(
                rx.cond(
                    title,
                    rx.vstack(
                        rx.heading(title, size="5", text_align="center"),
                        rx.cond(
                            subtitle,
                            rx.text(
                                subtitle,
                                color="gray.600",
                                text_align="center",
                                size="4",
                            ),
                        ),
                        spacing="2",
                        mb=8,
                    ),
                ),
                *children,
                spacing="6",
                align="stretch",
            ),
            max_width="1200px",
            padding_x=["4", "6", "8"],
            padding_y="12",
        ),
        bg=bg_color,
        width="100%",
        **props
    )

def hero_section(
    title: str,
    subtitle: str,
    cta_text: str,
    cta_href: str,
    bg_gradient: str = "linear-gradient(135deg, #f6ad55 0%, #ed8936 100%)",
) -> rx.Component:
    """Seção hero reutilizável."""
    return rx.box(
        rx.container(
            rx.center(
                rx.vstack(
                    rx.heading(
                        title,
                        size="6",
                        color="white",
                        text_align="center",
                        mb=4,
                    ),
                    rx.text(
                        subtitle,
                        color="white",
                        opacity="0.9",
                        text_align="center",
                        size="4",
                        mb=8,
                    ),
                    rx.link(
                        rx.button(
                            cta_text,
                            bg="white",
                            color="orange.500",
                            size="3",
                            padding_x="8",
                            padding_y="3",
                        ),
                        href=cta_href,
                    ),
                    spacing="4",
                    align="center",
                    max_width="600px",
                ),
                min_height="500px",
            ),
            max_width="1200px",
            padding_x=["4", "6", "8"],
        ),
        background=bg_gradient,
        width="100%",
    )

def stats_card(value: str, label: str, icon: Optional[str] = None) -> rx.Component:
    """Card para exibir estatísticas."""
    return rx.box(
        rx.vstack(
            rx.cond(
                icon,
                rx.icon(icon, size=24, color="orange.500", mb=2),
            ),
            rx.heading(value, size="4", color="orange.500"),
            rx.text(label, color="gray.600", text_align="center"),
            spacing="2",
            align="center",
        ),
        bg="white",
        padding="6",
        border_radius="8px",
        border="1px solid",
        border_color="gray.200",
        text_align="center",
    )
