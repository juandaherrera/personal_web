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
                rx.span(
                    f"© {datetime.date.today().year} ",
                ),
                rx.span("by juandaherrera "),
                rx.span(f"v{const.version}", color=Color.SECONDARY.value),
                rx.span("."),
                font_size=Size.DEFAULT.value,
            ),
            href=const.REPO_URL,
            is_external=True,
        ),
        rx.text(
            "Built with ❤ from Palmira, Colombia.",
            font_size=Size.DEFAULT.value,
            margin_top=Size.ZERO.value,
        ),
        spacing=Size.ZERO.value,
        style=FOOTER_STYLE,
    )
