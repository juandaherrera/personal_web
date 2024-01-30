from enum import Enum

import reflex as rx

from .colors import Color, TextColor
from .fonts import Font, FontWeight


# Sizes
class Size(Enum):
    ZERO = "0px !important"
    VERY_SMALL = "0.3em"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    DEFAULT_MEDIUM = "1.125em"
    DEFAULT_BIG = "1.5em"
    BIG = "2em"
    MEDIUM_BIG = "3em"
    VERY_BIG = "4em"


# Stylesheets
STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css2?family=Roboto:wght@400&display=swap",
    "https://cdn.jsdelivr.net/gh/devicons/devicon@v2.15.1/devicon.min.css",  # Lenguages Icons
]

# Styles
BASE_STYLE = {
    "background_color": Color.BACKGROUND.value,
    "font_family": Font.DEFAULT.value,
    "font_weight": FontWeight.LIGHT.value,
    "color": TextColor.PRIMARY.value,
    "scroll_behavior": "smooth",
    rx.Link: {"text_decoration": "none", "_hover": {}},
}

DEFAULT_BUTTON_STYLE = dict(
    background_color="transparent",
    border=f"{Size.VERY_SMALL.value} solid",
    padding_y=Size.DEFAULT_BIG.value,
)

NAVBAR_TITLE_STYLE = dict(
    font_size=Size.BIG.value,
    font_family=Font.JUANDAHERRERA.value,
    font_weight=FontWeight.JUANDAHERRERA.value,
)

NAVBAR_STYLE = dict(
    position="sticky",
    bg=Color.CONTENT.value,
    padding_x=Size.BIG.value,
    padding_y=Size.DEFAULT.value,
    z_index="999",
    top="0",
    width="100%",
)

MAIN_PIC_STYLE = dict(
    max_width=["20em", "30em", "43em"],
    border_radius="50%",
    padding="0.6em",
    border=f"{Size.SMALL.value} solid {Color.PRIMARY.value}",
    _hover={
        "border": f"{Size.SMALL.value} solid {Color.PRIMARY.value}",
        "box_shadow": f"0 0 8px {Color.PRIMARY.value}, 0 0 12px {Color.PRIMARY.value}",
    },
)

PRESENTATION_STACK_STYLE = dict(
    align_items="center",
    width="100%",
    background=Color.BACKGROUND_ALT.value,
    box_shadow=f"0 0 {Size.DEFAULT_BIG.value} {Color.CONTENT.value}",
    margin_top=Size.ZERO.value,
    padding_y=Size.DEFAULT_BIG.value,
)
