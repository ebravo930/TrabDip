import psycopg2 as psy
import config

class Paciente:
    def __init__(self,rut='',nombre=''):
        self.__rut = rut
        self.__nombre = nombre

    def GetRut(self):
        return self.__rut
    def GetNombre(self):
        return self.__nombre
    
    def SetRut(self,rut):
        self.__rut = rut
    def SetNombre(self,nombre):
        self.__nombre = nombre

def conectar_bd():
    try:
        conexion = psy.connect(host=config.host,database=config.database,user=config.user,password=config.password)
        return conexion
    except psy.Error as error:
        print("Error al conectar a la base de datos:", error)
        return None

def obtener_id_paciente(rut):
    try:
        conexion = conectar_bd()
        cursor = conexion.cursor()
        query = "SELECT id FROM paciente WHERE rut = %s;"
        cursor.execute(query, (rut,))
        # -------------------------------------------------------------------------------
        return cursor.fetchone()[0]
        # -------------------------------------------------------------------------------
    except psy.Error as error:
        print("Error al ejecutar la consulta: ", error)

    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()

def InsPac(l):
    try:
        conexion = conectar_bd()
        cursor = conexion.cursor()
        query = "INSERT INTO Paciente (rut, nombre) VALUES(%s,%s);"
        cursor.execute(query, (l.GetRut(), l.GetNombre()))
        conexion.commit()

    except psy.Error as error:
        print("Error al ejecutar la consulta:", error)

    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()

def ListarPac():
    try:
        conexion = conectar_bd()
        cursor = conexion.cursor()
        query = """
            select rut, nombre from paciente
        """
        cursor.execute(query)
        # -------------------------------------------------------------------------------
        if cursor.rowcount > 0:
            print("-" * 80)
            print("|"," " * 28, "Lista de Pacientes", " " * 28,"|")
            print("-" * 80)
            print("RUT \t| Nombre \t\t| Total Paciente[",cursor.rowcount,"]")
            print("-" * 80)
            row = cursor.fetchone() #Itera en el resultado, obtenidno los datos de la sigueinte fila
            while row is not None:
                print(f'{str(row[0])} \t| {str(row[1])}')
                row = cursor.fetchone()
        else:
            print('No existen registros en la base de datos')
        # -------------------------------------------------------------------------------
    except psy.Error as error:
        print("Error al ejecutar la consulta:", error)

    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()