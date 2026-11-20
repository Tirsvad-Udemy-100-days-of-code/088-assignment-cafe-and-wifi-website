[English](Step-1-List-Cafes) · **Dansk** · [Bahasa Melayu](Step-1-List-Cafes-ms)

# Trin 1: Vis caféerne

Det første trin viser alle caféer fra den medfølgende database `cafes.db` på én webside.

![Listen over caféer](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/088-assignment-cafe-and-wifi-website/raw/branch/main/docs/screenshots/step-1-list.png)

## Hvad blev bygget

- En `Cafe`-post for én række i tabellen `cafe`.
- Et lager med `get_all_cafes()`, der læser rækkerne med `sqlite3`.
- En controller til `GET /` og en visning, der laver caféerne om til HTML-kort: billede, navn, sted, kortlink, wifi, stikkontakter, toilet, telefonopkald, siddepladser og kaffepris.
- En server, der startes med `python -m cafe_wifi` og bygger på `wsgiref`, så intet skal installeres.

## Hvad vi fik ud af det

- **At læse SQLite med standardbiblioteket.** `sqlite3` er nok til at læse; forbindelsen lukkes af en kontekstmanager, og alle forespørgsler bruger parametre fra start.
- **At escape output.** Alle værdier fra databasen escapes, før de skrives i HTML, og kun `http`- og `https`-links bruges i `href` og `src`.
- **Hvordan en WSGI-forespørgsel virker.** Et program er en funktion, der får forespørgslens miljø og returnerer status, headere og indhold. Frameworks som Flask bygger på netop det.
- **Beskidte data.** Pundtegnet i priserne var gemt som et erstatningstegn. Rettelsen ligger i én funktion med en test, og databasefilen er urørt.
- **Lag.** Dataadgang, regler og HTML ligger i hver sin pakke, så hvert lag kan testes alene.
- **Hvor billederne kommer fra.** Billederne er links til andre websteder. Skærmbilledet er taget i en container uden internet, så billedfladerne er grå; på din computer indlæses de.

## Prøv det

```bash
python -m cafe_wifi
```

Åbn <http://127.0.0.1:8000>.
