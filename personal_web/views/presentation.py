import reflex as rx

import personal_web.constants as const
import personal_web.styles.styles as styles
from personal_web.components.buttons import default_button
from personal_web.components.link_icon import link_icon
from personal_web.components.type_animation import type_animation
from personal_web.components.working_at import working_at
from personal_web.styles.colors import Color, TextColor
from personal_web.styles.styles import Size


def presentation() -> rx.Component:
    return rx.chakra.stack(
        rx.chakra.center(
            rx.chakra.responsive_grid(
                rx.chakra.stack(
                    rx.chakra.avatar(
                        src=const.MAIN_PIC,
                        size="full",
                        style=styles.MAIN_PIC_STYLE,
                    ),
                    width="100%",
                    aspect_ratio=1 / 1,
                    align_items="end",
                ),
                _hello_iam(),
                columns=[1, 1, 1, 2, 2],
                width="100%",
                padding_y=Size.DEFAULT_BIG.value,
                spacing_x=Size.VERY_BIG.value,
                spacing_y=Size.BIG.value,
                justify_content="center",
                align_items="center",
            ),
            width=styles.INDEX_SECTION_STYLE["width"],
            padding_x=styles.INDEX_SECTION_STYLE["padding_x"],
        ),
        style=styles.PRESENTATION_STACK_STYLE,
    )


def _hello_iam() -> rx.Component:
    return rx.chakra.vstack(
        rx.chakra.text(
            "Hola👋🏻, soy",
            font_size=[Size.DEFAULT_BIG.value, Size.BIG.value],
            color=TextColor.SECONDARY.value,
            padding_buttom=Size.ZERO.value,
        ),
        rx.chakra.heading(
            "Juan David Herrera",
            size="2xl",
            color=TextColor.PRIMARY.value,
        ),
        type_animation(
            sequence=const.CURRENT_POSITION,
            repeat=float("inf"),
            speed=20,
            style=dict(
                font_size=[Size.DEFAULT_BIG.value, Size.BIG.value],
                color=TextColor.SECONDARY.value,
            ),
        ),
        # Dónde trabajo?
        working_at(
            const.CURRENT_COMPANY_LOGO,
            const.CURRENT_COMPANY_URL,
            f"Logo de {const.CURRENT_COMPANY_NAME}",
        ),
        rx.chakra.divider(
            border_color=TextColor.PRIMARY.value,
        ),
        # Redes
        rx.chakra.hstack(
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
            link_icon(
                "icons/instagram.svg",
                const.INSTAGRAM_URL,
                "Logo Instagram",
            ),
            spacing=Size.DEFAULT_MEDIUM.value,
            padding_y=Size.DEFAULT_MEDIUM.value,
        ),
        # Conoce más acerca de mi
        rx.chakra.box(
            default_button(
                "Conoce más de mi",
                "arrow_down",
                Color.PRIMARY.value,
                Color.SECONDARY.value,
                "#about_me",
                id="main_button",
            ),
            # display="none",
        ),
        align_items="start",
    )
