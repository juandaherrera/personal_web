import datetime

import reflex as rx

import personal_web.constants as const
from personal_web.styles.colors import Color, TextColor
from personal_web.styles.styles import FOOTER_LOGO_STYLE, FOOTER_STYLE, Size


def footer() -> rx.Component:
    return rx.chakra.vstack(
        rx.chakra.image(
            src="favicon.ico",
            alt="Logo de Juan David Herrera. Es una 'j' y una 'd juntas",
            style=FOOTER_LOGO_STYLE,
        ),
        rx.chakra.link(
            rx.chakra.text(
                rx.chakra.span(
                    f"© {datetime.date.today().year} ",
                ),
                rx.chakra.span("by juandaherrera "),
                rx.chakra.span(f"v{const.version}", color=Color.SECONDARY.value),
                rx.chakra.span("."),
                font_size=Size.DEFAULT.value,
            ),
            href=const.REPO_URL,
            is_external=True,
        ),
        rx.chakra.text(
            "Built with ❤ from Palmira, Colombia.",
            font_size=Size.DEFAULT.value,
            margin_top=Size.ZERO.value,
        ),
        spacing=Size.ZERO.value,
        style=FOOTER_STYLE,
    )
