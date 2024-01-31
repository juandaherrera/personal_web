import reflex as rx

from personal_web.data.job import Job
from personal_web.styles.colors import Color, TextColor
from personal_web.styles.styles import Size

from .texts import title


# Añadir tecnologías usadas en el trabajo. Quizas usar badges con borders redondeados.
# Ejemplo: https://adriancecilia.dev/#projects
def work_experience(job: Job) -> rx.Component:
    return rx.accordion(
        rx.accordion_item(
            rx.accordion_button(_we_header(job)),
            rx.accordion_panel(_we_panel(job)),
            border_top_width=Size.ZERO.value,
            border_color=Color.SECONDARY.value,
        ),
        allow_toggle=True,
        width="100%",
    )


def _we_header(job: Job) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            # Logo compañía
            rx.center(
                rx.image(
                    src=job.company_logo,
                    alt=f"Logo de {job.company_name}",
                    height="2.5em",
                ),
                width="5.5em",
            ),
            # Divisor
            rx.center(
                rx.divider(
                    orientation="vertical",
                    border_color=TextColor.PRIMARY.value,
                ),
                height=Size.BIG.value,
            ),
            # Cargo
            rx.center(title(job.title, "lg"), text_align="left"),
            # Logo compañía
            rx.center(
                rx.accordion_icon(
                    font_size=Size.BIG.value,
                    _hover={
                        "color": Color.SECONDARY.value,
                        "text_shadow": f"0 0 8px {Color.PRIMARY.value}",
                    },
                )
            ),
            spacing=Size.DEFAULT_MEDIUM.value,
        ),
        # Fechas cargo
        rx.text(
            f"{job.start_date_format} - {job.end_date_format}",
            color=Color.SECONDARY.value,
        ),
        align_items="start",
    )


def _we_panel(job: Job) -> rx.Component:
    return rx.vstack(
        title("📋 Función principal", "md", padding_top=Size.DEFAULT.value),
        rx.text(
            job.description,
            text_align="justify",
            font_size=Size.DEFAULT_MEDIUM.value,
            padding_bottom=Size.DEFAULT.value,
        ),
        title("🏆 Logros", "md"),
        rx.text(
            job.achievements,
            text_align="justify",
            font_size=Size.DEFAULT_MEDIUM.value,
        ),
        align_items="start",
    )
