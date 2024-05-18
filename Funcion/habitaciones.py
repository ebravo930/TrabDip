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

        numero = input('Ingresa Nuemro de la Habitacion: \n')
        if not validar_entero(numero):
            print("Nuemro no valido. Por favor, ingresa un Nuemro válido. Volviendo al menu principal")
            punto_interrupcion()
            break
        l.SetNumero(numero)

        capacidad = input('Ingresa capacidad de camas \n')
        if not validar_entero(capacidad):
            print("Capacidad no valido. Por favor, ingresa un Capacidad válido. Volviendo al menu principal")
            punto_interrupcion()
            break 
        l.SetCapacidad(capacidad)

        habitaciones.append(l)
        for habitacion in habitaciones:
            insHabitacion(habitacion)
        break #finaliza el ciclo

def VerHabitacion():
    ListarHab()

def validar_entero(dato):
    if dato.strip() == "":
        return False  # Cadena vacía
    if dato.isdigit():
        return True   # Es un entero
    else:
        return False  # No es un entero