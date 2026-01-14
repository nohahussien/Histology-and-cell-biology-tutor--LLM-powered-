from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

db = SQLAlchemy()

class QA(db.Model):
    __tablename__ = "qa_logs"

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime(timezone=True),
    default=lambda: datetime.now(timezone.utc))
    question = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text, nullable=False)

