from datetime import date

import reflex as rx
import toml
from dateutil.relativedelta import relativedelta
from reflex.constants.colors import Color
from reflex.utils import console


def lang(language: bool = False) -> rx.Component:
    return rx.script(f"document.documentElement.lang='{language}'")


def get_experience() -> int:
    return date.today().year - 2021


def hex_to_rgb(hex_value: str | Color, opacity: float | None = None) -> str | Color:
    """Convert a hex_value color code to an RGB or RGBA string.

    Args:
        hex_value (str): The hex_value color code as a string, starting with '#'.
        opacity (Optional[float], optional): The opacity level as a float between 0 and 1.
            If not provided, the color will be opaque.

    Returns:
        str: The RGB or RGBA color string.

    Raises:
        ValueError: If `hex_value` is not in the form #RRGGBB.

    Examples:
        >>> hex_to_rgb("#FFFFFF")
        'rgb(255, 255, 255)'
        >>> hex_to_rgb("#FFFFFF", 0.5)
        'rgba(255, 255, 255, 0.5)'
    """
    if isinstance(hex_value, Color):
        return hex_value
    try:
        if len(hex_value) != 7 or hex_value[0] != "#":  # noqa: PLR2004
            raise ValueError("El código hexadecimal debe tener la forma #RRGGBB")

        hex_value = hex_value.lstrip("#")
        hex_tuple = tuple(int(hex_value[i : i + 2], 16) for i in (0, 2, 4))
        return (
            f"rgba({hex_tuple[0]}, {hex_tuple[1]}, {hex_tuple[2]}, {opacity})"
            if opacity
            else f"rgb({hex_tuple[0]}, {hex_tuple[1]}, {hex_tuple[2]})"
        )
    except Exception as e:
        console.warn(f"Error trying to convert hex color to RGB: {e}")
        return "rgb(255, 255, 255)"


def format_duration_en(years: int, months: int) -> str:
    """
    Formats a duration given in years and months into a human-readable string in English.

    Args:
        years (int): The number of years in the duration.
        months (int): The number of months in the duration.

    Returns:
        str: A formatted string representing the duration.
            The format varies based on the values of `years` and `months`
    """
    if years == 0:
        return "1 mo" if months == 1 else f"{months} mos"
    if years == 1:
        return "1yr" if months == 0 else f"1yr {months} mos" if months > 1 else "1yr 1 mo"
    if months == 0:
        return f"{years}yrs"
    return f"{years}yrs {months} mos" if months > 1 else f"{years}yrs 1 mo"


def format_duration_es(years: int, months: int) -> str:
    """
    Formats a duration in years and months into a human-readable string in Spanish.

    Args:
        years (int): The number of years in the duration.
        months (int): The number of months in the duration.

    Returns:
        str: A string representing the duration in Spanish. The format varies depending
            on the values of `years` and `months`
    """
    if years == 0:
        return "1 mes" if months == 1 else f"{months} meses"
    if years == 1:
        return (
            "1 año"
            if months == 0
            else f"1 año y {months} meses"
            if months > 1
            else "1 año y 1 mes"
        )
    if months == 0:
        return f"{years} años"
    return f"{years} años y {months} meses" if months > 1 else f"{years} años y 1 mes"


def date_difference(start_date: date, end_date: date, is_lang_en: bool = False) -> str:
    """
    Calculate the difference between two dates in terms of years and months,
    and return it as a formatted string in either English or Spanish.

    Args:
        start_date (date): The starting date of the range.
        end_date (date): The ending date of the range.
        is_lang_en (bool, optional): If True, the output will be formatted in English.
                                     If False, the output will be formatted in Spanish.
                                     Defaults to False.

    Returns:
        str: A formatted string representing the difference in years and months
             between the two dates.
    """
    end_date = end_date if end_date <= date.today() else date.today()
    adjusted_end_date = end_date + relativedelta(months=1)
    diff = relativedelta(adjusted_end_date.replace(day=1), start_date.replace(day=1))

    formatter = format_duration_en if is_lang_en else format_duration_es
    return formatter(diff.years, diff.months)


def get_version_from_toml(config_path: str = "pyproject.toml") -> str:
    """
    Get the version from the project configuration file.

    Parameters
    ----------
    config_path : str, optional
        Path of the configuration, by default "pyproject.toml"

    Returns
    -------
    str
        Version of the project.
    """
    with open(config_path, encoding="utf-8") as file:
        config = toml.load(file)
    return config["project"]["version"]


if __name__ == "__main__":
    start_date_1 = date(2023, 7, 10)
    end_date_1 = date(2024, 3, 20)
    print(date_difference(start_date_1, end_date_1, True))  # 9 mos  # noqa: T201
    print(date_difference(start_date_1, end_date_1, False))  # 9 meses # noqa: T201

    start_date_2 = date(2022, 6, 10)
    end_date_2 = date(2023, 7, 20)
    print(date_difference(start_date_2, end_date_2, True))  # 1yr 2 mos # noqa: T201

    start_date_3 = date(2023, 7, 10)
    end_date_3 = date(2023, 7, 11)
    print(date_difference(start_date_3, end_date_3, True))  # 1 mo # noqa: T201
    print(date_difference(start_date_3, end_date_3, False))  # 1 mes # noqa: T201
