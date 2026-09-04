"""
Programa: Validación de correo electrónico
Autor: Brayan Ramirez Alvarado
Materia: Programación Lógica y Funcional
Profesor: Neri Perez Giovany Humberto
Grado y grupo: 7SA
Fecha: 02/09/2026

Descripción:
    Este programa valida una dirección de correo electrónico
    utilizando una expresión regular. El programa continúa
    solicitando datos hasta que el usuario introduzca un
    correo válido.
"""

import re

# Expresión regular para validar el correo electrónico
patron = r"^[\w.-]+@[\w.-]+\.[A-Za-z]{2,}$"


def validar_correo():
    """Solicita y valida un correo electrónico mediante un ciclo."""
    
    while True:
        correo = input("Ingresa tu correo electrónico: ")

        if re.fullmatch(patron, correo):
            print("Correo electrónico válido.")
            break
        else:
            print("Correo electrónico inválido. Intenta nuevamente.")


# Programa principal
validar_correo()