"""
Programa: Validación recursiva de contraseña segura
Autor: Brayan Ramirez Alvarado
Materia: Programación Lógica y Funcional
Profesor: Neri Perez Giovany Humberto
Grado y grupo: 7SA
Fecha: 02/09/2026

Descripción:
    Valida una contraseña mediante una expresión regular.
    Si la contraseña no cumple las condiciones, la función
    se vuelve a llamar hasta recibir una contraseña válida.
"""

import re

patron = r"^(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}$"


def validar_password():
    """Valida una contraseña utilizando recursividad."""

    password = input("Ingresa una contraseña segura: ")

    if re.fullmatch(patron, password):
        print("Contraseña válida.")
    else:
        print("Contraseña inválida.")
        print("Debe tener mínimo 8 caracteres, una mayúscula,")
        print("un número y un carácter especial.")
        validar_password()


# Programa principal
validar_password()