from Modelo.paciente import *
from Modelo.medico import *
from Modelo.cama import *
from Modelo.visita import *

def seleccionar_opcion(elementos):
    """ Muestra las opciones y retorna la elección válida del usuario. """
    for elemento in elementos:
        print(f"{elemento[0]}. {elemento[1]}")
    seleccion = input("Seleccione una opción de la lista: ")
    while seleccion not in [str(elem[0]) for elem in elementos]:
        print("Selección inválida. Intente de nuevo.")
        seleccion = input("Seleccione una opción de la lista: ")
    return seleccion

def agregar_visita():
    print("Agregar Nueva Visita")
    # Lista de pacientes
    pacientes = ListarPac()
    print("Seleccione un paciente de la lista:")
    paciente_id = seleccionar_opcion(pacientes)

    # Lista de médicos
    medicos = ListarMedicos()
    print("Seleccione un médico tratante de la lista:")
    medico_id = seleccionar_opcion(medicos)

    # Lista de camas disponibles
    camas = ListarCama()
    print("Seleccione una cama disponible de la lista:")
    cama_id = seleccionar_opcion(camas)

    # Agregar la visita a la base de datos
    resultado = agregar_visita(paciente_id, medico_id, cama_id)
    if resultado:
        print("Visita agregada exitosamente con ID:", resultado)
    else:
        print("No se pudo agregar la visita.")


def ver_visitas():
    print("Listado de Visitas")
    visitas = listar_visitas()
    for visita in visitas:
        print(visita)
    input("Presione Enter para continuar...")

def actualizar_visita():
    print("Actualizar Visita")
    visita_id = input("Ingrese el ID de la visita a actualizar: ")
    nuevo_medico_id = input("Ingrese el nuevo ID del médico tratante: ")
    actualizar_visita(visita_id, nuevo_medico_id)
    print("Visita actualizada exitosamente.")

def eliminar_visita():
    print("Eliminar Visita")
    visita_id = input("Ingrese el ID de la visita a eliminar: ")
    eliminar_visita(visita_id)
    print("Visita eliminada exitosamente.")
