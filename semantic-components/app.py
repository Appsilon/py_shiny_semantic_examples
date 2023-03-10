from shiny import App
from shiny.ui import tags

from shiny_semantic import page_semantic

import modules
from app_layout import header, hero, sidebar


app_ui = page_semantic(
    header(),
    sidebar(),
    tags.div(
        hero(),
        modules.button.ui("button_section"),
        modules.emoji.ui("emoji_section"),
        modules.flag.ui("flag_section"),
        modules.header.ui("header_section"),
        modules.icon.ui("icon_section"),
        modules.inputs.ui("input_section"),
        modules.modal.ui("modal_section"),
        modules.slider.ui("slider_section"),
        modules.dropdown.ui("dropdown_section"),
        modules.checkbox.ui("checkbox_section"),
        modules.statistic.ui("statistic_section"),
        tags.div(style="opacity: 0; height: 5rem;"),
    ),
    title="Shiny Semantic",
)


def app_server(input, output, session):
    modules.button.server("button_section")
    modules.emoji.server("emoji_section")
    modules.flag.server("flag_section")
    modules.header.server("header_section")
    modules.icon.server("icon_section")
    modules.inputs.server("input_section")
    modules.modal.server("modal_section")
    modules.slider.server("slider_section")
    modules.dropdown.server("dropdown_section")
    modules.checkbox.server("checkbox_section")
    modules.statistic.server("statistic_section")


app = App(app_ui, app_server)
