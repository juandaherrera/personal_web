import datetime

import reflex as rx

import personal_web.constants as const
from personal_web.state import MainState
from personal_web.styles.colors import Color
from personal_web.styles.styles import FOOTER_LOGO_STYLE, FOOTER_STYLE, Size


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="favicon.ico",
            alt="Logo de Juan David Herrera. Es una 'j' y una 'd juntas",
            loading="lazy",
            style=FOOTER_LOGO_STYLE,
        ),
        rx.text(
            rx.text.span(
                f"© {datetime.date.today().year} ",
            ),
            rx.text.span("by juandaherrera "),
            rx.link(
                rx.text.span(
                    f"v{const.version}",
                    color=Color.SECONDARY.value,
                    transition="transform 0.2s ease, text-shadow 0.3s ease, color 0.5s ease",
                    _hover={
                        "color": Color.SECONDARY.value,
                        "text_shadow": f"0 0 6px {Color.PRIMARY.value}",
                        "transform": "scale(1.25)",
                    },
                ),
                color="inherit",
                href=const.REPO_URL,
                is_external=True,
            ),
            rx.text.span("."),
            font_size=Size.DEFAULT.value,
        ),
        rx.text(
            rx.cond(
                MainState.is_language_en,
                "Built with 🧡 from Palmira, Colombia 🇨🇴",
                "Hecho con 🧡 desde Palmira, Colombia 🇨🇴",
            ),
            font_size=Size.DEFAULT.value,
            margin_top=Size.ZERO.value,
        ),
        align="center",
        spacing="0",
        style=FOOTER_STYLE,
    )
