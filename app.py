from flask import Flask, render_template, request
from translate_code import translate_code

app = Flask(__name__, template_folder="templates", static_folder="customs")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/translate", methods=["POST"])
def translate():
    input_code = request.form["input_code"]
    source_language = request.form["source_language"]
    target_language = request.form["target_language"]

    translated_code = translate_code(input_code, source_language, target_language)

    return render_template(
        "index.html", input_code=input_code, translated_code=translated_code
    )


if __name__ == "__main__":
    app.run(debug=True)
