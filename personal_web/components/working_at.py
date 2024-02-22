import reflex as rx

from personal_web.styles.styles import Size


def working_at(image: str, url: str, alt: str) -> rx.Component:
    return rx.chakra.hstack(
        rx.chakra.text("En", font_size=[Size.DEFAULT_BIG.value, Size.BIG.value]),
        rx.chakra.link(
            rx.chakra.image(src=image, alt=alt, height=["2em", "2.5em"]),
            href=url,
            is_external=True,
            transition="transform 0.2s ease",
            _hover={
                "transform": "scale(1.1)",
            },
        ),
        padding_bottom=Size.DEFAULT_MEDIUM.value,
    )
