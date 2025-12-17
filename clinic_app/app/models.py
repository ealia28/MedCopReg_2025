from app import db
from datetime import datetime

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    address = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), nullable=True)  # НОВОЕ ПОЛЕ: email пациента
    phone = db.Column(db.String(20), nullable=True)   # НОВОЕ ПОЛЕ: телефон пациента
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # НОВОЕ ПОЛЕ: дата создания
    appointments = db.relationship('Appointment', backref='patient', lazy=True)

class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    specialty = db.Column(db.String(100), nullable=True)  # НОВОЕ ПОЛЕ: специализация
    license_number = db.Column(db.String(50), nullable=True)  # НОВОЕ ПОЛЕ: номер лицензии
    appointments = db.relationship('Appointment', backref='doctor', lazy=True)

class Medicine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    usage = db.Column(db.Text, nullable=False)
    action = db.Column(db.Text, nullable=False)
    side_effects = db.Column(db.Text, nullable=False)
    dosage = db.Column(db.String(100), nullable=True)  # НОВОЕ ПОЛЕ: дозировка
    manufacturer = db.Column(db.String(150), nullable=True)  # НОВОЕ ПОЛЕ: производитель

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    symptoms = db.Column(db.Text, nullable=False)
    diagnosis = db.Column(db.String(150), nullable=False)
    prescription = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default='completed')  # НОВОЕ ПОЛЕ: статус приема
    follow_up_date = db.Column(db.Date, nullable=True)  # НОВОЕ ПОЛЕ: дата повторного визита
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # НОВОЕ ПОЛЕ: дата создания


