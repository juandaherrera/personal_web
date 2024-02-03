import reflex as rx

import personal_web.styles.styles as styles
from personal_web.styles.fonts import FontSize
from personal_web.styles.styles import Size


def default_button(
    text: str,
    icon: str,
    button_color: str,
    text_color: str,
    url: str = "/",
    **kwargs,
) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.text(text),
                rx.icon(tag=icon),
                font_size=FontSize.BUTTON.value,
                color=text_color,
                padding_x=[Size.VERY_SMALL.value, Size.MEDIUM.value],
            ),
            style=styles.DEFAULT_BUTTON_STYLE,
            border_color=button_color,
            transition="box-shadow 0.3s ease",
            _hover={
                "background_color": "transparent",
                "box_shadow": f"0 0 8px {button_color}, 0 0 12px {button_color}",
            },
        ),
        href=url,  # TO_DO agregar la lógica para scrollear,
        **kwargs,
    )
