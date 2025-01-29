from flask import Flask, request, jsonify, send_from_directory
import os
import subprocess

app = Flask(__name__)

# Speicherort für generierte Bilder
STORAGE_PATH = "uml_images"

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/generate', methods=['POST'])
def generate_image():
    try:
        data = request.json
        uml_code = data.get('uml')

        if not uml_code:
            print("Fehler: Kein UML-Code empfangen.")
            return jsonify({"error": "Kein PlantUML-Code bereitgestellt"}), 400

        uml_file = os.path.join(STORAGE_PATH, "diagram.puml")
        image_file = os.path.join(STORAGE_PATH, "diagram.svg")

        # UML-Code speichern
        print(f"UML-Code wird gespeichert in: {uml_file}")
        with open(uml_file, 'w') as f:
            f.write(uml_code)

        # PlantUML-Befehl ausführen und Ausgabe erfassen
        try:
            result = subprocess.run(
                ["java", "-jar", "plantuml.jar", "-tsvg", uml_file],
                check=True, capture_output=True, text=True
            )
            print("PlantUML-Ausgabe:", result.stdout)
            print("PlantUML-Fehlerausgabe:", result.stderr)

        except subprocess.CalledProcessError as e:
            print(f"Fehler beim PlantUML-Aufruf: {e}")
            print("Standardausgabe:", e.stdout)
            print("Fehlerausgabe:", e.stderr)
            return jsonify({"error": "Fehler beim Erstellen des Diagramms"}), 500

        # Prüfen, ob SVG-Datei erfolgreich erstellt wurde
        if not os.path.exists(image_file):
            print(f"Fehler: Die SVG-Datei wurde nicht erstellt ({image_file}).")
            return jsonify({"error": "SVG-Datei konnte nicht erstellt werden"}), 500

        print("SVG-Datei erfolgreich generiert:", image_file)
        return jsonify({"image_url": f"/uml_images/diagram.svg"})

    except Exception as e:
        print("Unerwarteter Fehler:", str(e))
        return jsonify({"error": str(e)}), 500


@app.route('/uml_images/<filename>')
def get_image(filename):
    return send_from_directory(STORAGE_PATH, filename)

if __name__ == '__main__':
    os.makedirs(STORAGE_PATH, exist_ok=True)
    app.run(host='0.0.0.0', port=5000, debug=True)

