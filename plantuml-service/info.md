# PlantUML Service – Technische Beschreibung

## Zweck

Der `plantuml-service` ist ein einfacher REST-Service, der PlantUML-Code entgegennimmt, diesen mit `plantuml.jar` rendert und das resultierende SVG-Bild zurückgibt. Er wird vom Frontend über eine HTTP-Schnittstelle angesprochen.

## Hauptfunktionen

- Entgegennahme von PlantUML-Code über eine HTTP-POST-Anfrage
- Speicherung des Codes als temporäre `.puml`-Datei
- Aufruf von `java -jar plantuml.jar` zur SVG-Erzeugung
- Rückgabe des gerenderten SVG-Bildes als HTTP-Antwort

## Schnittstelle

### Endpoint: `/render` (POST)
- **Request Body**: PlantUML-Quellcode als `text/plain`
- **Response**: `image/svg+xml`, das generierte Diagramm

### Beispiel:

```http
POST /render
Content-Type: text/plain

@startuml
Alice -> Bob: Hello
@enduml
``` 
Antwort: SVG-Diagramm

## Abhängigkeiten

- Flask: Web-Framework
- subprocess, tempfile: zur sicheren temporären Verarbeitung
- plantuml.jar und Java-Laufzeitumgebung

## Deployment

Läuft in einem eigenen Docker-Container unter Port 8080. Wird vom Frontend-Service direkt angesprochen.

---

