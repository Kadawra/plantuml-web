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
    data = request.json
    uml_code = data.get('uml')

    if not uml_code:
        return jsonify({"error": "Kein PlantUML-Code bereitgestellt"}), 400

    uml_file = os.path.join(STORAGE_PATH, "diagram.puml")
    image_file = os.path.join(STORAGE_PATH, "diagram.svg")

    # UML-Code speichern
    with open(uml_file, 'w') as f:
        f.write(uml_code)

    # PlantUML-Befehl ausführen
    try:
        subprocess.run(["java", "-jar", "plantuml.jar", "-tsvg", uml_file], check=True)
        return jsonify({"image_url": f"/uml_images/diagram.svg"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/uml_images/<filename>')
def get_image(filename):
    return send_from_directory(STORAGE_PATH, filename)

if __name__ == '__main__':
    os.makedirs(STORAGE_PATH, exist_ok=True)
    app.run(host='0.0.0.0', port=5000)
