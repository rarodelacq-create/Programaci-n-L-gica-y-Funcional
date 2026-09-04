"""
Programa: Validación recursiva de matrícula escolar
Autor: Brayan Ramirez Alvarado
Materia: Programación Lógica y Funcional
Profesor: Neri Perez Giovany Humberto
Grado y grupo: 7SA
Fecha: 02/09/2026

Descripción:
    Valida una matrícula escolar mediante una expresión regular
    y recursividad. Para 2026, la estructura es 26 + 115 +
    tres dígitos correspondientes al número del alumno.
"""

import re

patron = r"^26115\d{3}$"


def validar_matricula():
    """Valida una matrícula utilizando recursividad."""

    matricula = input("Ingresa tu matrícula escolar: ")

    if re.fullmatch(patron, matricula):
        print("Matrícula válida.")
    else:
        print("Matrícula inválida.")
        print("El formato debe ser: 26115XXX.")
        validar_matricula()


# Programa principal
validar_matricula()