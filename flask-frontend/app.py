from flask import Flask, request, render_template_string
import requests
import os

app = Flask(__name__)
UPLOAD_PATH = "/uml"
INIT_PUML = os.path.join(os.path.dirname(__file__), "init.puml")

FORM_HTML = """
<h2>PlantUML Online</h2>
<form method="POST">
<textarea name="uml" rows="15" cols="80">{{ user_input }}</textarea><br>
<input type="submit" value="Render">
</form>

{% if svg %}
<h3>Diagramm:</h3>
<div>{{ svg | safe }}</div>
{% endif %}
"""

def render_puml(code: str) -> str:
    res = requests.post("http://plantuml-service:8080/render", data=code.encode("utf-8"),
                            headers={"Content-Type": "text/plain"})
    return res.text if res.status_code == 200 else None

@app.route("/", methods=["GET", "POST"])
def index():
    svg = None

    if request.method == "POST":
        # User hat etwas geschickt
        puml_code = request.form["uml"]
    else:
        # Erste Seite, lad aus init.puml
        if os.path.exists(INIT_PUML):
            with open(INIT_PUML, "r") as f:
                puml_code = f.read()
        else:
            puml_code = "@startuml\nAlice -> Bob : Hello\n@enduml"

    # Datei abspeichern ins Volume (optional)
    with open(os.path.join(UPLOAD_PATH, "diagram.puml"), "w") as f:
        f.write(puml_code)

    svg = render_puml(puml_code)

    return render_template_string(FORM_HTML, svg=svg, user_input=puml_code)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
