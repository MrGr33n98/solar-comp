import reflex as rx

from solar_comp import styles


def card(*children, **props):
    return rx.card(
        *children,
        box_shadow=styles.box_shadow_style,
        size="3",
        width="100%",
        **props,
    )
