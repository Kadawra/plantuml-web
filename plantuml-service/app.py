from flask import Flask, request, Response
import subprocess
import tempfile
import os

app = Flask(__name__)

@app.route("/render", methods=["POST"])
def render():
    puml_code = request.data.decode("utf-8")

    with tempfile.TemporaryDirectory() as tmpdir:
        input_path = os.path.join(tmpdir, "input.puml")
        output_path = os.path.join(tmpdir, "input.svg")

        with open(input_path, "w") as f:
            f.write(puml_code)

        try:
            jar_path = "/app/plantuml.jar"
            subprocess.run(["java", "-jar", jar_path, "-tsvg", input_path],
                        check=True, cwd=tmpdir)

            with open(output_path, "r") as f:
                svg = f.read()
            return Response(svg, mimetype="image/svg+xml")
        except subprocess.CalledProcessError as e:
            return f"Render error: {e}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
