"""
Programa: Cálculo recursivo del factorial
Autor: Brayan Ramirez Alvarado
Materia: Programación Lógica y Funcional
Profesor: Neri Perez Giovany Humberto
Grado y grupo: 7SA
Fecha: 02/09/2026

Descripción:
    Este programa calcula el factorial de un número utilizando
    una función recursiva.

    La función se llama a sí misma hasta llegar al caso base,
    que es 0 o 1.

    Ejemplo:
        5! = 5 * 4 * 3 * 2 * 1 = 120
"""


def factorial(numero):
    """
    Calcula el factorial de un número mediante recursividad.

    Parámetro:
        numero (int): Número al que se le calculará el factorial.

    Retorna:
        int: Resultado del factorial.
    """

    # Caso base
    if numero == 0 or numero == 1:
        return 1

    # Llamada recursiva
    return numero * factorial(numero - 1)


# Definir el número
numero = 5

# Calcular el factorial
resultado = factorial(numero)

# Mostrar el resultado
print(f"El factorial de {numero} es {resultado}")