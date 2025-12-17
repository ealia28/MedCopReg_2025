from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy.sql import func
from datetime import datetime
from app import db
from app.models import Patient, Doctor, Medicine, Appointment

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    medicines = Medicine.query.order_by(Medicine.name).all()
    return render_template('index.html', medicines=medicines)

@main_bp.route('/query', methods=['POST'])
def handle_query():
    query_type = request.form.get('query_type')
    result = {}
    
    if query_type == 'calls_by_date':
        date_str = request.form.get('date')
        date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
        count = Appointment.query.filter_by(date=date_obj).count()
        result['title'] = f"Количество вызовов на {date_str}"
        result['data'] = f"Всего вызовов (в клинике и на дому): {count}"

    elif query_type == 'patients_by_diagnosis':
        diagnosis = request.form.get('diagnosis')
        count = db.session.query(Appointment.patient_id).filter(func.lower(Appointment.diagnosis) == func.lower(diagnosis)).distinct().count()
        result['title'] = f"Количество больных с диагнозом '{diagnosis}'"
        result['data'] = f"Всего пациентов: {count}"

    elif query_type == 'side_effects_by_medicine':
        medicine_name = request.form.get('medicine_name')
        medicine = Medicine.query.filter_by(name=medicine_name).first()
        side_effects = medicine.side_effects if medicine else "Лекарство не найдено."
        result['title'] = f"Побочные эффекты для лекарства '{medicine_name}'"
        result['data'] = side_effects

    return render_template('query_results.html', result=result)

@main_bp.route('/health')
def health_check():
    """Проверка работоспособности приложения."""
    return "OK", 200

@main_bp.route('/patients')
def list_patients():
    patients = Patient.query.all()
    return render_template('patients.html', patients=patients)

@main_bp.route('/add-patient', methods=['GET', 'POST'])
def add_patient():
    if request.method == 'POST':
        birth_date = datetime.strptime(request.form['birth_date'], '%Y-%m-%d').date()
        new_patient = Patient(
            name=request.form['name'],
            gender=request.form['gender'],
            birth_date=birth_date,
            address=request.form['address'],
            email=request.form.get('email'),  # НОВОЕ ПОЛЕ
            phone=request.form.get('phone')   # НОВОЕ ПОЛЕ
        )
        db.session.add(new_patient)
        db.session.commit()
        return redirect(url_for('main.list_patients'))
    return render_template('add_patient.html')

@main_bp.route('/appointments')
def list_appointments():
    appointments = Appointment.query.order_by(Appointment.date.desc()).all()
    return render_template('appointments.html', appointments=appointments)

@main_bp.route('/add-appointment', methods=['GET', 'POST'])
def add_appointment():
    if request.method == 'POST':
        date = datetime.strptime(request.form['date'], '%Y-%m-%d').date()
        new_appointment = Appointment(
            date=date,
            location=request.form['location'],
            symptoms=request.form['symptoms'],
            diagnosis=request.form['diagnosis'],
            prescription=request.form['prescription'],
            status=request.form.get('status', 'completed'),  # НОВОЕ ПОЛЕ
            follow_up_date=datetime.strptime(request.form['follow_up_date'], '%Y-%m-%d').date() if request.form.get('follow_up_date') else None,  # НОВОЕ ПОЛЕ
            patient_id=int(request.form['patient_id']),
            doctor_id=int(request.form['doctor_id'])
        )
        db.session.add(new_appointment)
        db.session.commit()
        return redirect(url_for('main.list_appointments'))
    
    patients = Patient.query.all()
    doctors = Doctor.query.all()
    return render_template('add_appointment.html', patients=patients, doctors=doctors)

@main_bp.route('/add-medicine', methods=['GET', 'POST'])
def add_medicine():
    if request.method == 'POST':
        new_med = Medicine(
            name=request.form['name'],
            usage=request.form['usage'],
            action=request.form['action'],
            side_effects=request.form['side_effects']
        )
        db.session.add(new_med)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('add_medicine.html')

