**English** · [Dansk](Step-3-Delete-Cafe-da) · [Bahasa Melayu](Step-3-Delete-Cafe-ms)

# Step 3: Delete a cafe

The third step lets a visitor remove a cafe, after a confirmation.

![The delete confirmation](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/088-assignment-cafe-and-wifi-website/raw/branch/main/docs/screenshots/step-3-delete-confirm.png)

## What was built

- Every cafe card has a "Delete" link to `/delete/<id>`.
- `GET /delete/<id>` shows a page that names the cafe and asks for confirmation; `POST /delete/<id>` removes the cafe with `delete_cafe()` and sends the visitor back to the list.
- An id that does not exist, or is not a whole number, gives the "not found" page and changes nothing.

## What we gained

- **Safe and unsafe methods.** A `GET` request must never change data, because browsers, search engines and link previews call it freely. Only `POST` deletes, and a test calls the delete address with `GET` several times to prove it.
- **Confirmation.** A destructive action gets its own page with the name of the thing that will be removed, and a way to cancel.
- **Strict routing.** The route accepts only digits (`/delete/42`). Anything else, such as `/delete/abc` or `/delete/1/2`, is a 404, so no odd input reaches the database.
- **Not found is a result, not a crash.** The repository answers "nothing was deleted" with `False`, and the controller turns that into a 404 page.
- **Done the layered way.** The new rule needed one method in the repository, one use case and one controller route; nothing else had to change.

## Try it

Start the site with `python -m cafe_wifi`, then click "Delete" on a cafe.
