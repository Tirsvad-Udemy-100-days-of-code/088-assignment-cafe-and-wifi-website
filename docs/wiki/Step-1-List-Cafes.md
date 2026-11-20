**English** · [Dansk](Step-1-List-Cafes-da) · [Bahasa Melayu](Step-1-List-Cafes-ms)

# Step 1: List the cafes

The first step shows every cafe of the supplied database `cafes.db` on one web page.

![The list of cafes](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/088-assignment-cafe-and-wifi-website/raw/branch/main/docs/screenshots/step-1-list.png)

## What was built

- A `Cafe` record for one row of the `cafe` table.
- A repository with `get_all_cafes()` that reads the rows with `sqlite3`.
- A controller for `GET /` and a view that turns the cafes into HTML cards: image, name, location, map link, wifi, sockets, toilet, calls, seats and coffee price.
- A server started with `python -m cafe_wifi`, built on `wsgiref`, so nothing has to be installed.

## What we gained

- **Reading SQLite with the standard library.** `sqlite3` is enough for a read; the connection is closed by a context manager and every query is parameterised from the start.
- **Escaping output.** Every value that comes from the database is escaped before it is written into HTML, and only `http` and `https` links are used for `href` and `src`.
- **How a WSGI request works.** An application is a function that receives the request environment and returns a status, headers and a body. Frameworks such as Flask are built on exactly this.
- **Dirty data.** The pound sign in the prices was stored as a replacement character. The fix lives in one function with a test, and the database file is left untouched.
- **Layers.** Data access, rules and HTML are in separate packages, so each can be tested alone.

- **Where the pictures come from.** The images are links to other websites. The screenshot above was taken in a container without internet access, so the picture areas are grey; on your computer they load.

## Try it

```bash
python -m cafe_wifi
```

Open <http://127.0.0.1:8000>.
