import reflex as rx

import personal_web.styles.styles as styles
from personal_web.components.project import project_card
from personal_web.components.texts import title
from personal_web.data.project import projects_en_list, projects_list
from personal_web.styles.styles import Size


def projects(en: bool = False) -> rx.Component:
    selected_list = projects_list if not en else projects_en_list
    return rx.vstack(
        title("Projects 💻" if en else "Proyectos 💻"),
        rx.grid(
            *[project_card(project) for project in selected_list],
            columns=rx.breakpoints(
                initial="1",
                sm="2",
                md="3",
            ),
            spacing="6",
        ),
        align_items="start",
        spacing="6",
        style=styles.INDEX_SECTION_STYLE,
        id="projects",
    )
