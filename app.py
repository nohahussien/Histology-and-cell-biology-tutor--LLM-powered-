import os
from flask import Flask, render_template, request
from models import db, QA
import my_llm
from my_llm import ask_llm
from dotenv import load_dotenv
load_dotenv()  # This reads .env into os.environ


GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# External db ( on Render postgres) as requested
DATABASE_URL = os.getenv("DATABASE_URL")
# Local db (on Docker postgres) as created in the beginning
# DATABASE_URL = "postgresql://postgres:postgres@localhost:5433/histology_db"

app = Flask(__name__)

my_llm.client = my_llm.Groq(api_key=GROQ_API_KEY)

# Database config
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

@app.route("/", methods=["GET", "POST"])
def index():
    answer = None
    if request.method == "POST":
        question = request.form["question"]
        answer = ask_llm(question)

        qa = QA(question=question, answer=answer)
        db.session.add(qa)
        db.session.commit()

    return render_template("index.html", answer=answer)

@app.route("/history")
def history():
    qa_list = QA.query.order_by(QA.timestamp.desc()).all()
    return render_template("history.html", qa_list=qa_list)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5000)


 # Running on http://127.0.0.1:5000
 # Running on http://192.168.1.41:5000








