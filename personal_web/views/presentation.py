import reflex as rx

import personal_web.constants as const
from personal_web.components.buttons import default_button
from personal_web.components.link_icon import link_icon
from personal_web.components.type_animation import type_animation
from personal_web.components.working_at import working_at
from personal_web.state import MainState
from personal_web.styles import styles
from personal_web.styles.colors import Color, TextColor
from personal_web.styles.styles import Size


def presentation() -> rx.Component:
    return rx.stack(
        rx.center(
            rx.grid(
                rx.stack(
                    rx.avatar(
                        src=const.MAIN_PIC,
                        fallback="JD",
                        size="9",
                        color_scheme="cyan",
                        radius="full",
                        style=styles.MAIN_PIC_STYLE,
                    ),
                    align="center",
                    justify="end",
                    width="100%",
                    aspect_ratio=1 / 1,
                    align_items="center",
                ),
                _hello_iam(),
                columns=rx.breakpoints(
                    initial="1",
                    md="2",
                ),
                width="100%",
                padding_y=Size.DEFAULT_BIG.value,
                spacing_x="9",
                spacing_y="5",
                justify_content="center",
                align_items="center",
            ),
            width=styles.INDEX_SECTION_STYLE["width"],
            padding_x=styles.INDEX_SECTION_STYLE["padding_x"],
        ),
        justify="center",
        style=styles.PRESENTATION_STACK_STYLE,
    )


def _hello_iam() -> rx.Component:
    return rx.vstack(
        rx.text(
            rx.cond(
                MainState.is_language_en,
                "Hello👋🏻, I'm",
                "Hola👋🏻, soy",
            ),
            font_size=[Size.DEFAULT_BIG.value, Size.BIG.value],
            color=TextColor.SECONDARY.value,
            margin_bottom=Size.VERY_SMALL.value,
        ),
        rx.heading(
            "Juan David Herrera",
            size=rx.breakpoints(
                initial="8",
                lg="9",
            ),
            color=TextColor.PRIMARY.value,
            weight="bold",
        ),
        type_animation(
            sequence=const.CURRENT_POSITION,
            repeat=float("inf"),
            speed=20,
            style=dict(
                font_size=[Size.DEFAULT_BIG.value, Size.BIG.value],
                color=TextColor.SECONDARY.value,
                margin_top=Size.VERY_SMALL.value,
            ),
        ),
        # Dónde trabajo?
        working_at(
            const.CURRENT_COMPANY_LOGO,
            const.CURRENT_COMPANY_URL,
            f"Logo de {const.CURRENT_COMPANY_NAME}",
        ),
        rx.divider(
            border_color=TextColor.PRIMARY.value,
        ),
        # Redes
        rx.hstack(
            link_icon(
                "icons/github.svg",
                const.GUTHUB_URL,
                "Logo GitHub",
            ),
            link_icon(
                "icons/linkedin.svg",
                const.LINKEDIN_URL,
                "Logo LinkedIn",
            ),
            spacing="4",
            padding_y=Size.DEFAULT_MEDIUM.value,
        ),
        # Conoce más acerca de mi
        rx.box(
            default_button(
                rx.cond(
                    MainState.is_language_en,
                    "Learn more about me",
                    "Conoce más de mi",
                ),
                "arrow_down",
                Color.PRIMARY.value,
                Color.SECONDARY.value,
                "#about_me",
                pointer=True,
                id="main_button",
            ),
        ),
        spacing="2",
        align_items="start",
    )
