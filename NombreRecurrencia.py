"""
Programa: Validación recursiva de nombre
Autor: Brayan Ramirez Alvarado
Materia: Programación Lógica y Funcional
Profesor: Neri Perez Giovany Humberto
Grado y grupo: 7SA
Fecha: 02/09/2026

Descripción:
    Valida un nombre mediante una expresión regular y
    recursividad. Solamente se permiten letras y espacios.
"""

import re

patron = r"^[A-Za-zÁÉÍÓÚáéíóúÑñÜü\s]+$"


def validar_nombre():
    """Valida un nombre utilizando recursividad."""

    nombre = input("Ingresa tu nombre: ")

    if re.fullmatch(patron, nombre):
        print("Nombre válido.")
    else:
        print("Nombre inválido.")
        print("Solo se permiten letras y espacios.")
        validar_nombre()


# Programa principal
validar_nombre()