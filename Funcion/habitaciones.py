import os
from Modelo.habitacion import *

def clear_screen():
    """Limpia la pantalla de la consola para diferentes sistemas operativos."""
    os.system('cls' if os.name == 'nt' else 'clear')

def NuevaHabitacion():
    habitaciones=[]
    while True:
        #Creo por cada vuelta del ciclo una instancia de la clase libro asi no voy remplazando el anterior.
        l=Habitacion()
        l.SetNumero(input('Ingresa Nuemro de la Habitacion: \n'))
        l.SetCapacidad(input('Ingresa capacidad de camas \n'))
        habitaciones.append(l)
        for habitacion in habitaciones:
            insHabitacion(habitacion)
        break #finaliza el ciclo

def VerHabitacion():
    os.system('cls' if os.name == 'nt' else 'clear')
    ListarHab()