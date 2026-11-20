"""HTML view of the add cafe form.

@file add_cafe_views.py
@brief A pure function that renders the form with values and errors, escaped.
"""

from collections.abc import Mapping
from html import escape

from cafe_wifi.constants import (
    ADD_PATH,
    ADD_SUBTITLE,
    BADGES,
    CHECKBOX_FIELDS,
    CHECKBOX_ON,
    FORM_TEXT_FIELDS,
    HOME_PATH,
    TEXT_BACK_LINK,
    TEXT_FACILITIES,
    TEXT_SUBMIT,
    TITLE_ADD,
)
from cafe_wifi.presentation.views.cafe_views import render_page

_CHECKBOX_LABELS = {attribute: label for label, attribute in BADGES}


def _render_error(errors: Mapping[str, str], field: str) -> str:
    """Return the error line of a field, or nothing when it is valid."""
    if field not in errors:
        return ""
    return f'<p class="error" id="error-{escape(field)}">{escape(errors[field])}</p>'


def _render_text_field(
    values: Mapping[str, str],
    errors: Mapping[str, str],
    field: str,
    label: str,
    max_length: int,
) -> str:
    """Return one labelled text input with its error."""
    state = " invalid" if field in errors else ""
    return (
        f'<div class="field{state}">'
        f'<label for="{escape(field)}">{escape(label)}</label>'
        f'<input type="text" id="{escape(field)}" name="{escape(field)}" '
        f'maxlength="{max_length}" value="{escape(values.get(field, ""))}">'
        f"{_render_error(errors, field)}</div>"
    )


def _render_checkbox(values: Mapping[str, str], field: str) -> str:
    """Return one labelled checkbox, checked when the value was sent."""
    checked = " checked" if values.get(field) == CHECKBOX_ON else ""
    return (
        f'<label><input type="checkbox" name="{escape(field)}" '
        f'value="{escape(CHECKBOX_ON)}"{checked}> '
        f"{escape(_CHECKBOX_LABELS[field])}</label>"
    )


## @brief Render the add cafe page.
#  @param values Entered values by field name, shown again in the inputs.
#  @param errors Error text by field name.
#  @return The complete HTML document, every value escaped.
def render_add_form(values: Mapping[str, str], errors: Mapping[str, str]) -> str:
    """Return the page with the form, the entered values and the field errors."""
    fields = "".join(
        _render_text_field(values, errors, field, label, max_length)
        for field, label, max_length in FORM_TEXT_FIELDS
    )
    checkboxes = "".join(_render_checkbox(values, field) for field in CHECKBOX_FIELDS)
    content = (
        f'<form class="form" method="post" action="{ADD_PATH}" novalidate>'
        f"{fields}"
        f"<fieldset><legend>{escape(TEXT_FACILITIES)}</legend>{checkboxes}</fieldset>"
        f'<button type="submit">{escape(TEXT_SUBMIT)}</button>'
        "</form>"
    )
    back = f'<a href="{HOME_PATH}">{escape(TEXT_BACK_LINK)}</a>'
    return render_page(TITLE_ADD, ADD_SUBTITLE, content, back)
