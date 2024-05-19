-- Creación de tablas

-- Tabla Paciente
CREATE TABLE Paciente (
    PacienteId SERIAL PRIMARY KEY,
    Rut VARCHAR(20) UNIQUE NOT NULL,
    Nombre VARCHAR(100) NOT NULL
);

-- Tabla Médico
CREATE TABLE Medico (
    MedicoId SERIAL PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL,
    Especialidad VARCHAR(50) NOT NULL,
    Vigente BOOLEAN NOT NULL
);

-- Tabla Habitación
CREATE TABLE Habitacion (
    HabitacionId SERIAL PRIMARY KEY,
    Numero VARCHAR(20) NOT NULL,
    Capacidad INT NOT NULL
);

-- Tabla Cama
CREATE TABLE Cama (
    CamaId SERIAL PRIMARY KEY,
    HabitacionId INT NOT NULL,
    Disponibilidad BOOLEAN NOT NULL,
    FOREIGN KEY (HabitacionId) REFERENCES Habitacion(HabitacionId)
);

-- Tabla Visita
CREATE TABLE Visita (
    VisitaId SERIAL PRIMARY KEY,
    PacienteId INT NOT NULL,
    FechaEntrada TIMESTAMP NOT NULL,
    FechaSalida TIMESTAMP,
    MedicoId INT NOT NULL,
    CamaId INT NOT NULL,
    FOREIGN KEY (PacienteId) REFERENCES Paciente(PacienteId),
    FOREIGN KEY (MedicoId) REFERENCES Medico(MedicoId),
    FOREIGN KEY (CamaId) REFERENCES Cama(CamaId)
);

-- Tabla Enfermedad
CREATE TABLE Enfermedad (
    EnfermedadId SERIAL PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL,
    Descripcion TEXT NOT NULL
);

-- Tabla Diagnostico (nueva tabla)
CREATE TABLE Diagnostico (
    DiagnosticoId SERIAL PRIMARY KEY,
    VisitaId INT NOT NULL,
    EnfermedadId INT NOT NULL,
    Descripcion TEXT,
    FOREIGN KEY (VisitaId) REFERENCES Visita(VisitaId),
    FOREIGN KEY (EnfermedadId) REFERENCES Enfermedad(EnfermedadId)
);



-- Tabla Examen
CREATE TABLE Examen (
    ExamenId SERIAL PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL,
    Descripcion TEXT NOT NULL
);

-- Tabla VisitaExamen
CREATE TABLE VisitaExamen (
    VisitaId INT NOT NULL,
    ExamenId INT NOT NULL,
    Fecha TIMESTAMP NOT NULL,
    Resultado TEXT,
    PRIMARY KEY (VisitaId, ExamenId),
    FOREIGN KEY (VisitaId) REFERENCES Visita(VisitaId),
    FOREIGN KEY (ExamenId) REFERENCES Examen(ExamenId)
);

-- Relación Examen-Enfermedad (tabla de unión)
CREATE TABLE ExamenEnfermedad (
    ExamenId INT NOT NULL,
    EnfermedadId INT NOT NULL,
    PRIMARY KEY (ExamenId, EnfermedadId),
    FOREIGN KEY (ExamenId) REFERENCES Examen(ExamenId),
    FOREIGN KEY (EnfermedadId) REFERENCES Enfermedad(EnfermedadId)
);

-- Índices para mejorar la velocidad de las consultas
CREATE INDEX idx_paciente ON Paciente(Rut);
CREATE INDEX idx_medico ON Medico(Nombre);
CREATE INDEX idx_habitacion ON Habitacion(Numero);
CREATE INDEX idx_cama ON Cama(HabitacionId);
CREATE INDEX idx_visita ON Visita(PacienteId);
CREATE INDEX idx_diagnostico ON Diagnostico(VisitaId);
CREATE INDEX idx_enfermedad ON Enfermedad(Nombre);
CREATE INDEX idx_examen ON Examen(Nombre);

-- Inserts
-- Inserts para la Tabla Paciente
INSERT INTO Paciente (Rut, Nombre) VALUES
('12345678-9', 'Juan Pérez'),
('87654321-0', 'Ana Gómez'),
('23456789-1', 'Carlos Ruiz'),
('34567890-2', 'Diana Morales'),
('45678901-3', 'Pedro Sánchez'),
('56789012-4', 'Lucía Hernández'),
('67890123-5', 'Javier López'),
('78901234-6', 'Marta Vidal'),
('89012345-7', 'Felipe Castro'),
('90123456-8', 'Sofía Martínez');

-- Inserts para la Tabla Médico
INSERT INTO Medico (Nombre, Especialidad, Vigente) VALUES
('Dr. Alberto Solis', 'Cardiología', TRUE),
('Dr. Carmen Linares', 'Pediatría', TRUE),
('Dr. Oscar Blanco', 'Dermatología', TRUE),
('Dra. Laura Redondo', 'Ginecología', TRUE),
('Dr. Marcos Anton', 'Neurología', TRUE),
('Dr. Samuel Prado', 'Anestesiología', TRUE),
('Dra. Elena Núñez', 'Ortopedia', TRUE),
('Dr. Carlos Esteban', 'Psiquiatría', TRUE),
('Dra. Patricia Miró', 'Oftalmología', TRUE),
('Dr. Jorge Marín', 'Urgenciología', TRUE);

-- Inserts para la Tabla Habitación
INSERT INTO Habitacion (Numero, Capacidad) VALUES
('101', 2),
('102', 2),
('103', 1),
('104', 1),
('105', 3),
('201', 2),
('202', 2),
('203', 1),
('204', 1),
('205', 3);

-- Inserts para la Tabla Cama
INSERT INTO Cama (HabitacionId, Disponibilidad) VALUES
(1, TRUE),
(1, TRUE),
(2, TRUE),
(2, TRUE),
(3, TRUE),
(4, TRUE),
(5, TRUE),
(5, TRUE),
(5, TRUE),
(6, TRUE);

-- Inserts para la Tabla Visita
INSERT INTO Visita (PacienteId, FechaEntrada, FechaSalida, MedicoId, CamaId) VALUES
(1, '2024-01-01 10:00:00', '2024-01-01 20:00:00', 1, 1),
(2, '2024-01-02 10:00:00', '2024-01-02 20:00:00', 2, 2),
(3, '2024-01-03 10:00:00', '2024-01-03 20:00:00', 3, 3),
(4, '2024-01-04 10:00:00', '2024-01-04 20:00:00', 4, 4),
(5, '2024-01-05 10:00:00', '2024-01-05 20:00:00', 5, 5),
(6, '2024-01-06 10:00:00', '2024-01-06 20:00:00', 6, 6),
(7, '2024-01-07 10:00:00', '2024-01-07 20:00:00', 7, 7),
(8, '2024-01-08 10:00:00', '2024-01-08 20:00:00', 8, 8),
(9, '2024-01-09 10:00:00', '2024-01-09 20:00:00', 9, 9),
(10, '2024-01-10 10:00:00', '2024-01-10 20:00:00', 10, 10);

-- Inserts para la Tabla Enfermedad
INSERT INTO Enfermedad (Nombre, Descripcion) VALUES
('Gripe', 'Infección viral que afecta principalmente el sistema respiratorio.'),
('Varicela', 'Enfermedad viral que causa una erupción cutánea de pequeñas ampollas rojas.'),
('Hipertensión', 'Enfermedad crónica caracterizada por incremento de la presión arterial.'),
('Diabetes', 'Enfermedad crónica que afecta la manera en que el cuerpo procesa el azúcar en la sangre.'),
('Asma', 'Enfermedad pulmonar que provoca dificultad para respirar.'),
('Artritis', 'Inflamación de las articulaciones que provoca dolor y limitación del movimiento.'),
('Osteoporosis', 'Enfermedad que debilita los huesos, haciéndolos frágiles y más propensos a romperse.'),
('Alzheimer', 'Enfermedad neurodegenerativa que provoca la pérdida de la memoria.'),
('Cáncer', 'Enfermedad caracterizada por una división celular incontrolada en partes del cuerpo.'),
('Migraña', 'Tipo de dolor de cabeza recurrente que puede causar un dolor pulsante o palpitante.');

-- Inserts para la Tabla Diagnostico
INSERT INTO Diagnostico (VisitaId, EnfermedadId, Descripcion) VALUES
(1, 1, 'Diagnóstico inicial de gripe.'),
(2, 2, 'Diagnóstico inicial de varicela.'),
(3, 3, 'Control de hipertensión.'),
(4, 4, 'Control de diabetes.'),
(5, 5, 'Revisión de síntomas de asma.'),
(6, 6, 'Evaluación de artritis en rodillas.'),
(7, 7, 'Consulta por riesgo de osteoporosis.'),
(8, 8, 'Evaluación temprana de Alzheimer.'),
(9, 9, 'Consulta y diagnóstico de cáncer.'),
(10, 10, 'Consulta para tratamiento de migraña.');

-- Inserts para la Tabla Examen
INSERT INTO Examen (Nombre, Descripcion) VALUES
('Hemograma', 'Análisis de sangre que evalúa los diferentes tipos de células sanguíneas.'),
('Electrocardiograma', 'Registro de la actividad eléctrica del corazón.'),
('Ecografía', 'Técnica de imagen que usa ondas de sonido para crear imágenes del interior del cuerpo.'),
('Biopsia', 'Procedimiento que involucra la extracción de una muestra de tejido para examinarla más de cerca.'),
('Tomografía', 'Procedimiento de diagnóstico por imagen que permite visualizar estructuras internas.'),
('Resonancia Magnética', 'Técnica de imagen que usa imanes y ondas de radio para producir imágenes detalladas.'),
('Prueba de esfuerzo', 'Examen que evalúa el rendimiento cardíaco durante el ejercicio físico.'),
('Radiografía', 'Procedimiento de imagen que usa radiación para visualizar el interior del cuerpo.'),
('Análisis de orina', 'Examen de laboratorio realizado en una muestra de orina.'),
('Densitometría ósea', 'Examen que mide la densidad mineral ósea.');

-- Inserts para la Tabla VisitaExamen
INSERT INTO VisitaExamen (VisitaId, ExamenId, Fecha, Resultado) VALUES
(1, 1, '2024-01-01 10:30:00', 'Resultados normales'),
(2, 2, '2024-01-02 10:30:00', 'Ritmo cardíaco irregular'),
(3, 3, '2024-01-03 10:30:00', 'No se observan anomalías'),
(4, 4, '2024-01-04 10:30:00', 'Presencia de células atípicas'),
(5, 5, '2024-01-05 10:30:00', 'Tumor detectado en el lóbulo frontal'),
(6, 6, '2024-01-06 10:30:00', 'Estructura ósea normal'),
(7, 7, '2024-01-07 10:30:00', 'Capacidad pulmonar reducida'),
(8, 8, '2024-01-08 10:30:00', 'Fractura en costilla derecha'),
(9, 9, '2024-01-09 10:30:00', 'Infección urinaria detectada'),
(10, 10, '2024-01-10 10:30:00', 'Densidad ósea baja');

-- Inserts para la Tabla ExamenEnfermedad
INSERT INTO ExamenEnfermedad (ExamenId, EnfermedadId) VALUES
(1, 3),
(2, 8),
(3, 7),
(4, 9),
(5, 5),
(6, 7),
(7, 6),
(8, 4),
(9, 1),
(10, 7);
