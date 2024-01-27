import reflex as rx

import personal_web.constants as const
from personal_web.components.buttons import default_button
from personal_web.components.link_icon import link_icon
from personal_web.components.main_pic import main_pic
from personal_web.components.working_at import working_at
from personal_web.styles.colors import Color, TextColor
from personal_web.styles.styles import Size


def presentation() -> rx.Component:
    return rx.center(
        rx.hstack(
            main_pic(const.MAIN_PIC),
            rx.vstack(
                rx.text(
                    "Hola👋🏻, soy",
                    font_size=Size.BIG.value,
                    color=TextColor.SECONDARY.value,
                    padding_buttom=Size.ZERO.value,
                ),
                rx.heading(
                    "Juan David Herrera",
                    size="3xl",
                    color=TextColor.PRIMARY.value,
                ),
                rx.text(
                    const.CURRENT_POSITION,
                    font_size=Size.BIG.value,
                    color=TextColor.SECONDARY.value,
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
                        "icons/github.svg", const.GUTHUB_URL, "Logo GitHub"
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
                        TextColor.TERTIARY.value,
                    ),
                ),
                align_items="start",
            ),
            width="100%",
            padding_x=Size.VERY_BIG.value,
            padding_y=Size.DEFAULT_BIG.value,
            spacing=Size.BIG.value,
        ),
    )
