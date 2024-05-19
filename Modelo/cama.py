import psycopg2 as psy
import config
from Modelo.habitacion import *

class Cama:
    def __init__(self,habitacion='',habitacion_origen=''):
        
        self.__habitacion = habitacion
        self.__habitacion_origen = habitacion_origen        

    def GetHabitacion(self):
        return self.__habitacion
    
    def GetHabitacion_origen(self):
        return self.__habitacion_origen

    def SetHabitacion(self,habitacion):
        self.__habitacion = habitacion

    def SetHabitacion_origen(self,habitacion_origen):
        self.__habitacion_origen = habitacion_origen

def punto_interrupcion():
    input("Presiona una tecla para continuar...")

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

        habitacionexiste = valida_habitacion_existe(l.GetHabitacion())
        capacidadhabitacion = valida_habitacion_capacidad(l.GetHabitacion())

        if  capacidadhabitacion:
            print("La Habitacion ingresado, excede su capacidad")
            punto_interrupcion()
        
        elif not habitacionexiste:
            idHabitacion = obtener_id_habitacion(l.GetHabitacion())
            # print("Habitacion ID", idHabitacion)
            query = "INSERT INTO Cama (habitacionid, disponibilidad) VALUES(%s,%s);"
            cursor.execute(query, (idHabitacion, True,))
            conexion.commit()

            if cursor.rowcount > 0:
                print("Cama ingresado con exito.")
            else:
                print("Error al ingresar al Cama.")
            
            punto_interrupcion()
        else:
            print("La Habitacion ingresado, no se encuentra en nuestros registros")
            punto_interrupcion()

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
