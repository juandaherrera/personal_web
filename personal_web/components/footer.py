import datetime

import reflex as rx

import personal_web.constants as const
from personal_web.styles.colors import TextColor
from personal_web.styles.styles import Size


def footer() -> rx.Component:
    return rx.vstack(
        # rx.image(src="favicon.ico"),
        rx.link(
            f"© {datetime.date.today().year} by juandaherrera.",
            href=const.GUTHUB_URL,
            is_external=True,
            font_size=Size.DEFAULT.value,
        ),
        rx.text(
            "Built with ❤ from Palmira, Colombia.",
            font_size=Size.DEFAULT.value,
            margin_top=Size.ZERO.value,
        ),
        margin_bottom=Size.SMALL.value,
        padding_bottom=Size.SMALL.value,
        color=TextColor.SECONDARY.value,
    )
