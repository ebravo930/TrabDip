from Funcion.medicos import *
from Funcion.pacientes import *
from Funcion.habitaciones import *
from Funcion.camas import *
from Funcion.visitas import *
from Funcion.enfermedad import *
from Funcion.diagnostico import *
import os

def clear_screen():
    """Limpia la pantalla de la consola para diferentes sistemas operativos."""
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    while True:
        clear_screen()
        print("Sistema de Gestión Hospitalaria")
        print("1. Gestionar Pacientes")
        print("2. Gestionar Médicos")
        print("3. Gestionar Visitas")
        print("4. Gestionar Enfermedad")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            gestionar_pacientes()
        elif opcion == '2':
            gestionar_medicos()
        elif opcion == '3':
            gestionar_visitas()
        elif opcion == '4':
            gestionar_enfermedad()
        elif opcion == '5':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Por favor intente nuevamente.")
            input("Presiona Enter para continuar...")

def gestionar_pacientes():
    while True:
        clear_screen()
        print("Gestión de Pacientes")
        print("1. Agregar Nuevo Paciente")
        print("2. Ver Pacientes")
        print("3. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            NuevoPaciente()
        elif opcion == '2':
            VerPaciente()
        elif opcion == '3':
            break
        else:
            print("Opción no válida.")
            input("Presiona Enter para continuar...")

def gestionar_medicos():
    while True:
        clear_screen()
        print("Gestión de Médicos")
        print("1. Agregar Nuevo Médico")
        print("2. Ver Médicos")
        print("3. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            NuevoMedico()
        elif opcion == '2':
            VerMedicos()
        elif opcion == '3':
            break
        else:
            print("Opción no válida.")
            input("Presiona Enter para continuar...")

def gestionar_visitas():
    while True:
        clear_screen()
        print("Gestión de Visitas")
        print("1. Agregar Nueva Visita")
        print("2. Ver Visitas")
        print("3. Actualizar Visita")
        print("4. Eliminar Visita")
        print("5. Ingresar Diagnostico")
        print("6. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_visita()
        elif opcion == '2':
            ver_visitas()
        elif opcion == '3':
            actualizar_visita()
        elif opcion == '4':
            eliminar_visita()
        elif opcion == '5':
            NuevoDagnostico()
        elif opcion == '6':
            break
        else:
            print("Opción no válida.")
            input("Presiona Enter para continuar...")

def gestionar_enfermedad():
    while True:
        clear_screen()
        print("Gestión de Enfermedad")
        print("1. Agregar nueva enfermedad")
        print("2. Ver enfermedades")
        print("3. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            NuevaEnfermedad()
        elif opcion == '2':
            VerEnfermedades()
        elif opcion == '3':
            break
        else:
            print("Opción no válida.")
            input("Presiona Enter para continuar...")

if __name__ == "__main__":
    main_menu()