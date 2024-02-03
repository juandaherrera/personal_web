import reflex as rx

import personal_web.styles.styles as styles
from personal_web.components.texts import title
from personal_web.data.project import Project
from personal_web.styles.colors import Color, TextColor
from personal_web.styles.fonts import FontSize
from personal_web.styles.styles import Size

from .work_experience import tech_badge


def project_card(project: Project) -> rx.Component:
    return rx.card(
        _project_card_body(project.description, project.technologies),
        header=_project_card_header(project.name),
        footer=_project_card_footer(project.repository_url),
        style=styles.PROJECT_CARD_STYLE,
    )


def _project_card_body(description: str, technologies: list) -> rx.Component:
    return rx.vstack(
        rx.text(description),
        rx.cond(
            len(technologies) > 0,
            rx.flex(
                *[tech_badge(name) for name in technologies],
                padding_top=Size.DEFAULT_MEDIUM.value,
                padding_bottom=Size.ZERO.value,
                spacing=Size.DEFAULT_BIG.value,
                flex_wrap="wrap",
            ),
        ),
        align_items="start",
    )


def _project_card_header(name: str) -> rx.Component:
    return rx.flex(
        title(
            name,
            font_size=FontSize.SUBTITLES.value,
        ),
        rx.spacer(),
        rx.divider(
            border_color=Color.SECONDARY.value,
        ),
    )


def _project_card_footer(url: str) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.box(
                class_name="devicon-github-plain",
                font_size=FontSize.BUTTON_ICONS.value,
                transition="transform 0.18s ease, box-shadow 0.3s ease",
                _hover={
                    "color": Color.SECONDARY.value,
                    "transform": "scale(1.25)",
                },
            ),
            spacing=Size.SMALL.value,
            width="100%",
        ),
        width="100%",
        href=url,
        is_external=True,
    )
