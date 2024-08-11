import datetime

import reflex as rx

import personal_web.constants as const
from personal_web.styles.colors import Color, TextColor
from personal_web.styles.styles import FOOTER_LOGO_STYLE, FOOTER_STYLE, Size


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="favicon.ico",
            alt="Logo de Juan David Herrera. Es una 'j' y una 'd juntas",
            style=FOOTER_LOGO_STYLE,
        ),
        rx.link(
            rx.text(
                rx.text.span(
                    f"© {datetime.date.today().year} ",
                ),
                rx.text.span("by juandaherrera "),
                rx.text.span(f"v{const.version}", color=Color.SECONDARY.value),
                rx.text.span("."),
                font_size=Size.DEFAULT.value,
            ),
            color="inherit",
            href=const.REPO_URL,
            is_external=True,
        ),
        rx.text(
            "Built with ❤ from Palmira, Colombia.",
            font_size=Size.DEFAULT.value,
            margin_top=Size.ZERO.value,
        ),
        align="center",
        spacing="0",
        style=FOOTER_STYLE,
    )
