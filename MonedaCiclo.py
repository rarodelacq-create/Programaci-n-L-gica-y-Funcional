"""
Programa: Validación de dato moneda
Autor: Brayan Ramirez Alvarado
Materia: Programación Lógica y Funcional
Profesor: Neri Perez Giovany Humberto
Grado y grupo: 7SA
Fecha: 02/09/2026

Descripción:
    Valida un dato monetario utilizando una expresión regular.
    Se permiten cinco dígitos y opcionalmente entre uno y dos
    números decimales.
"""

import re

# Cinco dígitos y opcionalmente uno o dos decimales
patron = r"^\d{5}(\.\d{1,2})?$"


def validar_moneda():
    """Solicita y valida un dato monetario mediante un ciclo."""

    while True:
        moneda = input("Ingresa el dato moneda (#####.##): ")

        if re.fullmatch(patron, moneda):
            print("Dato moneda válido.")
            break
        else:
            print("Dato moneda inválido. Intenta nuevamente.")


# Programa principal
validar_moneda()