**English** · [Dansk](Reflection-da) · [Bahasa Melayu](Reflection-ms)

# Reflection

The assignment asks for a journal of how the project was approached. This is ours.

## How we approached it

We planned before coding: a business case, the people who would use the result, a plan with five milestones and a task list. Then each milestone was a branch and a pull request that was reviewed against a checklist before it was merged. The site itself grew in three steps (list, add, delete), and every step ended with tests, a screenshot and a wiki page.

## What was easy

- Reading the data. `sqlite3` is in the standard library, and the table is small and clear.
- Layers. Once the first use case had its repository, controller and view, the next two steps were small additions.

## What was hard

- Doing without a framework. Routing, form parsing and HTML output are written by hand. That is more code, but it shows what a framework does for you.
- Dirty data. The pound sign in the prices was lost in the database file. We decode it on read in one place and leave the file alone.
- Taking screenshots without taking over the desktop. They are taken in a Docker container with a headless browser. The container has no internet access, so the cafe pictures show as grey boxes.

## Biggest learning

A `GET` request must never change anything, and every value that comes from a user or a database must be escaped before it goes into HTML. Both are easy to get right at the start and hard to add later.

## What we would do differently

- Add editing of a cafe and a search by area and facilities.
- Let the screenshot container load a few local sample images, so the pictures show.
- Add a token to the forms so that another website cannot post to them.
