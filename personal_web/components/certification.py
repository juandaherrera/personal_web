import reflex as rx

from personal_web.components.texts import title
from personal_web.data.certification import Certification
from personal_web.styles.colors import Color, TextColor
from personal_web.styles.fonts import FontSize
from personal_web.styles.styles import EDUCATION_COLLEGE_LOGO_STYLE, Size

from .buttons import rounded_button


def certification(certification: Certification) -> rx.Component:
    return rx.hstack(
        rx.center(
            rx.image(
                src=certification.institute_logo,
                alt=f"Logo de {certification.institute}",
                style=EDUCATION_COLLEGE_LOGO_STYLE,
            ),
        ),
        rx.vstack(
            title(
                certification.title,
                size="6",
                margin_bottom=Size.ZERO.value,
            ),
            rx.hstack(
                rx.vstack(
                    rx.text(
                        certification.institute,
                        font_size=FontSize.BODY.value,
                        color=Color.SECONDARY.value,
                    ),
                    rx.text(
                        certification.period,
                        font_size=FontSize.SMALL_TEXT.value,
                    ),
                    align_items="start",
                    spacing="0",
                ),
                rx.cond(
                    certification.credential_url != '/',
                    rx.chakra.divider(
                        orientation="vertical",
                        border_color=TextColor.PRIMARY.value,
                        height=Size.BIG.value,
                    ),
                ),
                rx.cond(
                    certification.credential_url != '/',
                    rounded_button(
                        "Credencial",
                        url=certification.credential_url,
                        text_size=FontSize.VERY_SMALL_TEXT.value,
                    ),
                ),
                spacing=Size.DEFAULT.value,
                align="center",
            ),
            align="start",
            spacing="1",
            max_width=["90%", "85%", "80%", "80%", "75%"],
        ),
        align="center",
        spacing=Size.DEFAULT.value,
    )
