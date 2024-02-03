from enum import Enum


class Font(Enum):
    DEFAULT = "Poppins"
    JUANDAHERRERA = "Roboto Condensed, Poppins"


class FontSize(Enum):
    SUBTITLES = ["1.2em", "1.65em"]
    SECOND_SUBTITLE = ["1.05em", "1.25em"]
    BUTTON = ["1.15em", "1.40em"]
    BUTTON_ICONS = ["1.6em", "1.9em"]
    BODY = ["0.95em", "1.125em"]
    SMALL_TEXT = ["0.85em", "1em"]


class FontWeight(Enum):
    LIGHT = "300"
    MEDIUM = "500"
    JUANDAHERRERA = "400"
