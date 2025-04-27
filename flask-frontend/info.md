# Flask Frontend – Technische Beschreibung

## Zweck

Das `flask-frontend` stellt eine einfache Web-Oberfläche bereit, über die Benutzer PlantUML-Code eingeben und ein SVG-Diagramm generieren können. Es ist ein typisches Flask-Frontend, das Benutzereingaben über ein HTML-Formular verarbeitet und die Darstellung des generierten SVG-Diagramms übernimmt.

## Hauptfunktionen

- HTML-Formular zur Eingabe von PlantUML-Code
- Unterstützung für initiale Inhalte via `init.puml`
- POST-Anfrage an den `plantuml-service` zur Diagrammerzeugung
- Darstellung des zurückgegebenen SVG im Browser

## Schnittstelle

### Route: `/` (GET/POST)
- **GET**: Lädt ein Formular mit initialem Inhalt aus `init.puml` (falls vorhanden).
- **POST**: Sendet den eingegebenen UML-Code an den PlantUML-Service und zeigt das generierte SVG-Diagramm an.

### Interner Aufruf:
```http
POST http://plantuml-service:8080/render
Content-Type: text/plain
Body: PlantUML-Text
```
## Abhängigkeiten

- Flask: Web-Framework
- requests: für HTTP-Kommunikation mit dem Backend-Service

## Deployment

Das Frontend läuft im eigenen Docker-Container und ist über http://localhost:5000 erreichbar (wenn docker-compose verwendet wird).

---