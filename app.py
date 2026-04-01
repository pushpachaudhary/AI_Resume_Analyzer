from flask import Flask, render_template, request, jsonify
import PyPDF2
import os
from model import analyze_resume

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

def extract_text_from_pdf(file_path):
    reader = PyPDF2.PdfReader(file_path)
    text = ""

    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()

    return text

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["resume"]

    if file:
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(file_path)

        text = extract_text_from_pdf(file_path)
        result = analyze_resume(text)

        return jsonify(result)

    return jsonify({"error": "No file uploaded"})

if __name__ == "__main__":
    app.run(debug=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)    