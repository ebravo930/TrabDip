from Funcion.medicos import NuevoMedico, VerMedicos
from Funcion.pacientes import NuevoPaciente, VerPaciente
from Funcion.habitaciones import NuevaHabitacion, VerHabitacion
from Funcion.camas import NuevoCama, VerCama

import os
#from funciones import NuevoMedico, VerMedicos, NuevoPaciente, VerPaciente, NuevaHabitacion, NuevoCama, VerHabitacion, VerCama

def clear_screen():
    """Limpia la pantalla de la consola para diferentes sistemas operativos."""
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    while True:
        clear_screen()
        print("-" * 80)
        print("Sistema de Gestión de Clínica")
        print("1. Médicos")
        print("   1.1 Ingresar médico     | 1.2 Listar médicos")
        print("2. Pacientes")
        print("   2.1 Ingresar paciente   | 2.2 Listar pacientes")
        print("3. Habitación")
        print("   3.1 Ingresar habitación | 3.2 Listar habitación")
        print("4. Cama")
        print("   4.1 Ingresar Cama       | 4.2 Listar cama")
        print("5. Salir")
        print("-" * 80)

        opcion = input("Ingrese una opción: ").strip()
        clear_screen()
        if opcion == '1.1':
            NuevoMedico()
        elif opcion == '1.2':
            VerMedicos()
        elif opcion == '2.1':
            NuevoPaciente()
        elif opcion == '2.2':
            VerPaciente()
        elif opcion == '3.1':
            NuevaHabitacion()
        elif opcion == '3.2':
            VerHabitacion()
        elif opcion == '4.1':
            NuevoCama()
        elif opcion == '4.2':
            VerCama()
        elif opcion == '5':
            print("Saliendo...")
            break
        else:
            clear_screen()
            print("Opción inválida. Por favor, seleccione una opción válida.")
            input("Presione Enter para continuar...")  # Pausa para que el usuario vea el mensaje

if __name__ == "__main__":
    menu()
