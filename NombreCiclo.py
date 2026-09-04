"""
Programa: Validación de nombre
Autor: Brayan Ramirez Alvarado
Materia: Programación Lógica y Funcional
Profesor: Neri Perez Giovany Humberto
Grado y grupo: 7SA
Fecha: 02/09/2026

Descripción:
    Valida un nombre utilizando una expresión regular.
    Solamente se permiten letras y espacios.
"""

import re

patron = r"^[A-Za-zÁÉÍÓÚáéíóúÑñÜü\s]+$"


def validar_nombre():
    """Solicita y valida un nombre mediante un ciclo."""

    while True:
        nombre = input("Ingresa tu nombre: ")

        if re.fullmatch(patron, nombre):
            print("Nombre válido.")
            break
        else:
            print("Nombre inválido.")
            print("Solo se permiten letras y espacios.")


# Programa principal
validar_nombre()