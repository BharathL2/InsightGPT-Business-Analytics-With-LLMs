import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from utils.text_analysis import load_transcript
from utils.data_analysis import perform_eda
from utils.llm_engine import summarize_text, generate_insights

load_dotenv()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    uploaded_file = request.files["file"]

    if uploaded_file.filename.endswith(".csv"):
        filepath = os.path.join("static", uploaded_file.filename)
        uploaded_file.save(filepath)

        eda_results, plots = perform_eda(filepath)
        return render_template("result.html", eda=eda_results, plots=plots)

    elif uploaded_file.filename.endswith(".txt"):
        transcript = uploaded_file.read().decode("utf-8")
        summary = summarize_text(transcript)
        insights = generate_insights(transcript)

        return render_template("result.html", summary=summary, insights=insights)

    else:
        return "Unsupported file format", 400

if __name__ == "__main__":
    app.run(debug=True)
