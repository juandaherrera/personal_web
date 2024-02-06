from enum import Enum

import reflex as rx

from personal_web.utils import hex_to_rgb

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
    LARGE = "5em"


# Stylesheets
STYLESHEETS = [
    "/css/loop.css",
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css2?family=Roboto:wght@400&display=swap",
    "https://cdn.jsdelivr.net/gh/devicons/devicon@2.16.0/devicon.min.css",  # Lenguages Icons
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

INDEX_SECTION_STYLE = dict(
    width=["85%", "80%", "80%", "75%"],
    padding_x=Size.DEFAULT.value,
    padding_top=Size.VERY_BIG.value,
)

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
    padding_x=[Size.BIG.value, Size.MEDIUM_BIG.value],
    padding_y=Size.DEFAULT.value,
    z_index="999",
    top="0",
    width="100%",
)

MAIN_PIC_STYLE = dict(
    border=f"{Size.MEDIUM.value} solid {Color.PRIMARY.value}",
    padding=Size.DEFAULT.value,
    transition="transform 0.2s ease, box-shadow 0.3s ease",
    _hover={
        "transform": [
            "scale(1.05)",
            "scale(1.05)",
            "scale(1.05)",
            "scale(1.05)",
            "scale(1.035)",
        ],
        "border": f"{Size.MEDIUM.value} solid {Color.PRIMARY.value}",
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

TECH_STACK_ICON_STYLE = dict(
    font_size=Size.LARGE.value,
    padding_x=Size.MEDIUM.value,
)

TECH_STACK_STYLE = dict(
    transition="transform 0.2s ease, text-shadow 0.3s ease, color 0.5s ease",
    _hover={
        "color": Color.SECONDARY.value,
        "text_shadow": f"0 0 6px {Color.PRIMARY.value}",
        "transform": "scale(1.25)",
    },
)

TECH_BADGE_STYLE = dict(
    padding_y=Size.SMALL.value,
    padding_x=Size.DEFAULT.value,
    bg=hex_to_rgb(Color.AQUA.value, 0.15),
    color=Color.AQUA.value,
    border_radius="15px",
    font_size=Size.MEDIUM.value,
    font_weight="normal",
    text_transform="capitalize",
    margin_right=[Size.MEDIUM.value, Size.DEFAULT.value],
    margin_bottom=[Size.MEDIUM.value, Size.DEFAULT.value],
    transition="transform 0.18s ease",
    _hover={
        "transform": "scale(1.15)",
    },
)

PROJECT_CARD_STYLE = dict(
    color=TextColor.PRIMARY.value,
    margin_right=[
        Size.DEFAULT.value,
        Size.DEFAULT_BIG.value,
        "1.85em",
    ],
    margin_bottom=[
        Size.DEFAULT.value,
        Size.DEFAULT_BIG.value,
        "1.85em",
    ],
    background=hex_to_rgb(Color.CONTENT.value, 0.55),
    width=["17.5em", "20em"],
    transition="transform 0.3s ease, box-shadow 0.35s ease",
    _hover={
        "transform": ["scale(1.05)", "scale(1.05)", "scale(1.075)"],
        "box_shadow": f"0px 0px 20px {hex_to_rgb(Color.CONTENT.value, 0.3)}",
    },
)

EDUCATION_COLLEGE_LOGO_STYLE = dict(
    height="5em",
    aspect_ratio=1 / 1,
    transition="transform 0.18s ease",
    _hover={
        "transform": "scale(1.15)",
    },
)

FOOTER_LOGO_STYLE = dict(
    height=["3.5em", "4em"],
    margin_bottom=Size.ZERO.value,
    transition="transform 0.18s ease",
    _hover={
        "transform": "scale(1.2)",
    },
)

FOOTER_STYLE = dict(
    padding_top=Size.DEFAULT.value,
    padding_bottom=Size.SMALL.value,
    color=TextColor.SECONDARY.value,
)
