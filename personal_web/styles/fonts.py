from enum import Enum


class Font(Enum):
    DEFAULT = "Poppins"
    JUANDAHERRERA = "Roboto Condensed, Poppins"


class FontSize(Enum):
    SUBTITLES = ["1.2em", "1.65em"]  # noqa: RUF012
    SECOND_SUBTITLE = ["1.05em", "1.25em"]  # noqa: RUF012
    BUTTON = ["1.15em", "1.40em"]  # noqa: RUF012
    BUTTON_ICONS = ["1.6em", "1.9em"]  # noqa: RUF012
    BODY = ["0.95em", "1.125em"]  # noqa: RUF012
    SMALL_TEXT = ["0.85em", "1em"]  # noqa: RUF012
    VERY_SMALL_TEXT = ["0.75em", "0.8em"]  # noqa: RUF012


class FontWeight(Enum):
    LIGHT = "300"
    MEDIUM = "500"
    JUANDAHERRERA = "400"
