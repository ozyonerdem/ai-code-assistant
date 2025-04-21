from flask import Flask, request, render_template
from ollama_client import generate_code, parse_response

app = Flask(__name__, template_folder='templates')

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        prompt = request.form["prompt"]
        raw_response = generate_code(prompt)
        title, code = parse_response(raw_response)
        return render_template("results.html", title =title, code = code)
    return render_template("form.html")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)