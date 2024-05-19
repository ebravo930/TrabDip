import psycopg2
import config

class Visita:
    def __init__(self, visita_id=None, paciente_id=None, medico_id=None, cama_id=None, fecha_entrada=None, fecha_salida=None):
        self.visita_id = visita_id
        self.paciente_id = paciente_id
        self.medico_id = medico_id
        self.cama_id = cama_id
        self.fecha_entrada = fecha_entrada
        self.fecha_salida = fecha_salida

    def set_datos(self, paciente_id, medico_id, cama_id, fecha_entrada, fecha_salida):
        self.paciente_id = paciente_id
        self.medico_id = medico_id
        self.cama_id = cama_id
        self.fecha_entrada = fecha_entrada
        self.fecha_salida = fecha_salida

def conectar_bd():
    try:
        return psycopg2.connect(host=config.host, database=config.database, user=config.user, password=config.password)
    except psycopg2.Error as e:
        print("Error conectando a la base de datos: ", e)
        return None

def agregar_visita(visita):
    conexion = conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        query = "INSERT INTO Visita (paciente_id, medico_id, cama_id, fecha_entrada, fecha_salida) VALUES (%s, %s, %s, %s, %s) RETURNING visita_id;"
        try:
            cursor.execute(query, (visita.paciente_id, visita.medico_id, visita.cama_id, visita.fecha_entrada, visita.fecha_salida))
            visita_id = cursor.fetchone()[0]
            conexion.commit()
            print("Visita agregada con ID:", visita_id)
            return visita_id
        except psycopg2.Error as e:
            print("Error al agregar visita: ", e)
            conexion.rollback()
        finally:
            cursor.close()
            conexion.close()

def listar_visitas():
    conexion = conectar_bd()
    if conexion:
        cursor = conexion.cursor()
        try:
            # Se realiza una consulta que une las tablas Visita, Paciente y Medico para obtener los nombres
            query = """
                SELECT p.Nombre AS NombrePaciente, m.Nombre AS NombreMedico, v.FechaEntrada, v.FechaSalida
                FROM Visita v
                JOIN Paciente p ON v.PacienteId = p.PacienteId
                JOIN Medico m ON v.MedicoId = m.MedicoId;
            """
            cursor.execute(query)
            visitas = cursor.fetchall()
            # Formatear la salida para una mejor legibilidad
            if visitas:
                for visita in visitas:
                    nombre_paciente, nombre_medico, fecha_entrada, fecha_salida = visita
                    print(f"Paciente: {nombre_paciente}, Médico: {nombre_medico}, Fecha de entrada: {fecha_entrada}, Fecha de salida: {fecha_salida}")
            else:
                print("No se encontraron visitas.")
        except psycopg2.Error as e:
            print("Error al listar visitas: ", e)
        finally:
            cursor.close()
            conexion.close()

