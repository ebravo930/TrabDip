# Paciente
import os
from Modelo.paciente import *

def clear_screen():
    """Limpia la pantalla de la consola para diferentes sistemas operativos."""
    os.system('cls' if os.name == 'nt' else 'clear')

def NuevoPaciente():
    pacientes=[]
    while True:
        l=Paciente()
        l.SetRut(input('Ingresa Rut Paciente: \n'))
        l.SetNombre(input('Ingresa Nombre Paciente: \n'))
        pacientes.append(l)
        for paciente in pacientes:
            InsPac(paciente)
        break

def VerPaciente():
    os.system('cls' if os.name == 'nt' else 'clear')
    ListarPac()
    print("")
    opcion = input('Ingresa:  1 para volver al menu | 2 Para editar datos Paciente \n \n ')

    if opcion == '1':
        print("Volviendo al Menu Principal")

    elif opcion == '2':
        print("Editar Medico")
        # EditarPaciente()
        ListarPac()
    
    else:
        print("Opción inválida. Volviendo al Menu Principal")