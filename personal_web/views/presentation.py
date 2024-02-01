import reflex as rx

import personal_web.constants as const
import personal_web.styles.styles as styles
from personal_web.components.buttons import default_button
from personal_web.components.link_icon import link_icon
from personal_web.components.type_animation import type_animation
from personal_web.components.working_at import working_at
from personal_web.styles.colors import Color, TextColor
from personal_web.styles.styles import Size


def hello_iam() -> rx.Component:
    return rx.vstack(
        rx.text(
            "Hola👋🏻, soy",
            font_size=[Size.DEFAULT_BIG.value, Size.BIG.value],
            color=TextColor.SECONDARY.value,
            padding_buttom=Size.ZERO.value,
        ),
        rx.heading(
            "Juan David Herrera",
            size="2xl",
            color=TextColor.PRIMARY.value,
        ),
        type_animation(
            sequence=const.CURRENT_POSITION,
            repeat=float("inf"),
            speed=20,
            style=dict(
                font_size=Size.BIG.value,
                color=TextColor.SECONDARY.value,
            ),
        ),
        # Dónde trabajo?
        working_at(
            const.CURRENT_COMPANY_LOGO,
            const.CURRENT_COMPANY_URL,
            f"Logo {const.CURRENT_COMPANY_NAME}",
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
            link_icon(
                "icons/instagram.svg",
                const.INSTAGRAM_URL,
                "Logo Instagram",
            ),
            spacing=Size.DEFAULT_MEDIUM.value,
            padding_y=Size.DEFAULT_MEDIUM.value,
        ),
        # Conoce más acerca de mi
        rx.box(
            default_button(
                "Conoce más de mi",
                "arrow_down",
                Color.PRIMARY.value,
                Color.SECONDARY.value,
            ),
        ),
        align_items="start",
    )


def presentation() -> rx.Component:
    return rx.stack(
        rx.center(
            rx.responsive_grid(
                rx.center(
                    rx.avatar(
                        src=const.MAIN_PIC,
                        size="full",
                        style=styles.MAIN_PIC_STYLE,
                    ),
                    max_width=["20em", "30em", "40em"],
                ),
                hello_iam(),
                columns=[1, 1, 1, 2, 2],
                width="100%",
                padding_x=Size.VERY_BIG.value,
                padding_y=Size.DEFAULT_BIG.value,
                spacing=Size.VERY_BIG.value,
                justify_content="center",
                align_items="center",
            ),
        ),
        style=styles.PRESENTATION_STACK_STYLE,
    )
