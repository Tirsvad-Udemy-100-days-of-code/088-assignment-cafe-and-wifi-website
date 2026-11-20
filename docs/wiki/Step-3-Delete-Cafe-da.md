[English](Step-3-Delete-Cafe) · **Dansk** · [Bahasa Melayu](Step-3-Delete-Cafe-ms)

# Trin 3: Slet en café

Det tredje trin lader en besøgende fjerne en café efter en bekræftelse.

![Bekræftelse af sletning](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/088-assignment-cafe-and-wifi-website/raw/branch/main/docs/screenshots/step-3-delete-confirm.png)

## Hvad blev bygget

- Hvert cafékort har et "Delete"-link til `/delete/<id>`.
- `GET /delete/<id>` viser en side, der nævner caféen og beder om bekræftelse; `POST /delete/<id>` fjerner caféen med `delete_cafe()` og sender den besøgende tilbage til listen.
- Et id, der ikke findes eller ikke er et helt tal, giver siden "ikke fundet" og ændrer intet.

## Hvad vi fik ud af det

- **Sikre og usikre metoder.** En `GET`-forespørgsel må aldrig ændre data, fordi browsere, søgemaskiner og linkvisninger kalder den frit. Kun `POST` sletter, og en test kalder slet-adressen med `GET` flere gange for at bevise det.
- **Bekræftelse.** En handling, der ikke kan fortrydes, får sin egen side med navnet på det, der fjernes, og en vej til at annullere.
- **Streng routing.** Ruten accepterer kun cifre (`/delete/42`). Alt andet, som `/delete/abc` eller `/delete/1/2`, giver 404, så mærkelige input aldrig når databasen.
- **"Ikke fundet" er et resultat, ikke et nedbrud.** Lageret svarer "intet blev slettet" med `False`, og controlleren gør det til en 404-side.
- **Gjort lagdelt.** Den nye regel krævede én metode i lageret, én brugssag og én controller-rute; intet andet skulle ændres.

## Prøv det

Start webstedet med `python -m cafe_wifi` og klik på "Delete" ved en café.
