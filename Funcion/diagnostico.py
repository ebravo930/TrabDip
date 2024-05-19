import os
from Modelo.diagnostico import *

def clear_screen():
    """Limpia la pantalla de la consola para diferentes sistemas operativos."""
    os.system('cls' if os.name == 'nt' else 'clear')

def NuevoDagnostico():
    clear_screen()
    diagnosticos=[]
    while True:
        print("-" * 80)
        l=Diagnostico()

        descripcion = input('Ingresa descripcion diagnostico: \n')
        if len(descripcion.strip()) == 0:
            print("Descripcion no valida. Por favor, ingresa un Descripcion válido. Volviendo al menu principal")
            punto_interrupcion()
            break
        l.SetDescripcion(descripcion)

        diagnosticos.append(l)
        print("-" * 80)
        for diagnostico in diagnosticos:
            InsertarDiagnostico(diagnostico)
        break