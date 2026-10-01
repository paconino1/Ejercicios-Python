""" ==============================================================================
 Autor: Francisco Niño Caballero

 Enunciado: Ejercicio 8: Generador de Handles de Correo
 Crea un script que solicite el nombre y el primer apellido de un usuario y genere un correo
 corporativo del tipo nombre.apellido@iescastillodeluna.es en minúsculas y sin espacios.
 ============================================================================== """

nombre = input("Introduzca su nombre: ")
apellido = input("Introduzca su primer apellido: ")

correo = f"{nombre.lower().strip()}.{apellido.lower().strip()}@iescastillodeluna.es"

print(f"Su correo corporativo es {correo}")