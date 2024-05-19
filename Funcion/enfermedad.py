import os
from Modelo.enfermedad import *

def clear_screen():
    """Limpia la pantalla de la consola para diferentes sistemas operativos."""
    os.system('cls' if os.name == 'nt' else 'clear')
    
def NuevaEnfermedad():
    clear_screen()
    ListarEnfermedad()
    print("")
    enfermedades=[]
    while True:
        print("-" * 80)
        l=Enfermedad()

        nombre = input('Ingresa nombre enfermedad, Verifique que este no se encuentre en los registros: \n')
        if len(nombre.strip()) == 0:
            print("Nombre no valida. Por favor, ingresa un Nombre válido. Volviendo al menu principal")
            punto_interrupcion()
            break
        l.SetNombre(nombre)

        descripcion = input('Ingresa descripcion enfermedad: \n')
        if len(descripcion.strip()) == 0:
            print("Descripcion no valida. Por favor, ingresa un Descripcion válido. Volviendo al menu principal")
            punto_interrupcion()
            break
        l.SetDescripcion(descripcion)

        enfermedades.append(l)
        print("-" * 80)
        for enfermedad in enfermedades:
            InsertarEnfermedad(enfermedad)
        break

def VerEnfermedades():
    clear_screen()
    ListarEnfermedad()
    punto_interrupcion()