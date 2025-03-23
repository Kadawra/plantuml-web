FROM python:3.11-slim

# Systemabhängigkeiten: Java + Graphviz + plantuml.jar
RUN apt-get update && apt-get install -y \
    openjdk-17-jre-headless graphviz wget && \
    apt-get clean

WORKDIR /app

# plantuml.jar direkt von GitHub holen (aktuellste Version)
RUN wget -O plantuml.jar https://github.com/plantuml/plantuml/releases/latest/download/plantuml.jar

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

CMD ["python", "app.py"]