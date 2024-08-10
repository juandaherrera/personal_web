import reflex as rx

import personal_web.styles.styles as styles
from personal_web.components.certification import certification
from personal_web.components.texts import title
from personal_web.data.certification import certifications_list
from personal_web.styles.styles import Size


def certifications() -> rx.Component:
    return rx.vstack(
        title("Certificaciones 📃"),
        rx.flex(
            *[certification(item) for item in certifications_list],
            width="100%",
            spacing="9",
            flex_wrap="wrap",
        ),
        align_items="start",
        spacing=Size.DEFAULT_BIG.value,
        style=styles.INDEX_SECTION_STYLE,
        padding_top=Size.LARGE.value,
        id="certifications",
    )
