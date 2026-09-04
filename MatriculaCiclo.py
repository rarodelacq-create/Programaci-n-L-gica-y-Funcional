"""
Programa: Validación de matrícula escolar
Autor: Brayan Ramirez Alvarado
Materia: Programación Lógica y Funcional
Profesor: Neri Perez Giovany Humberto
Grado y grupo: 7SA
Fecha: 02/09/2026

Descripción:
    Valida una matrícula escolar utilizando una expresión regular.
    Para el año 2026, la matrícula debe comenzar con 26,
    continuar con 115 y terminar con tres dígitos.
"""

import re

# Estructura: 26 + 115 + tres dígitos
patron = r"^26115\d{3}$"


def validar_matricula():
    """Solicita y valida una matrícula mediante un ciclo."""

    while True:
        matricula = input("Ingresa tu matrícula escolar: ")

        if re.fullmatch(patron, matricula):
            print("Matrícula válida.")
            break
        else:
            print("Matrícula inválida.")
            print("El formato debe ser: 26115XXX.")


# Programa principal
validar_matricula()