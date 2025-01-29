# Basis-Image mit Python 3.9
FROM python:3.9

# Arbeitsverzeichnis im Container
WORKDIR /app

# Java (OpenJDK) installieren
RUN apt-get update && \
    apt-get install -y openjdk-17-jre && \
    rm -rf /var/lib/apt/lists/*

# Kopiere die Abhängigkeitsdatei und installiere sie
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopiere den Rest des Projekts
COPY . .

# PlantUML herunterladen
RUN wget -O plantuml.jar https://sourceforge.net/projects/plantuml/files/plantuml.jar/download

# Sicherstellen, dass das UML-Verzeichnis existiert
RUN mkdir -p /app/uml_images

# Flask-Anwendung auf Port 5000 bereitstellen
EXPOSE 5000

# Starte die Anwendung
CMD ["python", "app.py"]
