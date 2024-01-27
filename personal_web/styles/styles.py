from enum import Enum

from .colors import Color, TextColor


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


# Styles
BASE_STYLE = {
    "background_color": Color.BACKGROUND.value,
    "color": TextColor.PRIMARY.value,
}

DEFAULT_BUTTON_STYLE = dict()

NAVBAR_TITLE_STYLE = dict(font_size=Size.BIG.value)

MAIN_PIC_STYLE = dict(
    max_width="43em",
    border_radius="50%",
    padding="0.6em",
    border=f"{Size.SMALL.value} solid {Color.PRIMARY.value}",
    _hover={
        "border": f"{Size.SMALL.value} solid {Color.PRIMARY.value}",
        "box_shadow": f"0 0 8px {Color.PRIMARY.value}, 0 0 12px {Color.PRIMARY.value}",
    },
)
