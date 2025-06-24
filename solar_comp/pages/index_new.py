"""Página inicial da aplicação."""

import reflex as rx
from ..components.navbar_new import navbar
from ..components.base import hero_section, section_container, card, stats_card

def features_section() -> rx.Component:
    """Seção de características principais."""
    return section_container(
        [
            rx.flex(
                card(
                    "Empresas Verificadas",
                    "Todas as empresas passam por um processo rigoroso de verificação para garantir qualidade e confiabilidade.",
                ),
                card(
                    "Orçamentos Gratuitos",
                    "Receba múltiplos orçamentos gratuitamente e compare as melhores ofertas para seu projeto solar.",
                ),
                card(
                    "Suporte Especializado",
                    "Nossa equipe de especialistas está sempre disponível para ajudar você em cada etapa do processo.",
                ),
                direction=rx.breakpoints(initial="column", md="row"),
                gap="6",
                width="100%",
            )
        ],
        title="Por que escolher o Solar Marketplace?",
        subtitle="Conectamos você às melhores empresas de energia solar do Brasil",
    )

def how_it_works() -> rx.Component:
    """Seção explicando como funciona."""
    return section_container(
        [
            rx.flex(
                rx.vstack(
                    rx.box(
                        rx.text("1", size="6", weight="bold", color="white"),
                        bg="orange.500",
                        border_radius="50%",
                        width="60px",
                        height="60px",
                        display="flex",
                        align_items="center",
                        justify_content="center",
                        mb=4,
                    ),
                    rx.heading("Busque Empresas", size="3", mb=2),
                    rx.text(
                        "Encontre empresas especializadas em energia solar na sua região",
                        text_align="center",
                        color="gray.600",
                    ),
                    align="center",
                ),
                rx.vstack(
                    rx.box(
                        rx.text("2", size="6", weight="bold", color="white"),
                        bg="orange.500",
                        border_radius="50%",
                        width="60px",
                        height="60px",
                        display="flex",
                        align_items="center",
                        justify_content="center",
                        mb=4,
                    ),
                    rx.heading("Compare Orçamentos", size="3", mb=2),
                    rx.text(
                        "Solicite orçamentos gratuitos e compare preços e serviços",
                        text_align="center",
                        color="gray.600",
                    ),
                    align="center",
                ),
                rx.vstack(
                    rx.box(
                        rx.text("3", size="6", weight="bold", color="white"),
                        bg="orange.500",
                        border_radius="50%",
                        width="60px",
                        height="60px",
                        display="flex",
                        align_items="center",
                        justify_content="center",
                        mb=4,
                    ),
                    rx.heading("Instale e Economize", size="3", mb=2),
                    rx.text(
                        "Escolha a melhor opção e comece a economizar na sua conta de luz",
                        text_align="center",
                        color="gray.600",
                    ),
                    align="center",
                ),
                direction=rx.breakpoints(initial="column", md="row"),
                gap="8",
                width="100%",
            )
        ],
        title="Como Funciona",
        subtitle="Em 3 passos simples você encontra a empresa ideal",
        bg_color="gray.50",
    )

def cta_section() -> rx.Component:
    """Call-to-action final."""
    return rx.box(
        rx.container(
            rx.center(
                rx.vstack(
                    rx.heading(
                        "Pronto para Economizar com Energia Solar?",
                        size="5",
                        text_align="center",
                        color="white",
                        mb=4,
                    ),
                    rx.text(
                        "Junte-se a milhares de brasileiros que já reduziram sua conta de luz em até 95%",
                        text_align="center",
                        color="white",
                        opacity="0.9",
                        size="4",
                        mb=8,
                    ),
                    rx.hstack(
                        rx.link(
                            rx.button(
                                "Ver Empresas",
                                bg="white",
                                color="orange.500",
                                size="3",
                                padding_x="8",
                            ),
                            href="/empresas",
                        ),
                        rx.link(
                            rx.button(
                                "Cadastrar Empresa",
                                variant="outline",
                                color="white",
                                border_color="white",
                                size="3",
                                padding_x="8",
                            ),
                            href="/cadastro-empresa",
                        ),
                        spacing="4",
                    ),
                    spacing="4",
                    align="center",
                    max_width="600px",
                ),
            ),
            max_width="1200px",
            padding_x=["4", "6", "8"],
            padding_y="16",
        ),
        background="linear-gradient(135deg, #ed8936 0%, #c05621 100%)",
        width="100%",
    )

def index() -> rx.Component:
    """Página inicial."""
    return rx.vstack(
        navbar(),
        hero_section(
            title="Encontre as Melhores Empresas de Energia Solar",
            subtitle="Compare orçamentos gratuitos e escolha a empresa ideal para seu projeto de energia solar",
            cta_text="Encontrar Empresas",
            cta_href="/empresas",
        ),
        features_section(),
        how_it_works(),
        cta_section(),
        spacing="0",
        width="100%",
    )
