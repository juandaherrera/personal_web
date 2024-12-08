import reflex as rx
import reflex_chakra as rxc

import personal_web.styles.styles as styles
from personal_web.components.texts import title
from personal_web.data.project import Project
from personal_web.styles.colors import Color, TextColor
from personal_web.styles.fonts import FontSize
from personal_web.styles.styles import Size

from .work_experience import tech_badge


def project_card(project: Project) -> rx.Component:
    return rxc.card(
        _project_card_body(project.description, project.technologies),
        header=_project_card_header(project.name),
        footer=_project_card_footer(project.repository_url, project.website_url),
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
                spacing="0",
                flex_wrap="wrap",
            ),
        ),
        spacing="2",
        align_items="start",
    )


def _project_card_header(name: str) -> rx.Component:
    return rx.flex(
        title(
            name,
            size="6",
        ),
        rx.spacer(),
        rxc.divider(
            border_color=Color.SECONDARY.value,
        ),
        align="start",
    )


def _project_card_footer(
    github_url: str, website_url: str = "/", website_icon: str = "chrome"
) -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.box(
                class_name="devicon-github-plain",
                font_size=FontSize.BUTTON_ICONS.value,
                transition="transform 0.18s ease",
                _hover={
                    "color": Color.SECONDARY.value,
                    "transform": "scale(1.25)",
                },
            ),
            color="inherit",
            href=github_url,
            is_external=True,
        ),
        rx.cond(
            website_url != "/",
            rx.link(
                rx.box(
                    class_name=f"devicon-{website_icon}-plain",
                    font_size=FontSize.BUTTON_ICONS.value,
                    transition="transform 0.18s ease",
                    _hover={
                        "color": Color.SECONDARY.value,
                        "transform": "scale(1.25)",
                    },
                ),
                color="inherit",
                href=website_url,
                is_external=True,
            ),
        ),
        spacing="2",
        width="100%",
    )
