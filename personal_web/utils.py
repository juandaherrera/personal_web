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


def hex_to_rgb(hex_value: str | Color, opacity: float | None = None) -> str:
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


def date_difference(start_date: date, end_date: date, is_lang_en: bool = False) -> str:  # noqa: C901, PLR0911, PLR0912
    # TODO(@juandaherrera): Refactor this function to make it more readable and maintainable
    # Suma un mes al final para cumplir con la regla
    adjusted_end_date = end_date + relativedelta(months=1)

    # Calcula la diferencia en años y meses
    diff = relativedelta(adjusted_end_date, start_date)
    years = diff.years
    months = diff.months

    # Formateo en inglés
    if is_lang_en:
        if years == 0 and months == 1:
            return "1 mo"
        elif years == 0:  # noqa: RET505
            return f"{months} mos"
        elif years == 1 and months == 0:
            return "1yr"
        elif years == 1:
            return f"1yr {months} mos"
        elif months == 1:
            return f"{years}yrs 1 mo"
        else:
            return f"{years}yrs {months} mos" if months else f"{years}yrs"

    # Formateo en español
    else:  # noqa: PLR5501
        if years == 0 and months == 1:
            return "1 mes"
        elif years == 0:  # noqa: RET505
            return f"{months} meses"
        elif years == 1 and months == 0:
            return "1 año"
        elif years == 1:
            return f"1 año y {months} meses"
        elif months == 1:
            return f"{years} años y 1 mes"
        else:
            return f"{years} años y {months} meses" if months else f"{years} años"


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
