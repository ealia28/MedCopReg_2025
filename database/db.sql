CREATE TABLE patient (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(150) NOT NULL,
    gender VARCHAR(10) NOT NULL,
    birth_date DATE NOT NULL,
    address VARCHAR(255) NOT NULL,
    email VARCHAR(100),
    phone VARCHAR(20),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

CREATE TABLE doctor (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(150) NOT NULL,
    specialty VARCHAR(100),
    license_number VARCHAR(50),
    PRIMARY KEY (id)
);

CREATE TABLE medicine (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    usage TEXT NOT NULL,
    action TEXT NOT NULL,
    side_effects TEXT NOT NULL,
    dosage VARCHAR(100),
    manufacturer VARCHAR(150),
    UNIQUE KEY uq_medicine_name (name),
    PRIMARY KEY (id)
);

CREATE TABLE appointment (
    id INT NOT NULL AUTO_INCREMENT,
    date DATE NOT NULL,
    location VARCHAR(100) NOT NULL,
    symptoms TEXT NOT NULL,
    diagnosis VARCHAR(150) NOT NULL,
    prescription TEXT NOT NULL,
    status VARCHAR(20) DEFAULT 'completed',
    follow_up_date DATE,
    patient_id INT NOT NULL,
    doctor_id INT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    KEY idx_appointment_patient_id (patient_id),
    KEY idx_appointment_doctor_id (doctor_id),
    CONSTRAINT fk_appointment_patient
    FOREIGN KEY (patient_id)
    REFERENCES patient (id),
    CONSTRAINT fk_appointment_doctor
    FOREIGN KEY (doctor_id)
    REFERENCES doctor (id)
);
