from app.models import Patient, Doctor, Appointment, Medicine
from app import db
from datetime import date

def test_calls_by_date(client, app):
    p = Patient(name="P", gender="male", birth_date=date(1990,1,1), address="A")
    d = Doctor(name="D")
    db.session.add_all([p, d])
    db.session.commit()

    a = Appointment(
        date=date(2024,1,1),
        location="Clinic",
        symptoms="S",
        diagnosis="D",
        prescription="P",
        patient_id=p.id,
        doctor_id=d.id
    )
    db.session.add(a)
    db.session.commit()

    response = client.post("/query", data={
        "query_type": "calls_by_date",
        "date": "2024-01-01"
    })

    assert b"Всего вызовов" in response.data
    assert b"1" in response.data


def test_side_effects_query(client, app):
    med = Medicine(
        name="Парацетамол",
        usage="Use",
        action="Action",
        side_effects="Жар, сонливость"
    )
    db.session.add(med)
    db.session.commit()

    response = client.post("/query", data={
        "query_type": "side_effects_by_medicine",
        "medicine_name": "Парацетамол"
    })

    assert b"Жар" in response.data


