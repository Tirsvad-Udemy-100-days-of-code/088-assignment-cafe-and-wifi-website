"""Constants of the cafe and wifi website.

@file constants.py
@brief The single place for values that are used in more than one module.
"""

## @brief Name of the application, shown in the page title.
APP_NAME = "Cafe and Wifi"

## @brief Host the development server binds to by default.
DEFAULT_HOST = "127.0.0.1"

## @brief Port the development server listens on by default.
DEFAULT_PORT = 8000

## @brief Name of the environment variable that overrides the database path.
CAFE_WIFI_DB_ENV = "CAFE_WIFI_DB"

## @brief Database path used when the environment variable is not set,
#  relative to the repository root.
DEFAULT_DB_RELATIVE_PATH = "data/cafes.db"

## @brief Character the stored prices contain where a pound sign was lost.
PRICE_REPLACEMENT_CHARACTER = "\ufffd"

## @brief Currency sign shown in place of the replacement character.
PRICE_CURRENCY_SIGN = "\u00a3"

## @brief Path of the home page.
HOME_PATH = "/"

## @brief HTTP methods the site answers.
ALLOWED_METHODS = ("GET", "HEAD")

## @brief Value of the Allow header of a 405 response.
ALLOW_HEADER_VALUE = ", ".join(ALLOWED_METHODS)

## @brief Content type of every HTML response.
CONTENT_TYPE_HTML = "text/html; charset=utf-8"

## @brief Character encoding of every response body.
RESPONSE_ENCODING = "utf-8"

## @brief Status line of a successful response.
STATUS_OK = "200 OK"

## @brief Status line of an unknown path.
STATUS_NOT_FOUND = "404 Not Found"

## @brief Status line of a method the site does not accept.
STATUS_METHOD_NOT_ALLOWED = "405 Method Not Allowed"

## @brief URL schemes that may be used in a link or an image source.
SAFE_URL_SCHEMES = ("http", "https")

## @brief Label of the seats line on a cafe card.
LABEL_SEATS = "Seats"

## @brief Label of the price line on a cafe card.
LABEL_PRICE = "Coffee"

## @brief Label of the map link on a cafe card.
LABEL_MAP = "Map"

## @brief Text shown when a cafe has no seats or price on record.
TEXT_UNKNOWN = "n/a"

## @brief Text of the page shown when the database holds no cafes.
TEXT_NO_CAFES = "No cafes found."

## @brief Badge labels, in display order, with the Cafe attribute each one reads.
BADGES = (
    ("Wifi", "has_wifi"),
    ("Sockets", "has_sockets"),
    ("Toilet", "has_toilet"),
    ("Calls", "can_take_calls"),
)

## @brief Inline stylesheet of every page: a responsive card grid.
PAGE_CSS = """
*{box-sizing:border-box}
body{margin:0;font-family:system-ui,Segoe UI,Arial,sans-serif;background:#f4f1ec;
color:#2b2b2b;line-height:1.4}
header{background:#3b2a20;color:#fff;padding:1.5rem 2rem}
header h1{margin:0;font-size:1.8rem}
header p{margin:.25rem 0 0;color:#d8c9bd}
main{max-width:1200px;margin:0 auto;padding:1.5rem 2rem}
.grid{display:grid;gap:1.25rem;grid-template-columns:repeat(auto-fill,minmax(260px,1fr))}
.card{background:#fff;border-radius:10px;overflow:hidden;
box-shadow:0 1px 4px rgba(0,0,0,.15);display:flex;flex-direction:column}
.card img{width:100%;height:180px;object-fit:cover;background:#ddd}
.body{padding:1rem;display:flex;flex-direction:column;gap:.5rem}
.body h2{margin:0;font-size:1.15rem}
.location{margin:0;color:#6b5d52}
.badges{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:.4rem}
.badge{padding:.15rem .6rem;border-radius:999px;font-size:.8rem}
.badge.yes{background:#dff3e0;color:#1b5e20}
.badge.no{background:#eee;color:#757575;text-decoration:line-through}
.facts{margin:0;font-size:.95rem}
a{color:#8a4b1f}
@media (max-width:600px){main{padding:1rem}header{padding:1rem}}
"""

## @brief Page layout; $title, $css and $content are substituted.
PAGE_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>$title</title>
<style>$css</style>
</head>
<body>
<header><h1>$title</h1><p>$subtitle</p></header>
<main>
$content
</main>
</body>
</html>
"""

## @brief Subtitle shown under the title of the home page.
HOME_SUBTITLE = "Cafes with wifi and power sockets for remote working"

## @brief Message of the 404 page.
TEXT_NOT_FOUND = "Page not found."

## @brief Message of the 405 page.
TEXT_METHOD_NOT_ALLOWED = "Method not allowed."
