from app.models import Patient
from app import db

def test_add_patient(client, app):
    response = client.post("/add-patient", data={
        "name": "Test Person",
        "gender": "male",
        "birth_date": "1990-01-01",
        "address": "Some street"
    }, follow_redirects=True)

    assert response.status_code == 200
    assert Patient.query.count() == 1

