
# tiene solo insertar


# tiene solo insertar


# tiene solo insertar


# Falta implementa 





# CREATE TABLE Visita (
#     VisitaId SERIAL PRIMARY KEY,
#     PacienteId INT NOT NULL,
#     FechaEntrada TIMESTAMP NOT NULL,
#     FechaSalida TIMESTAMP,
#     MedicoId INT NOT NULL,
#     CamaId INT NOT NULL,
#     FOREIGN KEY (PacienteId) REFERENCES Paciente(PacienteId),
#     FOREIGN KEY (MedicoId) REFERENCES Medico(MedicoId),
#     FOREIGN KEY (CamaId) REFERENCES Cama(CamaId)
# );

# -- Tabla Diagnostico (nueva tabla)
# CREATE TABLE Diagnostico (
#     DiagnosticoId SERIAL PRIMARY KEY,
#     VisitaId INT NOT NULL,
#     EnfermedadId INT NOT NULL,
#     Descripcion TEXT,
#     FOREIGN KEY (VisitaId) REFERENCES Visita(VisitaId),
#     FOREIGN KEY (EnfermedadId) REFERENCES Enfermedad(EnfermedadId)

# -- Tabla VisitaExamen
# CREATE TABLE VisitaExamen (
#     VisitaId INT NOT NULL,
#     ExamenId INT NOT NULL,
#     Fecha TIMESTAMP NOT NULL,
#     Resultado TEXT,
#     PRIMARY KEY (VisitaId, ExamenId),
#     FOREIGN KEY (VisitaId) REFERENCES Visita(VisitaId),
#     FOREIGN KEY (ExamenId) REFERENCES Examen(ExamenId)
# );

# -- Relación Examen-Enfermedad (tabla de unión)
# CREATE TABLE ExamenEnfermedad (
#     ExamenId INT NOT NULL,
#     EnfermedadId INT NOT NULL,
#     PRIMARY KEY (ExamenId, EnfermedadId),
#     FOREIGN KEY (ExamenId) REFERENCES Examen(ExamenId),
#     FOREIGN KEY (EnfermedadId) REFERENCES Enfermedad(EnfermedadId)
# );