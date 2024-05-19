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
    
def punto_interrupcion():
    input("Presiona una tecla para continuar...")

def InsertarEnfermedad(l):
    try:
        conexion = conectar_bd()
        cursor = conexion.cursor()

        enfermedadexiste = valida_Enfermedad_existe(l.GetNombre())
        if enfermedadexiste:

            query = "INSERT INTO enfermedad ( nombre, descripcion) VALUES(%s,%s);"
            cursor.execute(query, (l.GetNombre(),l.GetDescripcion(),))
            conexion.commit()

            if cursor.rowcount > 0:
                print("Enfermedad ingresado con exito.")
            else:
                print("Error al ingresar la Enfermedad.")

        else:
            print("El Nombre ingresado, ya se encuentra en nuestros registros, Enfermedad no ingresada")
            punto_interrupcion()
    except psy.Error as error:
        print("Error al ejecutar la consulta:", error)

    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()

def ListarEnfermedad():
    try:
        conexion = conectar_bd()
        cursor = conexion.cursor()
        query = "select enfermedadid,nombre,descripcion from enfermedad"
        cursor.execute(query)
        # -------------------------------------------------------------------------------
        if cursor.rowcount > 0:#rowcount cuenta la cantidad de filas.
            print("-" * 80)
            print("Lista de Enfermedades")
            print("ID \t|Nombre \t\t| Descripcion \t|[",cursor.rowcount,"]")
            print("-" * 80)
            row = cursor.fetchone() #Itera en el resultado, obtenidno los datos de la sigueinte fila
            while row is not None:
                print(f'{str(row[0])} \t|{str(row[1])} \t| {str(row[2])}')
                row = cursor.fetchone()
            print('\n')
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

def valida_Enfermedad_existe(nombreenfermedad):
    try:
        conexion = conectar_bd()
        cursor = conexion.cursor()
        query = "SELECT nombre FROM enfermedad WHERE UPPER(nombre)  = %s;"
        cursor.execute(query, (nombreenfermedad.upper(),))

        if cursor.rowcount > 0:
            return False
        else:
            return True
            
    except psy.Error as error:
        print("Error al ejecutar la consulta: ", error)

    except TypeError as e:
        print("Error al ejecutar la consulta: ",e)

    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()