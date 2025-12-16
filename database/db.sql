CREATE TABLE app_patient (
    patient_id INT NOT NULL AUTO_INCREMENT,
    patient_full_name VARCHAR(150) NOT NULL,
    patient_gender_code VARCHAR(10) NOT NULL,
    patient_birth_date DATE NOT NULL,
    patient_address_text VARCHAR(255) NOT NULL,
    PRIMARY KEY (patient_id)
);

CREATE TABLE app_doctor (
    doctor_id INT NOT NULL AUTO_INCREMENT,
    doctor_full_name VARCHAR(150) NOT NULL,
    PRIMARY KEY (doctor_id)
);

CREATE TABLE app_medicine (
    medicine_id INT NOT NULL AUTO_INCREMENT,
    medicine_name_text VARCHAR(100) NOT NULL,
    medicine_usage_text TEXT NOT NULL,
    medicine_action_text TEXT NOT NULL,
    medicine_side_effects_text TEXT NOT NULL,
    UNIQUE KEY uq_medicine_name_text (medicine_name_text),
    PRIMARY KEY (medicine_id)
);

CREATE TABLE app_appointment (
    appointment_id INT NOT NULL AUTO_INCREMENT,
    appointment_date_value DATE NOT NULL,
    appointment_location_text VARCHAR(100) NOT NULL,
    appointment_symptoms_text TEXT NOT NULL,
    appointment_diagnosis_text VARCHAR(150) NOT NULL,
    appointment_prescription_text TEXT NOT NULL,
    appointment_patient_id INT NOT NULL,
    appointment_doctor_id INT NOT NULL,
    PRIMARY KEY (appointment_id),
    KEY idx_appointment_patient_id (appointment_patient_id),
    KEY idx_appointment_doctor_id (appointment_doctor_id),
    CONSTRAINT fk_appointment_patient FOREIGN KEY (appointment_patient_id) REFERENCES app_patient (patient_id),
    CONSTRAINT fk_appointment_doctor FOREIGN KEY (appointment_doctor_id) REFERENCES app_doctor (doctor_id)
);
