# Project: Gemini Flask

## Files

```
Project_Gemini_Flask/
├── app.py
├── requirements.txt
├── .env
└── templates/
    └── index.html
```

## Step 1: Create files

mkdir Project_Gemini_Flask
cd Project_Gemini_Flask
mkdir templates
touch app.py requirements.txt .env templates/index.html

## Step 2: Install packages

python3 -m venv .venv
source .venv/bin/activate

### Windows

py -m venv .venv
.venv\Scripts\activate

## Put this in requirements.txt:

Flask
google-genai
python-dotenv
gunicorn

## Install

pip install -r requirements.txt

## Step 3: Add API key

In .env:
GEMINI_API_KEY=your_api_key_here

## Step 4: app.py

```python
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

```

## Step 5: templates/index.html

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Ask Gemini</title>
    </head>
    <body>
        <h1>Ask Gemini</h1>

        <form method="POST">
            <input
                type="text"
                name="question"
                placeholder="Type something"
                required
            />
            <button type="submit">Submit</button>
        </form>

        {% if answer %}
        <h2>Answer:</h2>
        <p>{{ answer }}</p>
        {% endif %}
    </body>
</html>
```

## Step 6: Run

`python app.py`

---

## Deploy on Render

Before GitHub, create .gitignore:

.venv/
.env
**pycache**/

Push to GitHub.

Render settings:

Build Command: pip install -r requirements.txt
Start Command: gunicorn app:app

Add environment variable in Render:

GEMINI_API_KEY = your_api_key_here

Done.
