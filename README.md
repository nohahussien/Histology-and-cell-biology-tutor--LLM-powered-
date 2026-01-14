# 🔬 Histology and Cell Biology Tutor — LLM Powered

An interactive web application that allows users to ask questions about **Histology and Cell Biology** using a Large Language Model (LLM).  
All questions and answers are stored in a PostgreSQL database and can be viewed through a history interface.

The project is fully containerized using Docker and supports cloud deployment (via Render).

---

## 🚀 Features

- 🤖 AI-powered question answering using Groq LLM
- 🧬 Domain-restricted responses (Histology & Cell Biology)
- 🗃️ Persistent storage of all questions and answers
- 📜 History page to browse previous interactions
- 🐳 Dockerized for portability and easy deployment
- 🧪 Automated tests with pytest
- ☁️ Cloud-ready (Render compatible)

---

## 🏗️ Project Structure

├── app.py # Flask application entry point
├── my_llm.py # LLM integration logic
├── models.py # Database models
├── db_history.py # Export database history to CSV
├── templates/ # HTML templates (UI)
├── docker-compose.yml # Docker multi-service configuration
├── dockerfile # Application Docker image definition
├── requirements.txt # Python dependencies
├── test_app.py # Automated tests
├── .dockerignore # Docker ignore rules
└── README.md

---

## ⚙️ Tech Stack

- **Backend:** Python, Flask
- **LLM Provider:** Groq API
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Containerization:** Docker, Docker Compose
- **Testing:** Pytest
- **Deployment:** Render / Docker Hub

---

## 🔐 Environment Variables

Create a `.env` file in the project root:

GROQ_API_KEY=your_groq_api_key
DATABASE_URL=postgresql://<user>:<password>@<host>:<port>/<database>



⚠️ Never commit `.env` to GitHub.

---

## ▶️ Run Locally (without Docker)

1. Create virtual environment (optional):

python -m venv venv
source venv/bin/activate # Windows: venv\Scripts\activate

2. Install dependencies:

pip install -r requirements.txt


3. Set environment variables or create `.env`.

4. Run application:

python app.py

markdown
Copiar código

5. Open browser:

http://localhost:5000

---

## 🐳 Run with Docker

### Build and start containers:

docker compose up --build

Application will be available at:

http://localhost:5000

### Stop containers:

docker compose down

---

## 🗄️ Database

- PostgreSQL runs as a Docker container.
- Tables are created automatically on app startup.
- Main table: `qa_logs`
  - id
  - timestamp
  - question
  - answer

---

## 📤 Export History to CSV

Run:

python db_history.py


This exports all QA history to a CSV file.

---

## 🧪 Run Tests

Install pytest if needed:

pip install pytest

Run tests:

pytest

---

## ☁️ Cloud Deployment

The application can be deployed using:
- Render Web Service using the Docker image : "https://histology-app-latest-1.onrender.com/" (NOTE: this is doable as long as the API-key used is active!!"

---

## 📈 Future Improvements

- User authentication
- Pagination for history
- UI enhancements
- Rate limiting
- Admin dashboard
- Analytics
- Multi-language support

---

## 🎓 Please note that...

this app is only for educational and learning purposes.
