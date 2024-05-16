import psycopg2 as psy
import config

class Medico:
    def __init__(self,medicoid='' ,nombre='',especialidad='', vigente=''):
        
        self.__medicoid = medicoid
        self.__nombre = nombre
        self.__especialidad = especialidad
        self.__vigente = vigente        
    
    def GetMedicoid(self):
        return self.__medicoid
    def GetNombre(self):
        return self.__nombre
    def GetEspecialidad(self):
        return self.__especialidad
    def GetVigente(self):
        return self.__vigente
    
    def SetMedicoid(self,medicoid):
        self.__medicoid = medicoid
    def SetNombre(self,nombre):
        self.__nombre = nombre
    def SetEspecialidad(self,especialidad):
        self.__especialidad = especialidad
    def SetVigente(self,vigente):
        self.__vigente = vigente
            
            
    # def ShowData(self):
    #     print(f'Titulo:{self.__titulo}\nAutor:{self.__autor}')
    
def conectar_bd():
    try:
        conexion = psy.connect(host=config.host,database=config.database,user=config.user,password=config.password)
        return conexion
    except psy.Error as error:
        print("Error al conectar a la base de datos:", error)
        return None

def InsMedico(l):
    try:
        conexion = conectar_bd()
        cursor = conexion.cursor()
        query = "INSERT INTO medico (Nombre,Especialidad,Vigente) VALUES(%s,%s,%s);"
        cursor.execute(query, (l.GetNombre(), l.GetEspecialidad(), True))
        conexion.commit()

    except psy.Error as error:
        print("Error al ejecutar la consulta:", error)

    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()       

def ListarMedicos():
    try:
        conexion = conectar_bd()
        cursor = conexion.cursor()
        query = "select medicoid, Nombre, especialidad , Vigente from medico"
        cursor.execute(query)
        # -------------------------------------------------------------------------------
        if cursor.rowcount > 0:#rowcount cuenta la cantidad de filas.
            print("-" * 80)
            print("Profesionales Medicos")
            print("ID \t|Nombre \t\t| Especialidad \t| Vigente \t|[",cursor.rowcount,"]")
            print("-" * 80)
            row = cursor.fetchone() #Itera en el resultado, obtenidno los datos de la sigueinte fila
            while row is not None:
                print(f'{str(row[0])} \t|{str(row[1])} \t| {str(row[2])} \t| {str(row[3])}')
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

def CambiaEstado(l):
    try:
        conexion = conectar_bd()
        cursor = conexion.cursor()
        estado = obtener_estado_medico(l.GetMedicoid())

        query = """
                UPDATE public.medico
                SET  vigente = %s 
                WHERE medicoid = %s ;
        """
        if estado == True:
            cursor.execute(query, (False, l.GetMedicoid(),))
        else:
            cursor.execute(query, (True, l.GetMedicoid(),))

        conexion.commit()

    except psy.Error as error:
        print("Error al ejecutar la consulta:", error)

    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close() 

def obtener_estado_medico(medicoid):
    try:
        conexion = conectar_bd()
        cursor = conexion.cursor()
        query = "select vigente from medico where medicoid = %s;"
        cursor.execute(query, (medicoid))
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

def EditaMedico(l):
    try:
        conexion = conectar_bd()
        cursor = conexion.cursor()
        query = """
            UPDATE public.medico
            SET nombre  = %s ,
                especialidad = %s 
                WHERE medicoid = %s
        """
        cursor.execute(query, (l.GetNombre(), l.GetEspecialidad(), l.GetMedicoid()))
        conexion.commit()

    except psy.Error as error:
        print("Error al ejecutar la consulta:", error)

    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close() 

