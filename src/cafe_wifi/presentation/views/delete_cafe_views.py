"""HTML view of the delete confirmation page.

@file delete_cafe_views.py
@brief A pure function that names the cafe to delete, escaped.
"""

from html import escape
from string import Template

from cafe_wifi.constants import (
    DELETE_PATH_PREFIX,
    DELETE_QUESTION,
    DELETE_WARNING,
    HOME_PATH,
    TEXT_BACK_LINK,
    TEXT_CANCEL,
    TEXT_DELETE,
    TITLE_DELETE,
)
from cafe_wifi.domain.entities.cafe import Cafe
from cafe_wifi.presentation.views.cafe_views import render_page


## @brief Render the page that asks the visitor to confirm a deletion.
#  @param cafe The cafe that would be deleted.
#  @return The complete HTML document; the form posts to the delete path.
def render_delete_confirmation(cafe: Cafe) -> str:
    """Return the page with the question, a Delete button and a Cancel link."""
    question = Template(DELETE_QUESTION).substitute(
        name=f"<strong>{escape(cafe.name)}</strong>"
    )
    content = (
        f'<form class="confirm" method="post" action="{DELETE_PATH_PREFIX}{cafe.id}">'
        f"<p>{question}</p>"
        f"<p>{escape(DELETE_WARNING)}</p>"
        '<div class="actions">'
        f'<button type="submit" class="danger">{escape(TEXT_DELETE)}</button>'
        f'<a href="{HOME_PATH}">{escape(TEXT_CANCEL)}</a>'
        "</div></form>"
    )
    back = f'<a href="{HOME_PATH}">{escape(TEXT_BACK_LINK)}</a>'
    return render_page(TITLE_DELETE, "", content, back)
