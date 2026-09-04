"""
Programa: Validación recursiva de número telefónico
Autor: Brayan Ramirez Alvarado
Materia: Programación Lógica y Funcional
Profesor: Neri Perez Giovany Humberto
Grado y grupo: 7SA
Fecha: 02/09/2026

Descripción:
    Valida un número telefónico de México mediante recursividad.
    El número debe comenzar con +52 y tener 10 dígitos.
"""

import re

patron = r"^\+52\d{10}$"


def validar_telefono():
    """Valida un número telefónico utilizando recursividad."""

    telefono = input("Ingresa tu teléfono (+52 y 10 dígitos): ")

    if re.fullmatch(patron, telefono):
        print("Número telefónico válido.")
    else:
        print("Número telefónico inválido. Intenta nuevamente.")
        validar_telefono()


# Programa principal
validar_telefono()