import os
from Modelo.medico import *


def clear_screen():
    """Limpia la pantalla de la consola para diferentes sistemas operativos."""
    os.system('cls' if os.name == 'nt' else 'clear')

def NuevoMedico():
    clear_screen()
    medicos=[]
    while True:
        #Creo por cada vuelta del ciclo una instancia de la clase libro asi no voy remplazando el anterior.
        l=Medico()

        nombre = input('Ingresa Nombre Medico: \n')
        if len(nombre.strip()) == 0:
            print("Nombre no valido. Por favor, ingresa un Nombre válido. Volviendo al menu principal")
            punto_interrupcion()
            break
        l.SetNombre(nombre)

        especialidad = input('Ingresa Especialidad Medico: \n')
        if len(especialidad.strip()) == 0:
            print("Especialidad no valido. Por favor, ingresa un Especialidad válido. Volviendo al menu principal")
            punto_interrupcion()
            break

        l.SetEspecialidad(especialidad)
        medicos.append(l)
        for medico in medicos:
            InsMedico(medico)
        break #finaliza el ciclo

def VerMedicos():
    clear_screen()
    ListarMedicos()
    print("")
    opcion = input('Ingresa:  1 para volver al menu | 2 Para editar datos medico | 3 Para cambiar estado Vigente medico   \n \n ')

    if opcion == '1':
        print("Volviendo al Menu Principal")

    elif opcion == '2':
        print("Editar Medico")
        EditarMedico()
        ListarMedicos()

    elif opcion == '3':
        print("Cambiar Estado")
        CambiarEstadoMedico()
        ListarMedicos()
    
    else:
        print("Opción inválida. Volviendo al Menu Principal")

def EditarMedico():
    # clear_screen()
    medicos=[]
    while True:

        l=Medico()

        id = input('Ingresa ID Medico a editar: \n')
        if len(id.strip()) == 0:
            print("ID no valido. Por favor, ingresa un ID válido. Volviendo al menu principal")
            punto_interrupcion()
            break
        l.SetMedicoid(id)
        
        nombre = input('Ingresa Nombre Medico: \n')
        if len(nombre.strip()) == 0:
            print("Nombre no valido. Por favor, ingresa un Nombre válido. Volviendo al menu principal")
            punto_interrupcion()
            break
        l.SetNombre(nombre)

        especialidad = input('Ingresa Especialidad Medico: \n')
        if len(especialidad.strip()) == 0:
            print("Especialidad no valido. Por favor, ingresa un Especialidad válido. Volviendo al menu principal")
            punto_interrupcion()
            break
        l.SetEspecialidad(especialidad)

        medicos.append(l)
        for medico in medicos:
            EditaMedico(medico)
        break #finaliza el ciclo

def CambiarEstadoMedico():
    # clear_screen()
    medicos=[]
    while True:
        #Creo por cada vuelta del ciclo una instancia de la clase libro asi no voy remplazando el anterior.
        l=Medico()
        l.SetMedicoid(input('Ingresa ID Medico: \n'))
        medicos.append(l)
        for medico in medicos:
            CambiaEstado(medico)
        break #finaliza el ciclo