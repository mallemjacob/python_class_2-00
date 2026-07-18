import os

from dotenv import load_dotenv
from flask import Flask, render_template, request
from google import genai


load_dotenv()

app = Flask(__name__)

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


@app.route("/", methods=["GET", "POST"])
def home():
    answer = ""

    if request.method == "POST":
        question = request.form["question"]

        response = client.interactions.create(
            model="gemini-3.5-flash",
            input=f"Give a concise answer: {question}"
        )

        answer = response.output_text

    return render_template("index.html", answer=answer)


if __name__ == "__main__":
    app.run(debug=True)
