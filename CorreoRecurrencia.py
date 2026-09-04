"""
Programa: Validación recursiva de correo electrónico
Autor: Brayan Ramirez Alvarado
Materia: Programación Lógica y Funcional
Profesor: Neri Perez Giovany Humberto
Grado y grupo: 7SA
Fecha: 02/09/2026

Descripción:
    Este programa valida un correo electrónico mediante una
    expresión regular. Cuando el dato es incorrecto, la función
    se vuelve a llamar hasta recibir un dato válido.
"""

import re

# Expresión regular para validar el correo
patron = r"^[\w.-]+@[\w.-]+\.[A-Za-z]{2,}$"


def validar_correo():
    """Valida un correo utilizando recursividad."""

    correo = input("Ingresa tu correo electrónico: ")

    if re.fullmatch(patron, correo):
        print("Correo electrónico válido.")
    else:
        print("Correo electrónico inválido. Intenta nuevamente.")
        validar_correo()


# Programa principal
validar_correo()