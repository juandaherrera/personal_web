import reflex as rx

from personal_web.styles.colors import Color, TextColor
from personal_web.utils import hex_to_rgb

FEEDBACK_A = """
Juan David is one of the most capable and well-rounded data professionals I’ve had the chance to work with. His ability to design scalable, automated solutions and to model complex operational challenges is truly outstanding.
"""


def bento_card() -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.hstack(
                rx.flex(
                    rx.icon("user-round", size=100),  # type: ignore
                    align="center",
                    justify="center",
                    height="100%",
                ),
                rx.vstack(
                    rx.text(FEEDBACK_A),
                ),
                width="100%",
                height="100%",
                spacing="5",
                align="center",
            ),
            rx.hstack(
                rx.vstack(
                    rx.text(
                        "Abraham Farfán",
                        # font_weight="bold",
                        font_size="1.2em",
                        color=Color.SECONDARY.value,
                        width="100%",
                        align="right",
                        justify="right",
                    ),
                    rx.text(
                        "2025 - We worked together at Rappi",
                        color=TextColor.PRIMARY.value,
                        width="100%",
                        align="right",
                        justify="right",
                    ),
                    margin_bottom="0.75em",
                    justify="end",
                    align="end",
                    spacing="0",
                    width="100%",
                    height="100%",
                ),
                rx.vstack(
                    rx.image(
                        src="/icons/rappi_mustache.svg",
                        alt="Rappi",
                        width=rx.breakpoints(
                            initial="2em",
                            md="2em",
                            lg="3em",
                        ),
                        height=rx.breakpoints(
                            initial="2em",
                            md="2em",
                            lg="3em",
                        ),
                    ),
                    rx.icon("quote", size=50, color=Color.SECONDARY.value),  # type: ignore
                    spacing="1",
                    justify="end",  # Alinea horizontalmente al final (derecha)
                    align="end",  # Alinea verticalmente al final (abajo)
                    height="100%",
                ),
                spacing="5",
                width="100%",  # Asegura que el flex tome todo el ancho
                height="100%",
            ),
            width="100%",
            height="100%",
        ),
        padding="1.3em",
        width="100%",
        transition="transform 0.3s ease, box-shadow 0.35s ease",
        _hover={
            "transform": "scale(1.03)",
            "box_shadow": f"0px 0px 20px {hex_to_rgb(Color.CONTENT.value, 0.3)}",
        },
        border="0px",
    )
