# PlantUML Web Generator

Ein **einfaches Web-Interface** zur Erstellung von UML-Diagrammen mit PlantUML.

## 🚀 Features

- ✍ **UML-Code im Browser** eingeben und als **SVG-Diagramm** generieren.
- 🖥 **Flask-Backend** verarbeitet und erstellt die Diagramme.
- 🐳 **Docker-Container** für einfache Bereitstellung.
- ✅ **Unterstützt Bind-Mounts**, um Code-Änderungen direkt im laufenden Container zu übernehmen.

## 📂 Projektstruktur

```
plantuml-web/
│-- app.py             # Flask-Anwendung
│-- index.html         # Frontend mit HTML/JS
│-- Dockerfile         # Container-Konfiguration
│-- requirements.txt   # Python-Abhängigkeiten
│-- uml_images/        # Generierte Diagramme (wird ignoriert)
└-- .gitignore         # Ausschluss unnötiger Dateien
```

## ⚙️ Installation & Verwendung

### **1️⃣ Ohne Docker (manuell per Terminal)**
1. Repository klonen:
   ```bash
   cd <lokales (leeres) GitHubVerzeichnis>
  git clone https://github.com/Kadawra/plantuml-web.git
  git checkout -b <lokales UpdateVerzeichnis> --track origin/bugfix-puml-overwrite
   cd plantuml-web
   ```

2. Abhängigkeiten installieren:
   ```bash
   pip install -r requirements.txt
   ```

3. **PlantUML herunterladen** (falls noch nicht vorhanden):
   ```bash
   wget -O plantuml.jar https://sourceforge.net/projects/plantuml/files/plantuml.jar/download
   ```

4. Anwendung starten:
   ```bash
   python app.py
   ```

5. Öffne den Browser unter **`http://localhost:5000`**.

---

### **2️⃣ Mit Docker (empfohlen)**
Falls du **Docker** verwendest, kannst du den Container einfach starten.

#### **Container bauen & starten**
```bash
docker build -t plantuml-web .
docker run -p 5000:5000 plantuml-web
```

💡 **Wichtig:** Falls du Änderungen an `app.py` oder `index.html` machst, musst du den Container **neustarten**, damit die Änderungen übernommen werden:

```bash
docker stop <container_id>
docker rm <container_id>
docker run -p 5000:5000 plantuml-web
```

---

### **3️⃣ Docker mit Bind-Mounts nutzen (sofortige Code-Übernahme)**
Falls du möchtest, dass Änderungen **ohne Neustart des Containers** übernommen werden, kannst du einen **Bind-Mount** nutzen:

```bash
docker run -v $(pwd):/app -p 5000:5000 plantuml-web
```
✅ **Vorteil:** Änderungen in `app.py` oder `index.html` werden sofort sichtbar.  
⚠ **Nachteil:** Falls du neue Abhängigkeiten in `requirements.txt` hinzufügst, musst du den Container trotzdem neu bauen.

---

## 🛠 Entwicklung & Debugging

Falls du Änderungen testen willst, ohne Docker zu nutzen, kannst du Flask direkt starten:
```bash
python app.py
```

Falls du Logs aus dem Container sehen möchtest:
```bash
docker logs <container_id>
```

Falls du eine **Shell im Container öffnen** möchtest:
```bash
docker exec -it <container_id> bash
```

---

## 🏗 To-Do / Nächste Schritte

- 🚀 **CI/CD-Pipeline mit GitHub Actions**
- 🚀 **Mermaid.js-Support als nächster Schritt**
- 🚀 **Bessere UI & UX-Verbesserungen**

## 📄 Lizenz

Dieses Projekt steht unter der **MIT-Lizenz**.