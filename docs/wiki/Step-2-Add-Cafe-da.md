[English](Step-2-Add-Cafe) · **Dansk** · [Bahasa Melayu](Step-2-Add-Cafe-ms)

# Trin 2: Tilføj en café

Det andet trin lader en besøgende tilføje en café med en formular.

![Formularen](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/088-assignment-cafe-and-wifi-website/raw/branch/main/docs/screenshots/step-2-add-form.png)

Når indtastningen er forkert, vises formularen igen med fejlene og de værdier, der blev skrevet:

![Formularen med fejl](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/088-assignment-cafe-and-wifi-website/raw/branch/main/docs/screenshots/step-2-add-errors.png)

## Hvad blev bygget

- `GET /add` viser en tom formular; `POST /add` kontrollerer den og gemmer caféen med `add_cafe()`.
- En ren kontrolfunktion, der giver en fejl pr. felt: navn og sted er påkrævet, kort- og billedlink skal være `http` eller `https`, og intet felt er længere end databasekolonnen.
- En `NewCafe`-post, en `DuplicateCafeError` for et navn, der findes i forvejen, og en `AddCafe`-brugssag, der gør fejlen til en besked ved navnefeltet.
- Et link "Add a cafe" i sidehovedet.

## Hvad vi fik ud af det

- **Formularhåndtering.** En formular sendes som `application/x-www-form-urlencoded`; serveren læser et begrænset antal bytes og læser dem med `urllib.parse`. Et afkrydsningsfelt sendes kun, når det er afkrydset, så et manglende felt betyder "nej".
- **Kontrol ét sted.** Reglerne er en ren funktion i domænelaget og testes uden server og database.
- **Post, redirect, get.** Efter en vellykket post svarer serveren `303 See Other`, og browseren henter listen. En genindlæsning viser listen igen og sender ikke formularen to gange.
- **Parametriseret SQL.** Værdier klistres aldrig ind i SQL-teksten. En test gemmer et navn, der ligner et SQL-angreb, og tjekker, at det gemmes som almindelig tekst, og at tabellen er intakt.
- **Databasen som vagt for en regel.** Det unikke navn håndhæves af databasen; lageret oversætter fejlen til en domænefejl, som formularen kan vise.

## Prøv det

Start webstedet med `python -m cafe_wifi` og åbn <http://127.0.0.1:8000/add>.
