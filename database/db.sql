CREATE TABLE patient (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(150) NOT NULL,
    gender VARCHAR(10) NOT NULL,
    birth_date DATE NOT NULL,
    address VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE doctor (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(150) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE appointment (
    id INT NOT NULL AUTO_INCREMENT,
    date DATE NOT NULL,
    location VARCHAR(100) NOT NULL,
    symptoms TEXT NOT NULL,
    diagnosis VARCHAR(150) NOT NULL,
    prescription TEXT NOT NULL,
    patient_id INT NOT NULL,
    doctor_id INT NOT NULL,
    PRIMARY KEY (id),
    KEY (patient_id),
    KEY (doctor_id),
    CONSTRAINT fk_patient
        FOREIGN KEY (patient_id)
        REFERENCES patient (id),
    CONSTRAINT fk_doctor
        FOREIGN KEY (doctor_id)
        REFERENCES doctor (id)
);
