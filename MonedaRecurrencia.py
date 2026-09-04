"""
Programa: Validación recursiva de dato moneda
Autor: Brayan Ramirez Alvarado
Materia: Programación Lógica y Funcional
Profesor: Neri Perez Giovany Humberto
Grado y grupo: 7SA
Fecha: 02/09/2026

Descripción:
    Valida un dato monetario mediante una expresión regular.
    Si el valor es incorrecto, la función se vuelve a llamar.
"""

import re

patron = r"^\d{5}(\.\d{1,2})?$"


def validar_moneda():
    """Valida un dato monetario utilizando recursividad."""

    moneda = input("Ingresa el dato moneda (#####.##): ")

    if re.fullmatch(patron, moneda):
        print("Dato moneda válido.")
    else:
        print("Dato moneda inválido. Intenta nuevamente.")
        validar_moneda()


# Programa principal
validar_moneda()