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
        l.SetNombre(input('Ingresa Nombre Medico: \n'))
        l.SetEspecialidad(input('Ingresa Especialidad Medico: \n'))
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
    clear_screen()
    medicos=[]
    while True:
        #Creo por cada vuelta del ciclo una instancia de la clase libro asi no voy remplazando el anterior.
        l=Medico()
        l.SetMedicoid(input('Ingresa ID Medico a editar: \n'))
        l.SetNombre(input('Ingresa Nombre Medico: \n'))
        l.SetEspecialidad(input('Ingresa Especialidad Medico: \n'))
        medicos.append(l)
        for medico in medicos:
            EditaMedico(medico)
        break #finaliza el ciclo

def CambiarEstadoMedico():
    clear_screen()
    medicos=[]
    while True:
        #Creo por cada vuelta del ciclo una instancia de la clase libro asi no voy remplazando el anterior.
        l=Medico()
        l.SetMedicoid(input('Ingresa ID Medico: \n'))
        medicos.append(l)
        for medico in medicos:
            CambiaEstado(medico)
        break #finaliza el ciclo