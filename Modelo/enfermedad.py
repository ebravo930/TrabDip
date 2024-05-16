import psycopg2 as psy
import config

class Enfermedad:
    def __init__(self,nombre='', descripcion=''):
        self.__nombre = nombre
        self.__descripcion = descripcion

  
    def GetNombre(self):
        return self.__nombre
    def GetDescripcion(self):
        return self.__descripcion
    
    def SetNombre(self,nombre):
        self.__nombre = nombre
    def SetDescripcion(self,descripcion):
        self.__descripcion = descripcion


def conectar_bd():
    try:
        conexion = psy.connect(host=config.host,database=config.database,user=config.user,password=config.password)
        return conexion
    except psy.Error as error:
        print("Error al conectar a la base de datos:", error)
        return None