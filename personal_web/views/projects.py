import reflex as rx

import personal_web.styles.styles as styles
from personal_web.components.project import project_card
from personal_web.components.texts import title
from personal_web.data.project import projects_list
from personal_web.styles.styles import Size


def projects() -> rx.Component:
    return rx.vstack(
        title("Proyectos 💻"),
        rx.flex(
            *[project_card(project) for project in projects_list],
            flex_wrap="wrap",
        ),
        align_items="start",
        spacing=Size.DEFAULT_BIG.value,
        style=styles.INDEX_SECTION_STYLE,
    )
