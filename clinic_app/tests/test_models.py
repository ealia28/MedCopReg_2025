from app.models import Patient, Doctor, Medicine, Appointment
from app import db
from datetime import date
import pytest

def test_create_patient(db_session):
    p = Patient(
        name="Test",
        gender="M",
        birth_date=date(2000, 1, 1),
        address="Address"
    )
    db.session.add(p)
    db.session.commit()

    assert p.id is not None


def test_unique_medicine_name(db_session):
    m1 = Medicine(name="Аспирин", usage="...", action="...", side_effects="...")
    db.session.add(m1)
    db.session.commit()

    m2 = Medicine(name="Аспирин", usage="...", action="...", side_effects="...")
    db.session.add(m2)

    with pytest.raises(Exception):
        db.session.commit()


def test_create_appointment(db_session):
    p = Patient(name="P", gender="male", birth_date=date(1990,1,1), address="A")
    d = Doctor(name="Dr")

    db.session.add_all([p, d])
    db.session.commit()

    a = Appointment(
        date=date.today(),
        location="Clinic",
        symptoms="Cough",
        diagnosis="Flu",
        prescription="Rest",
        patient_id=p.id,
        doctor_id=d.id
    )

    db.session.add(a)
    db.session.commit()

    assert a.id is not None
