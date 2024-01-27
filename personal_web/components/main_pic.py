import reflex as rx

import personal_web.styles.styles as styles
from personal_web.styles.styles import Size


def main_pic(image: str) -> rx.Component:
    return rx.image(src=image, style=styles.MAIN_PIC_STYLE)
