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

## @brief Path of the add cafe form.
ADD_PATH = "/add"

## @brief HTTP methods the home page answers.
ALLOWED_METHODS = ("GET", "HEAD")

## @brief Value of the Allow header of a 405 response for the home page.
ALLOW_HEADER_VALUE = ", ".join(ALLOWED_METHODS)

## @brief HTTP methods the add cafe form answers.
ADD_ALLOWED_METHODS = ("GET", "HEAD", "POST")

## @brief Value of the Allow header of a 405 response for the add cafe form.
ADD_ALLOW_HEADER_VALUE = ", ".join(ADD_ALLOWED_METHODS)

## @brief Largest request body in bytes the site reads (64 KiB).
MAX_BODY_BYTES = 64 * 1024

## @brief Largest number of fields a submitted form may hold.
MAX_FORM_FIELDS = 50

## @brief Name of the Location header.
HEADER_LOCATION = "Location"

## @brief Value a checked checkbox sends.
CHECKBOX_ON = "on"

## @brief Longest accepted name, location, seats and coffee price.
MAX_TEXT_LENGTH = 250

## @brief Longest accepted map and image address.
MAX_URL_LENGTH = 500

## @brief Name of the SQLite error a duplicate unique value raises.
SQLITE_UNIQUE_ERROR_NAME = "SQLITE_CONSTRAINT_UNIQUE"

## @brief Form field names, equal to the cafe attributes and table columns.
FIELD_NAME = "name"
FIELD_LOCATION = "location"
FIELD_MAP_URL = "map_url"
FIELD_IMG_URL = "img_url"
FIELD_SEATS = "seats"
FIELD_COFFEE_PRICE = "coffee_price"
FIELD_HAS_SOCKETS = "has_sockets"
FIELD_HAS_TOILET = "has_toilet"
FIELD_HAS_WIFI = "has_wifi"
FIELD_CAN_TAKE_CALLS = "can_take_calls"

## @brief Required text fields with their longest accepted length.
REQUIRED_TEXT_FIELDS = (
    (FIELD_NAME, MAX_TEXT_LENGTH),
    (FIELD_LOCATION, MAX_TEXT_LENGTH),
)

## @brief Required web address fields with their longest accepted length.
URL_FIELDS = (
    (FIELD_MAP_URL, MAX_URL_LENGTH),
    (FIELD_IMG_URL, MAX_URL_LENGTH),
)

## @brief Optional text fields with their longest accepted length.
OPTIONAL_TEXT_FIELDS = (
    (FIELD_SEATS, MAX_TEXT_LENGTH),
    (FIELD_COFFEE_PRICE, MAX_TEXT_LENGTH),
)

## @brief Checkbox fields, in form order.
CHECKBOX_FIELDS = (
    FIELD_HAS_WIFI,
    FIELD_HAS_SOCKETS,
    FIELD_HAS_TOILET,
    FIELD_CAN_TAKE_CALLS,
)

## @brief Text input fields of the form: name, label and maximum length.
FORM_TEXT_FIELDS = (
    (FIELD_NAME, "Name", MAX_TEXT_LENGTH),
    (FIELD_LOCATION, "Location", MAX_TEXT_LENGTH),
    (FIELD_MAP_URL, "Map URL", MAX_URL_LENGTH),
    (FIELD_IMG_URL, "Image URL", MAX_URL_LENGTH),
    (FIELD_SEATS, "Seats (optional)", MAX_TEXT_LENGTH),
    (FIELD_COFFEE_PRICE, "Coffee price (optional)", MAX_TEXT_LENGTH),
)

## @brief Error shown for a required field that is empty.
ERROR_REQUIRED = "This field is required."

## @brief Error shown for a value that is too long; $limit is substituted.
ERROR_TOO_LONG = "Use at most $limit characters."

## @brief Error shown for an address that is not http or https.
ERROR_URL = "Enter a web address starting with http:// or https://."

## @brief Error shown when the name is already stored.
ERROR_DUPLICATE_NAME = "A cafe with this name already exists"

## @brief Heading of the add cafe page.
TITLE_ADD = "Add a cafe"

## @brief Subtitle of the add cafe page.
ADD_SUBTITLE = "Share a place with wifi and power sockets"

## @brief Text of the link from the home page to the form.
TEXT_ADD_LINK = "Add a cafe"

## @brief Text of the link from the form back to the home page.
TEXT_BACK_LINK = "Back to the list"

## @brief Label of the submit button of the form.
TEXT_SUBMIT = "Add cafe"

## @brief Legend of the facilities group of the form.
TEXT_FACILITIES = "Facilities"

## @brief Content type of every HTML response.
CONTENT_TYPE_HTML = "text/html; charset=utf-8"

## @brief Character encoding of every response body.
RESPONSE_ENCODING = "utf-8"

## @brief Status line of a successful response.
STATUS_OK = "200 OK"

## @brief Status line of a successful submission, redirecting to the list.
STATUS_SEE_OTHER = "303 See Other"

## @brief Status line of a submission that failed validation.
STATUS_UNPROCESSABLE = "422 Unprocessable Content"

## @brief Status line of a body that cannot be read as a form.
STATUS_BAD_REQUEST = "400 Bad Request"

## @brief Status line of a body larger than the limit.
STATUS_CONTENT_TOO_LARGE = "413 Content Too Large"

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
header a{color:#f2d9bf;display:inline-block;margin-top:.75rem}
.form{max-width:640px;background:#fff;border-radius:10px;padding:1.5rem;
box-shadow:0 1px 4px rgba(0,0,0,.15);display:flex;flex-direction:column;gap:1rem}
.field{display:flex;flex-direction:column;gap:.25rem}
.field label{font-weight:600}
.field input[type=text]{padding:.5rem;border:1px solid #bbb;border-radius:6px;
font:inherit}
.field.invalid input[type=text]{border-color:#b3261e}
.error{margin:0;color:#b3261e;font-size:.9rem}
fieldset{border:1px solid #ddd;border-radius:6px;display:flex;flex-wrap:wrap;gap:1rem}
button{align-self:flex-start;padding:.6rem 1.4rem;border:0;border-radius:6px;
background:#8a4b1f;color:#fff;font:inherit;cursor:pointer}
@media (max-width:600px){main{padding:1rem}header{padding:1rem}}
"""

## @brief Page layout; $title, $subtitle, $actions, $css and $content are
#  substituted.
PAGE_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>$title</title>
<style>$css</style>
</head>
<body>
<header><h1>$title</h1><p>$subtitle</p>$actions</header>
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

## @brief Message of the 400 page.
TEXT_BAD_REQUEST = "The form could not be read."

## @brief Message of the 413 page.
TEXT_CONTENT_TOO_LARGE = "The form is too large."

## @brief Message of the 405 page.
TEXT_METHOD_NOT_ALLOWED = "Method not allowed."
