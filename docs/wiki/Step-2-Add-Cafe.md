**English** · [Dansk](Step-2-Add-Cafe-da) · [Bahasa Melayu](Step-2-Add-Cafe-ms)

# Step 2: Add a cafe

The second step lets a visitor add a cafe through a form.

![The add form](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/088-assignment-cafe-and-wifi-website/raw/branch/main/docs/screenshots/step-2-add-form.png)

When the input is wrong, the form is shown again with the problems and the values that were typed:

![The form with errors](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/088-assignment-cafe-and-wifi-website/raw/branch/main/docs/screenshots/step-2-add-errors.png)

## What was built

- `GET /add` shows an empty form; `POST /add` validates it and stores the cafe with `add_cafe()`.
- A pure validation function that returns a field error for each problem: name and location are required, the map and image links must be `http` or `https`, and no field is longer than the database column.
- A `NewCafe` record, a `DuplicateCafeError` for a name that already exists, and an `AddCafe` use case that turns that error into a message on the name field.
- A link "Add a cafe" in the page header.

## What we gained

- **Form handling.** A form is posted as `application/x-www-form-urlencoded`; the server reads a limited number of bytes and parses them with `urllib.parse`. A checkbox is only sent when it is ticked, so a missing field means "no".
- **Validation in one place.** The rules are a pure function in the domain layer, so they are tested without a server or a database.
- **Post, redirect, get.** After a successful post the server answers `303 See Other` and the browser loads the list. A reload then shows the list again and does not post the form twice.
- **Parameterised SQL.** Values are never glued into the SQL text. A test stores a name that looks like an SQL attack and checks that it is saved as plain text and the table is intact.
- **Using the database to guard a rule.** The unique name is enforced by the database; the repository translates its error into a domain error that the form can show.

## Try it

Start the site with `python -m cafe_wifi` and open <http://127.0.0.1:8000/add>.
