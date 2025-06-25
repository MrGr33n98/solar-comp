"""Página de listagem de empresas."""

import reflex as rx
from ..components.navbar_new import navbar
from ..components.base import card, section_container, stats_card
from ..state.company import CompanyState, LeadState, CompanyData

def rating_select() -> rx.Component:
    """Componente de select para avaliação."""
    return rx.select.root(
        rx.select.trigger(placeholder="Avaliação mínima"),
        rx.select.content(
            rx.select.item("Todas as avaliações", value="0"),
            rx.select.item("4+ estrelas", value="4"),
            rx.select.item("4.5+ estrelas", value="4.5"),
        ),
        value=str(CompanyState.min_rating),
        on_change=CompanyState.set_min_rating,
    )

def search_filters() -> rx.Component:
    """Componente de filtros de busca."""
    return rx.box(
        rx.vstack(
            rx.heading("Encontre Empresas de Energia Solar", size="4", mb=4),
            rx.flex(
                rx.input(
                    placeholder="Buscar por nome ou descrição...",
                    value=CompanyState.search_query,
                    on_change=CompanyState.set_search_query,
                    flex=2,
                ),
                rx.input(
                    placeholder="Cidade",
                    value=CompanyState.selected_city,
                    on_change=CompanyState.set_selected_city,
                    flex=1,
                ),
                rating_select(),
                rx.button(
                    "Buscar",
                    on_click=CompanyState.load_companies,
                    bg="orange.500",
                    color="white",
                    size="2",
                ),                spacing="3",
                width="100%",
                wrap=rx.breakpoints(initial="wrap", sm="nowrap"),
                align_items="center",
            ),
            spacing="4",
            width="100%",
        ),
        bg="gray.50",
        padding="6",
        border_radius="8px",
        mb=8,
        width="100%",
    )

def company_card(company: CompanyData) -> rx.Component:
    """Card individual de empresa."""
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.vstack(
                    rx.hstack(
                        rx.heading(company.name, size="3"),
                        rx.cond(
                            company.is_verified,
                            rx.badge("Verificada", color_scheme="green"),
                        ),
                        spacing="2",
                        align="center",
                    ),
                    rx.text(
                        f"{company.city}, {company.state}",
                        color="gray.600",
                        size="2",
                    ),
                    align="start",
                    spacing="1",
                ),
                rx.spacer(),
                rx.vstack(
                    rx.hstack(
                        rx.text("⭐", size="3"),
                        rx.text(
                            f"{company.average_rating:.1f}",
                            weight="bold",
                        ),
                        rx.text(
                            f"({company.total_reviews} avaliações)",
                            color="gray.600",
                            size="2",
                        ),
                        spacing="1",
                        align="center",
                    ),
                    align="end",
                ),
                width="100%",
                align="start",
            ),
            rx.text(
                company.description[:200] + "..." if len(company.description) > 200
                else company.description,
                color="gray.700",
                size="3",
            ),
            rx.hstack(
                rx.cond(
                    company.phone,
                    rx.text(f"📞 {company.phone}", size="2", color="gray.600"),
                ),
                rx.cond(
                    company.email,
                    rx.text(f"✉️ {company.email}", size="2", color="gray.600"),
                ),
                spacing="4",
            ),
            rx.hstack(
                rx.button(
                    "Ver Detalhes",
                    on_click=rx.redirect(f"/empresa/{company.id}"),
                    variant="outline",
                    color_scheme="orange",
                ),
                rx.button(
                    "Solicitar Orçamento",
                    on_click=lambda: [
                        LeadState.set_selected_company_id(company.id),
                        rx.redirect("/contato")
                    ],
                    bg="orange.500",
                    color="white",
                ),
                spacing="3",
            ),
            spacing="4",
            align="stretch",
        ),
        bg="white",
        padding="6",
        border_radius="8px",
        border="1px solid",
        border_color="gray.200",
        _hover={
            "box_shadow": "0 4px 12px rgba(0,0,0,0.1)",
            "transform": "translateY(-2px)",
        },
        transition="all 0.3s ease",
    )

def companies_grid() -> rx.Component:
    """Grid de empresas."""
    return rx.box(
        rx.cond(
            CompanyState.loading,
            rx.center(
                rx.spinner(size="3"),
                height="200px",
            ),
            rx.cond(
                CompanyState.companies,
                rx.flex(
                    rx.foreach(
                        CompanyState.filter_companies,  # <-- Corrigido aqui
                        company_card,
                    ),
                    wrap=True,
                    gap="6",
                    width="100%",
                    direction=rx.breakpoints(initial="column", sm="row"),
                    justify="flex-start",
                ),
                rx.center(
                    rx.vstack(
                        rx.text("Nenhuma empresa encontrada", size="4", color="gray.600"),
                        rx.button(
                            "Cadastrar Empresa",
                            on_click=rx.redirect("/cadastro-empresa"),
                            bg="orange.500",
                            color="white",
                            size="2",
                        ),
                        spacing="4",
                    ),
                    height="200px",
                ),
            ),
        ),
        width="100%",
    )

def marketplace_stats() -> rx.Component:
    """Seção de estatísticas do marketplace."""
    return section_container(
        [
            rx.flex(
                stats_card("150+", "Empresas Cadastradas", "building"),
                stats_card("2.500+", "Projetos Realizados", "sun"),
                stats_card("4.8/5", "Avaliação Média", "star"),
                stats_card("95%", "Clientes Satisfeitos", "heart"),
                direction=rx.breakpoints(initial="column", sm="row"),
                gap="4",
                width="100%",
            )
        ],
        title="Marketplace Solar",
        subtitle="Conectando você às melhores empresas de energia solar",
        bg_color="gray.50",
    )

def empresas_page() -> rx.Component:
    """Página principal de empresas."""
    return rx.vstack(
        navbar(),
        rx.box(height="64px"),  # Espaçamento para navbar fixa
        marketplace_stats(),
        section_container([
            search_filters(),
            companies_grid(),
        ]),
        spacing="0",
        width="100%",
        on_mount=CompanyState.load_companies,
    )
