"""
Programa: Validación de contraseña segura
Autor: Brayan Ramirez Alvarado
Materia: Programación Lógica y Funcional
Profesor: Neri Perez Giovany Humberto
Grado y grupo: 7SA
Fecha: 02/09/2026

Descripción:
    Valida una contraseña mediante una expresión regular.
    La contraseña debe tener mínimo 8 caracteres, una mayúscula,
    un número y un carácter especial.
"""

import re

# Expresión regular para validar la contraseña
patron = r"^(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}$"


def validar_password():
    """Solicita y valida una contraseña utilizando un ciclo."""

    while True:
        password = input("Ingresa una contraseña segura: ")

        if re.fullmatch(patron, password):
            print("Contraseña válida.")
            break
        else:
            print("Contraseña inválida.")
            print("Debe tener mínimo 8 caracteres, una mayúscula,")
            print("un número y un carácter especial.")


# Programa principal
validar_password()