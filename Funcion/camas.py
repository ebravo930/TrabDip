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
    os.system('cls' if os.name == 'nt' else 'clear')
    ListarCama()


