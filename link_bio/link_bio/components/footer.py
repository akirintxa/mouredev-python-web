import reflex as rx
import datetime
import link_bio.constants as const
from link_bio.styles.styles import Size as Size
from link_bio.styles.colors import Color as Color
from link_bio.styles.colors import TextColor as TextColor


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="logo.png",
            height=Size.VERY_BIG.value
        ),
        rx.link(
            rx.box(
                f"© 2014-{datetime.date.today().year} ",
                rx.span("MoureDev by Brais Moure", color=Color.PRIMARY.value),
                " v3."
            ),
            href=const.MOUREDEV_URL,
            is_external=True,
            font_size=Size.MEDIUM.value
        ),
        rx.text(
            "BUILDING SOFTWARE WITH ♥ FROM GALICIA TO THE WORLD.",
            font_size=Size.MEDIUM.value,
            margin_top=Size.ZERO.value
        ),
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.BIG.value,
        spacing=Size.DEFAULT.value,
        color=TextColor.FOOTER.value
    )
