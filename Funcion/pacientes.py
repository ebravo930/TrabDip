# Paciente
import os
from Modelo.paciente import *

def clear_screen():
    """Limpia la pantalla de la consola para diferentes sistemas operativos."""
    os.system('cls' if os.name == 'nt' else 'clear')

def NuevoPaciente():
    clear_screen()
    pacientes=[]
    while True:
        print("-" * 80)
        l=Paciente()

        rut = input('Ingresa Rut Paciente: \n')
        if len(rut.strip()) == 0:
            print("Rut no valido. Por favor, ingresa un Rut válido. Volviendo al menu principal")
            punto_interrupcion()
            break
        l.SetRut(rut)

        nombre = input('Ingresa Nombre Paciente: \n')
        if len(nombre.strip()) == 0:
            print("Nombre no valido. Por favor, ingresa un Nombre válido. Volviendo al menu principal")
            punto_interrupcion()
            break
        l.SetNombre(nombre)

        pacientes.append(l)
        print("-" * 80)
        for paciente in pacientes:
            InsPac(paciente)
        break

def VerPaciente():
    clear_screen()   
    print("-" * 80)
    ListarPac()    
    print("-" * 80)
    opcion = input('Ingresa:  1 para volver al menu | 2 Para editar datos Paciente \n \n ')

    if opcion == '1':
        print("Volviendo al Menu Principal")

    elif opcion == '2':
        print("Editar Medico")
        EditarPaciente()
        # ListarPac() 
    else:
        print("Opción inválida. Volviendo al Menu Principal")

def EditarPaciente():
    # clear_screen()
    pacientes=[]
    while True:
        l=Paciente()

        rut = input('Ingresa RUT Paciente a editar: \n')
        if len(rut.strip()) == 0:
            print("RUT no valido. Por favor, ingresa un RUT válido. Volviendo al menu principal")
            punto_interrupcion()
            break
        l.SetRut(rut)
        
        nombre = input('Ingresa Nombre Paciente: \n')
        if len(nombre.strip()) == 0:
            print("Nombre no valido. Por favor, ingresa un Nombre válido. Volviendo al menu principal")
            punto_interrupcion()
            break
        l.SetNombre(nombre)

        pacientes.append(l)
        for paciente in pacientes:
            EditaPaciente(paciente)
        break #finaliza el ciclo