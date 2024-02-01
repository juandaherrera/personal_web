import datetime
from typing import Optional

import reflex as rx


def lang(language: str = "es") -> rx.Component:
    return rx.script(f"document.documentElement.lang='{language}'")


def get_experience() -> int:
    return datetime.date.today().year - 2021


def hex_to_rgb(hex: str, opacity: Optional[float] = None) -> str:
    """Convert a hex color code to an RGB or RGBA string.

    Args:
        hex (str): The hex color code as a string, starting with '#'.
        opacity (Optional[float], optional): The opacity level as a float between 0 and 1.
            If not provided, the color will be opaque.

    Returns:
        str: The RGB or RGBA color string.

    Raises:
        ValueError: If `hex` is not in the form #RRGGBB.

    Examples:
        >>> hex_to_rgb("#FFFFFF")
        'rgb(255, 255, 255)'
        >>> hex_to_rgb("#FFFFFF", 0.5)
        'rgba(255, 255, 255, 0.5)'
    """
    if len(hex) != 7 or hex[0] != '#':
        raise ValueError("El código hexadecimal debe tener la forma #RRGGBB")

    hex = hex.lstrip("#")
    hex_tuple = tuple(int(hex[i : i + 2], 16) for i in (0, 2, 4))
    return (
        f"rgba({hex_tuple[0]}, {hex_tuple[1]}, {hex_tuple[2]}, {opacity})"
        if opacity
        else f"rgb({hex_tuple[0]}, {hex_tuple[1]}, {hex_tuple[2]})"
    )
