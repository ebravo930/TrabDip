import psycopg2 as psy
import config

class Diagnostico:   
    def __init__(self,visitaid='', enfermedadid='' , descripcion=''):
        self.__visitaid = visitaid
        self.__enfermedadid = enfermedadid
        self.__descripcion = descripcion

    def GetVisitaid(self):
        return self.__visitaid
    def GetEnfermedadid(self):
        return self.__enfermedadid
    def GetDescripcion(self):
        return self.__descripcion
    
    def SetVisitaid(self,visitaid):
        self.__visitaid = visitaid
    def SetEnfermedadid(self,enfermedadid):
        self.__enfermedadid = enfermedadid
    def SetDescripcion(self,descripcion):
        self.__descripcion = descripcion

def conectar_bd():
    try:
        conexion = psy.connect(host=config.host,database=config.database,user=config.user,password=config.password)
        return conexion
    except psy.Error as error:
        print("Error al conectar a la base de datos:", error)
        return None
    
def punto_interrupcion():
    input("Presiona una tecla para continuar...")

def InsertarDiagnostico(l):
    try:
        conexion = conectar_bd()
        cursor = conexion.cursor()
        query = "INSERT INTO diagnostico (visitaid, enfermedadid, descripcion) VALUES(%s,%s,%s);"
        cursor.execute(query, (1, 1, l.GetDescripcion(),))
        conexion.commit()

        if cursor.rowcount > 0:
            print("Diagnostico ingresado con exito.")
        else:
            print("Error al ingresar al Diagnostico.")
            
        punto_interrupcion()
    except psy.Error as error:
        print("Error al ejecutar la consulta:", error)

    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()