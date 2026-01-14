import pytest
from app import app, db, QA

@pytest.fixture
def client():
    # Flask test client
    app.config['TESTING'] = True
    # Use in-memory SQLite for tests so we don’t touch Render DB
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  # create tables in memory
        yield client

def test_homepage(client):
    """Test homepage loads"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Ask' in response.data  

def test_ask_question(client):
    """Test asking a question inserts into DB"""
    response = client.post('/', data={'question': 'What is a mitochondrion?'})
    # After posting, check if DB has the question
    with app.app_context():
        qa_entry = QA.query.filter_by(question='What is a mitochondrion?').first()
        assert qa_entry is not None
        assert qa_entry.answer != ''  # answer should be generated

def test_history_page(client):
    """Test history page shows stored questions"""
    # First, insert a test row
    with app.app_context():
        qa = QA(question='Test question?', answer='Test answer')
        db.session.add(qa)
        db.session.commit()

    # Then access history page
    response = client.get('/history')
    assert response.status_code == 200
    assert b'Test question?' in response.data

