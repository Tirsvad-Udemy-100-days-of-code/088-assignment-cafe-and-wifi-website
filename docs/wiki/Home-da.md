[English](Home) · **Dansk** · [Bahasa Melayu](Home-ms)

# Cafe og Wifi-websted

Et lille websted, der viser caféer med wifi og stikkontakter til fjernarbejde. Det er løsningen på opgaven fra dag 88 i Udemy-kurset "100 Days of Code: The Complete Python Pro Bootcamp". Det kræver kun Python 3.13 eller nyere: ingen framework og ingen afhængigheder ved kørsel.

Webstedet bygges i tre trin. Hvert trin har et skærmbillede og en side, der forklarer, hvad trinnet lærte os.

| Trin | Hvad det tilføjer | Side |
| --- | --- | --- |
| 1 | Forsiden viser alle caféer i `cafes.db` | [Trin 1: Vis caféerne](Step-1-List-Cafes-da) |
| 2 | En formular med kontrol tilføjer en café | [Trin 2: Tilføj en café](Step-2-Add-Cafe-da) |
| 3 | En bekræftelsesside sletter en café | [Trin 3: Slet en café](Step-3-Delete-Cafe-da) |

Opgaven beder om en refleksion til sidst; vores står på [Refleksion](Reflection-da).

## Kør det

```bash
python -m venv .venv
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
python -m cafe_wifi
```

Åbn <http://127.0.0.1:8000>. Repositoriets README har kommandoerne til Windows og Linux, til testene og til skærmbillederne.
