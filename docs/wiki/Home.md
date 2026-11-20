**English** · [Dansk](Home-da) · [Bahasa Melayu](Home-ms)

# Cafe and Wifi website

A small website that lists cafes with wifi and power sockets for remote working. It is the solution to the day 88 assignment of the Udemy course "100 Days of Code: The Complete Python Pro Bootcamp". It needs only Python 3.13 or newer: no framework and no runtime dependency.

The site is built in three steps. Each step has a screenshot and a page that explains what the step taught.

| Step | What it adds | Page |
| --- | --- | --- |
| 1 | The home page lists all cafes of `cafes.db` | [Step 1: List the cafes](Step-1-List-Cafes) |
| 2 | A validated form adds a cafe | [Step 2: Add a cafe](Step-2-Add-Cafe) |
| 3 | A confirmation page deletes a cafe | [Step 3: Delete a cafe](Step-3-Delete-Cafe) |

The assignment asks for a reflection at the end; ours is on [Reflection](Reflection).

## Run it

```bash
python -m venv .venv
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
python -m cafe_wifi
```

Open <http://127.0.0.1:8000>. The README of the repository has the commands for Windows and Linux, for the tests and for the screenshots.
