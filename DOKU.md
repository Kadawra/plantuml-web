# 📘 Projektdokumentation (DOKU.md)

## 🧠 Architektur

![Architekturdiagramm](PlantUML-Service.svg)

- **[Webinterface]('http://localhost:5000')**: Ein- und Ausgabe-Element des PlantUMLs
- **[Flask-Frontend](flask-frontend/info.md)**: Nimmt den PlantUML-Code entgegen
- **[PlantUML-Service](plantUML-service/info.md)**: Wandelt den PlantUML-Code in ein .svg um

---

## 🔁 Wiedereinstieg:

### Git: Projekt aktualisieren

```bash
git clone <repo-url>
git branch -a
git checkout <branchname>
```

### ▶️ Start mit Docker Compose (empfohlen)

Voraussetzung: [Docker & Docker Compose](https://docs.docker.com/compose/install/) installiert.

```bash
# Im Projektverzeichnis:
docker-compose up --build
```

Dann im Browser öffnen:  
👉 [http://localhost:5000](http://localhost:5000)

---

## 📁 Git: Neue & entfernte Dateien verwalten

### Branch updaten

```bash
git add .
git commit -m "Message"
git push
```

### Tipps
- 🔐 `.gitignore` sauber halten → z. B. `.tar.gz`, `.venv`, `__pycache__/` ignorieren
---

## 🧠 Arbeiten mit KI (Prompt-gestützter Workflow)

### Am Projekt arbeiten

KI sinnvoll einsetzen für:  Debugging, Analyse, Dokumentation
📦 Projekt zippen oder als `.tar.gz` verpacken:
```bash
git archive --format=tar.gz -o project.tar.gz HEAD #tar --exclude='.git' -czf projekt.tar.gz .
```
Bitte analysiere den beigefügten Projekt-Export und:
- bearbeite die To-Dos aus der README.md
- optimiere meine Dockerfiles
- dokumentiere in DOKU.md"

### 📌 KI-Chat Übersicht verloren:

- Gliedere mit bitte alle in diesem Chat enthaltenen Fragen in Kategorien und gib eine kurze Zusammenfassung jeder Kategorie.
- Im Canvas bearbeiten und dann draus folgendes generieren:
   - strukturierte Dokumentation
   - FAQ-Seite
   - Confluence-Eintrag

---

## ⚙️ Debugging

### 🔍 Kommunikation zwischen Containern debuggen (Docker Compose)
Problem: Container erreichen sich nicht (z. B. `fetch('http://localhost:5000')` schlägt fehl)

✅ Lösung:
- Verwende den **Servicenamen aus `docker-compose.yml`** → z. B. `http://backend:5000`
- `localhost` ist **innerhalb eines Containers nicht der Host**, sondern der Container selbst.

#### 🧰 Nützliche Debug-Kommandos:

```bash
# Logs eines Containers anzeigen
docker-compose logs backend

# Interaktiv in Container springen
docker exec -it <container-name> sh   # oder bash

# Verbindung zu anderem Container testen (z. B. von frontend zu backend)
apk add curl        # ggf. vorher im Container installieren
curl http://backend:5000
```

📦 Wenn du im `frontend`-Container bist und `curl http://backend:5000` funktioniert, dann ist die Verbindung ok.

---