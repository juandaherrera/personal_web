import reflex as rx

from personal_web.styles.colors import TextColor
from personal_web.styles.styles import Size


def title(
    text: str,
    size: str = "8",
    color: str = TextColor.PRIMARY.value,
    id: str | None = None,  # noqa: A002
    margin_bottom: str = Size.VERY_SMALL.value,
    **kwargs,
) -> rx.Component:
    return rx.heading(
        text,
        size=size,
        color=color,
        margin_bottom=margin_bottom,
        id=id,
        **kwargs,
    )
