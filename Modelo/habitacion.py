import psycopg2 as psy
import config

class Habitacion:
    def __init__(self,numero='', capacidad=''):
        self.__numero = numero
        self.__capacidad = capacidad

     
    def GetNumero(self):
        return self.__numero
    def GetCapacidad(self):
        return self.__capacidad
    
    def SetNumero(self,numero):
        self.__numero = numero
    def SetCapacidad(self,capacidad):
        self.__capacidad = capacidad


def conectar_bd():
    try:
        conexion = psy.connect(host=config.host,database=config.database,user=config.user,password=config.password)
        return conexion
    except psy.Error as error:
        print("Error al conectar a la base de datos:", error)
        return None
    

def insHabitacion(l):
    try:
        conexion = conectar_bd()
        cursor = conexion.cursor()
        query = "INSERT INTO habitacion (numero, capacidad) VALUES(%s,%s);"
        cursor.execute(query, (l.GetNumero(),l.GetCapacidad(),))
        conexion.commit()

    except psy.Error as error:
        print("Error al ejecutar la consulta:", error)

    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()

def ListarHab():
    try:
        conexion = conectar_bd()
        cursor = conexion.cursor()
        query = """
                        SELECT 
                        habitacionid,
                        numero , 
                        capacidad,
                        (
                            SELECT COUNT(*) 
                            FROM cama 
                            WHERE habitacion.habitacionid = cama.habitacionid
                        ) AS Camas_habitacion
                    FROM 
                        habitacion
                """
        cursor.execute(query)
        # -------------------------------------------------------------------------------
        if cursor.rowcount > 0:#rowcount cuenta la cantidad de filas.
            print("-" * 80)
            print("Habitaciones")
            print("Numero Hab. \t| Capacidad \t| Camas Asignadas \t|[",cursor.rowcount,"]")
            print("-" * 80)
            row = cursor.fetchone() #Itera en el resultado, obtenidno los datos de la sigueinte fila
            while row is not None:
                print(f'{str(row[1])} \t\t| {str(row[2])} \t\t| {str(row[3])}')
                row = cursor.fetchone()
        else:
            print('No existen registros en la base de datos')
        # -------------------------------------------------------------------------------
    except psy.Error as error:
        print("Error al ejecutar la consulta: ", error)

    finally:
        cursor.close()
        conexion.close()

def obtener_id_habitacion(habitacion):
    try:
        conexion = conectar_bd()
        cursor = conexion.cursor()
        query = "select habitacionid from habitacion  where numero = %s;"
        cursor.execute(query, (habitacion,))
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
