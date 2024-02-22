import reflex as rx

import personal_web.styles.styles as styles
from personal_web.data.job import Job
from personal_web.styles.colors import Color, TextColor
from personal_web.styles.fonts import FontSize
from personal_web.styles.styles import Size

from .texts import title


def work_experience(job: Job) -> rx.Component:
    return rx.chakra.accordion(
        rx.chakra.accordion_item(
            rx.chakra.accordion_button(_we_header(job), _hover={}),
            rx.chakra.accordion_panel(_we_panel(job)),
            border_top_width=Size.ZERO.value,
            border_color=Color.SECONDARY.value,
        ),
        allow_toggle=True,
        width="100%",
    )


def _we_header(job: Job) -> rx.Component:
    return rx.chakra.hstack(
        rx.chakra.vstack(
            rx.chakra.hstack(
                # Logo compañía
                rx.chakra.center(
                    rx.chakra.image(
                        src=job.company_logo,
                        alt=f"Logo de {job.company_name}",
                        height="2.5em",
                        aspect_ratio=2 / 1,
                    ),
                    width=["4em", "5.5em"],
                ),
                # Divisor
                rx.chakra.center(
                    rx.chakra.divider(
                        orientation="vertical",
                        border_color=TextColor.PRIMARY.value,
                    ),
                    height=Size.BIG.value,
                ),
                # Cargo
                rx.chakra.center(
                    title(job.title, font_size=FontSize.SUBTITLES.value),
                    text_align="left",
                ),
                spacing=Size.DEFAULT_MEDIUM.value,
            ),
            # Fechas cargo
            rx.chakra.text(
                rx.chakra.span(
                    f"{job.start_date_format} - {job.end_date_format}",
                    color=Color.SECONDARY.value,
                ),
                rx.chakra.span(
                    f" · {job.calculate_duration()}",
                    color=Color.TERTIARY.value,
                ),
                text_align="left",
                font_size=FontSize.SMALL_TEXT.value,
            ),
            align_items="start",
        ),
        rx.chakra.spacer(),
        # Ícono de acordión
        rx.chakra.center(
            rx.chakra.accordion_icon(
                font_size=Size.BIG.value, style=styles.ACCORDION_ICON_STYLE
            )
        ),
        width="100%",
    )


def _we_panel(job: Job) -> rx.Component:
    return rx.chakra.vstack(
        title(
            "📋 Función principal",
            font_size=FontSize.SECOND_SUBTITLE.value,
            padding_top=Size.DEFAULT.value,
        ),
        rx.chakra.text(
            job.description,
            text_align="justify",
            font_size=FontSize.BODY.value,
            padding_bottom=Size.DEFAULT.value,
        ),
        title("🏆 Logros", font_size=FontSize.SECOND_SUBTITLE.value),
        rx.chakra.text(
            job.achievements,
            text_align="justify",
            font_size=FontSize.BODY.value,
        ),
        rx.cond(
            len(job.technologies) > 0,
            rx.chakra.flex(
                *[tech_badge(name) for name in job.technologies],
                padding_top=Size.DEFAULT_MEDIUM.value,
                padding_bottom=Size.ZERO.value,
                spacing=Size.DEFAULT_BIG.value,
                flex_wrap="wrap",
            ),
        ),
        align_items="start",
    )


def tech_badge(tech_name: str) -> rx.Component:
    return rx.chakra.badge(tech_name, style=styles.TECH_BADGE_STYLE)
