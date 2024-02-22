import reflex as rx

from personal_web.styles.colors import Color, TextColor
from personal_web.styles.styles import Size


def title(
    text: str,
    size: str = "2xl",
    color: str = TextColor.PRIMARY.value,
    id: str = None,
    margin_bottom: str = Size.VERY_SMALL.value,
    **kwargs,
) -> rx.Component:
    return rx.chakra.heading(
        text,
        size=size,
        color=color,
        margin_bottom=margin_bottom,
        id=id,
        **kwargs,
    )
