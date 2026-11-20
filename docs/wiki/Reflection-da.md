[English](Reflection) · **Dansk** · [Bahasa Melayu](Reflection-ms)

# Refleksion

Opgaven beder om en journal over, hvordan projektet blev grebet an. Det er vores.

## Hvordan vi greb det an

Vi planlagde, før vi kodede: en business case, de mennesker, der skulle bruge resultatet, en plan med fem milepæle og en opgaveliste. Derefter var hver milepæl en gren og en pull request, der blev gennemgået mod en tjekliste, før den blev flettet. Selve webstedet voksede i tre trin (vis, tilføj, slet), og hvert trin sluttede med tests, et skærmbillede og en wikiside.

## Hvad var let

- At læse data. `sqlite3` er i standardbiblioteket, og tabellen er lille og tydelig.
- Lag. Da den første brugssag havde sit lager, sin controller og sin visning, var de næste to trin små tilføjelser.

## Hvad var svært

- At klare sig uden framework. Routing, læsning af formularer og HTML-output er skrevet i hånden. Det er mere kode, men det viser, hvad et framework gør for dig.
- Beskidte data. Pundtegnet i priserne var gået tabt i databasefilen. Vi afkoder det ved læsning ét sted og lader filen være.
- At tage skærmbilleder uden at overtage skrivebordet. De tages i en Docker-container med en browser uden vindue. Containeren har ikke internet, så cafébillederne vises som grå felter.

## Største læring

En `GET`-forespørgsel må aldrig ændre noget, og hver værdi fra en bruger eller en database skal escapes, før den kommer i HTML. Begge dele er lette at gøre rigtigt fra start og svære at tilføje bagefter.

## Hvad vi ville gøre anderledes

- Tilføje redigering af en café og søgning på område og faciliteter.
- Lade skærmbilledcontaineren indlæse nogle lokale eksempelbilleder, så billederne vises.
- Tilføje et token til formularerne, så et andet websted ikke kan sende til dem.
