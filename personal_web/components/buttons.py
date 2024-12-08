import reflex as rx
import reflex_chakra as rxc

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
    pointer: bool = False,
    **kwargs,
) -> rx.Component:
    hover_dict = {
        "background_color": "transparent",
        "cursor": "pointer" if pointer else "default",
        "box_shadow": f"0 0 8px {button_color}, 0 0 12px {button_color}",
    }
    return rx.link(
        rx.button(
            rx.hstack(
                rx.text(text),
                rx.icon(tag=icon),
                align="center",
                spacing="2",
                font_size=FontSize.BUTTON.value,
                color=text_color,
                padding_x=[Size.VERY_SMALL.value, Size.MEDIUM.value],
            ),
            size="3",
            style=styles.DEFAULT_BUTTON_STYLE,
            border_color=button_color,
            transition="box-shadow 0.3s ease",
            _hover=hover_dict,
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
    hover_color: str = Color.SECONDARY.value,
    **kwargs,
):
    return rx.link(
        rxc.hstack(
            rxc.text(text),
            rxc.icon(tag=icon),
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
                "border_color": hover_color,
                "color": hover_color,
            },
        ),
        href=url,
        is_external=True,
        **kwargs,
    )
