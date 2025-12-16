CREATE TABLE patient (
    id INT NOT NULL AUTO_INCREMENT,
    full_name VARCHAR(150) NOT NULL,
    gender VARCHAR(10) NOT NULL,
    birth_date DATE NOT NULL,
    address VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE doctor (
    id INT NOT NULL AUTO_INCREMENT,
    full_name VARCHAR(150) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE medicine (
    id INT NOT NULL AUTO_INCREMENT,
    medicine_name VARCHAR(100) NOT NULL,
    usage_description TEXT NOT NULL,
    action_description TEXT NOT NULL,
    side_effects TEXT NOT NULL,
    UNIQUE KEY uq_medicine_name (medicine_name),
    PRIMARY KEY (id)
);

CREATE TABLE appointment (
    id INT NOT NULL AUTO_INCREMENT,
    appointment_date DATE NOT NULL,
    location VARCHAR(100) NOT NULL,
    symptoms TEXT NOT NULL,
    diagnosis VARCHAR(150) NOT NULL,
    prescription TEXT NOT NULL,
    patient_id INT NOT NULL,
    doctor_id INT NOT NULL,
    PRIMARY KEY (id),
    KEY idx_appointment_patient (patient_id),
    KEY idx_appointment_doctor (doctor_id),
    CONSTRAINT fk_appointment_patient
        FOREIGN KEY (patient_id)
        REFERENCES patient (id),
    CONSTRAINT fk_appointment_doctor
        FOREIGN KEY (doctor_id)
        REFERENCES doctor (id)
);
