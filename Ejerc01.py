# ==============================================================================
# Autor: Francisco Niño Caballero
#
# Enunciado: Ejercicio 1: Registro de Alumno
# Escribe un programa que solicite por consola el nombre del alumno, sus apellidos y su ciclo
# formativo. Posteriormente, debe mostrar un mensaje de bienvenida unificado utilizando
# cadenas formateadas (f-strings).
# ==============================================================================

nombre = input("Introduzca su nombre: ")
apellidos = input("Introduzca sus apellidos: ")
ciclo = input("Introduzca su ciclo formativo: ")

print(f"Hola {nombre} {apellidos}, bienvenido al ciclo formativo de {ciclo}.")