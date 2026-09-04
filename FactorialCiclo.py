"""
Programa: Cálculo del factorial de un número
Autor: Brayan Ramirez Alvarado
Materia: Programación Lógica y Funcional
Profesor: Neri Perez Giovany Humberto
Grado y grupo: 7SA
Fecha: 02/09/2026

Descripción:
    Este programa calcula el factorial de un número utilizando
    un ciclo for.

    El factorial de un número n se obtiene multiplicando todos
    los números enteros positivos desde 1 hasta n.

    Ejemplo:
        5! = 1 * 2 * 3 * 4 * 5 = 120
"""

# Definir el número
numero = 5

# Inicializar el resultado del factorial en 1
factorial = 1

# Calcular el factorial mediante un ciclo for
for i in range(1, numero + 1):
    factorial *= i

# Mostrar el resultado
print(f"El factorial de {numero} es {factorial}")