   # PlantUML Web Generator

   Ein einfaches Web-Interface zur Erstellung von UML-Diagrammen mit PlantUML.

   ## 🚀 Features

   - UML-Code im Browser eingeben und SVG-Diagramme generieren.
   - Flask-Backend zur Verarbeitung und Generierung von Diagrammen.
   - Docker-Container zur einfachen Bereitstellung.

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

   1. Repository klonen:

      ```bash
      git clone https://github.com/dein-benutzername/plantuml-web.git
      cd plantuml-web
      ```

   2. Abhängigkeiten installieren:

      ```bash
      pip install -r requirements.txt
      ```

   3. PlantUML herunterladen:

      ```bash
      wget -O plantuml.jar https://sourceforge.net/projects/plantuml/files/plantuml.jar/download
      ```

   4. Anwendung starten:

      ```bash
      python app.py
      ```

   5. Öffne den Browser unter `http://localhost:5000`.

   ## 🐳 Docker-Nutzung

   Build und Start des Containers:

   ```bash
   docker build -t plantuml-web .
   docker run -p 5000:5000 plantuml-web
   ```

   ## 🛠️ To-Do

   - Mermaid.js-Unterstützung hinzufügen.
   - Verbesserte Fehlerbehandlung.

   ## 📄 Lizenz

   Dieses Projekt steht unter der MIT-Lizenz.