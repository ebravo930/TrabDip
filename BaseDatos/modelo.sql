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
