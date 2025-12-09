def test_create_patient(db_session):
    from app.models import Patient

    p = Patient(name="Test", gender="M", birth_date="2000-01-01")
    db.session.add(p)
    db.session.commit()

    assert p.id is not None
