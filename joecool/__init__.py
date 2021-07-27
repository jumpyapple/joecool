from flask import Flask, Response, render_template, request


def create_app() -> Flask:
    """Create flask app."""
    app = Flask(__name__)

    @app.route("/", methods=["GET", "POST"])
    def home() -> Response:
        if request.method == "POST":
            input_text = request.form.get("input_text", None)
            if input_text:
                tokens = input_text.split()
                if len(tokens) >= 50:
                    return render_template("token.html", tokens=["Too", "long"])
                return render_template("token.html", tokens=tokens)
        return render_template("index.html")

    return app
