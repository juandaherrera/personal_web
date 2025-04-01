import reflex as rx
from reflex.vars import Var


class TypeAnimation(rx.Component):
    """Texts that are written and erased dynamically."""

    library = "react-type-animation"
    tag = "TypeAnimation"
    sequence: Var[list]
    speed: Var[int] = 40
    repeat: Var[int | float] = 0
    cursor: Var[bool] = True


type_animation = TypeAnimation.create
