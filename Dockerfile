# Basis-Image mit Python 3.9
FROM python:3.9

# Arbeitsverzeichnis im Container
WORKDIR /app

# Kopiere die Abhängigkeitsdatei und installiere sie
COPY requirements.txt .
RUN pip install -r requirements.txt

# Kopiere den Rest des Projekts
COPY . .

# Exponiere den Flask-Port 5000
EXPOSE 5000

# Starte die Anwendung
CMD ["python", "app.py"]