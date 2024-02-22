import reflex as rx

import personal_web.styles.styles as styles
from personal_web.components.certification import certification
from personal_web.components.texts import title
from personal_web.data.certification import certifications_list
from personal_web.styles.styles import Size


def certifications() -> rx.Component:
    return rx.chakra.vstack(
        title("Certificaciones 📃"),
        rx.chakra.responsive_grid(
            *[certification(item) for item in certifications_list],
            columns=[1, 1, 2, 2, 3],
            spacing_x=Size.DEFAULT_BIG.value,
            spacing_y=Size.MEDIUM_BIG.value
        ),
        align_items="start",
        spacing=Size.DEFAULT_BIG.value,
        style=styles.INDEX_SECTION_STYLE,
        padding_top=Size.LARGE.value,
        id="certifications",
    )
