# ==============================================================================
# Autor: Francisco Niño Caballero
#
# Enunciado: Ejercicio 2: Conversor de Temperatura
# Crea un programa que pida una temperatura en grados Celsius (permitiendo valores
# decimales) y la transforme a grados Fahrenheit.

# ==============================================================================

temperatura_celsius = float(input("Introduzca una temperatura en grados Celsius: "))
temperatura_fahrenheit = temperatura_celsius * 9/5 + 32
print(f"La temperatura en grados Fahrenheit es: {temperatura_fahrenheit:.2f} ºF")