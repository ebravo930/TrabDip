import psycopg2 as psy
import config
from Modelo.habitacion import *

class Cama:
    def __init__(self,habitacion=''):
        
        self.__habitacion = habitacion

    def GetHabitacion(self):
        return self.__habitacion

    def SetHabitacion(self,habitacion):
        self.__habitacion = habitacion


def conectar_bd():
    try:
        conexion = psy.connect(host=config.host,database=config.database,user=config.user,password=config.password)
        return conexion
    except psy.Error as error:
        print("Error al conectar a la base de datos:", error)
        return None
    

def InsCama(l):
    try:
        conexion = conectar_bd()
        cursor = conexion.cursor()
        idHabitacion = obtener_id_habitacion(l.GetHabitacion())
        print("Habitacion ID", idHabitacion)
        query = "INSERT INTO Cama (habitacionid, disponibilidad) VALUES(%s,%s);"
        cursor.execute(query, (idHabitacion, True,))
        conexion.commit()

    except psy.Error as error:
        print("Error al ejecutar la consulta:", error)

    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()
    
def ListarCama():
    try:
        conexion = conectar_bd()
        cursor = conexion.cursor()
        query = """
        	select habitacion.numero, camaid, disponibilidad from cama 
	        inner join habitacion on habitacion.habitacionid = cama.habitacionid
        """
        cursor.execute(query)
        # -------------------------------------------------------------------------------
        if cursor.rowcount > 0:#rowcount cuenta la cantidad de filas.
            print("-" * 80)
            print("Habitacion \t| Cama \t\t| Estado \t\t| Total [",cursor.rowcount,"]")
            print("-" * 80)
            row = cursor.fetchone() #Itera en el resultado, obtenidno los datos de la sigueinte fila
            while row is not None:
                print(f'{str(row[0])} \t\t| {str(row[1])} \t\t| {str(row[2])}')
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
