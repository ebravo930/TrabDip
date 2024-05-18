import os

from Funcion.habitaciones import VerHabitacion
from Modelo.cama import *
from Modelo.habitacion import *

def clear_screen():
    """Limpia la pantalla de la consola para diferentes sistemas operativos."""
    os.system('cls' if os.name == 'nt' else 'clear')

def NuevoCama():
    VerHabitacion()
    camas=[]
    while True:
        #Creo por cada vuelta del ciclo una instancia de la clase libro asi no voy remplazando el anterior.
        l=Cama()
        l.SetHabitacion(input('Ingresa Nuemro de la Habitacion asignada: \n'))
        camas.append(l)
        for cama in camas:
            InsCama(cama)
        break #finaliza el ciclo

def VerCama():
    clear_screen()
    ListarCama()
    

    # print("")
    # opcion = input('Ingresa:  1 para volver al menu | 2 Para Mover cama de habitacion \n \n ')

    # if opcion == '1':
    #     print("Volviendo al Menu Principal")

    # elif opcion == '2':
    #     print("Mover cama de habitacion")
    #     VerHabitacion()
    #     # MoverCamas()
        
    # else:
    #     print("Opción inválida. Volviendo al Menu Principal")

    punto_interrupcion()

# def MoverCamas():
#     camas=[]
#     while True:
#         l=Cama()
#         l.SetHabitacion_origen(input('Ingresa habitacion Origen : \n'))
#         l.SetHabitacion(input('Ingresa habitacion Destino : \n'))
#         camas.append(l)
#         for cama in camas:
#             MoverCama(cama)
#         break #finaliza el ciclo
