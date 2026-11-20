"""HTML views of the error pages.

@file error_views.py
@brief Pure functions that render a page for an error status.
"""

from html import escape

from cafe_wifi.presentation.views.cafe_views import render_page


## @brief Render an error page.
#  @param status Status line, for example "404 Not Found".
#  @param message Short explanation for the visitor.
#  @return The complete HTML document.
def render_error_page(status: str, message: str) -> str:
    """Return a page that shows the status and a message."""
    return render_page(status, "", f"<p>{escape(message)}</p>")
