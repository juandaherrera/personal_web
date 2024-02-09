import reflex as rx

import personal_web.styles.styles as styles
from personal_web.styles.colors import Color, TextColor
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
        href=url,
        **kwargs,
    )


def rounded_button(
    text: str,
    url: str,
    icon: str = "external_link",
    border_color: str = TextColor.PRIMARY.value,
    text_color: str = TextColor.SECONDARY.value,
    text_size: str = FontSize.SMALL_TEXT.value,
    **kwargs,
):
    return rx.link(
        rx.hstack(
            rx.text(text),
            rx.icon(tag=icon),
            color=text_color,
            font_size=text_size,
            spacing=Size.SMALL.value,
            align_items="center",
            border="0.1em solid",
            border_color=border_color,
            border_radius="1.2em",
            padding_y="0.5em",
            padding_x="1em",
            transition="border-color 0.25s ease, color 0.25s ease",
            _hover={
                "border_color": Color.SECONDARY.value,
                "color": Color.SECONDARY.value,
            },
        ),
        href=url,
        is_external=True,
        **kwargs,
    )
