""" ==============================================================================
 Autor: Francisco Niño Caballero

 Enunciado: Ejercicio 14: Tarifario con Descuento
 Un parque temático cobra 12€ por entrada. Sin embargo:
 ● Los menores de 4 años entran gratis.
 ● Los estudiantes o mayores de 65 años tienen un 40% de descuento.
 ● El resto paga la tarifa completa.
 Solicita edad y si es estudiante (s/n) para calcular el precio final a pagar
 ============================================================================== """

edad = int(input("Introduzca su edad: "))
es_estudiante = input("¿Es estudiante? (s/n): ").strip().lower()
ENTRADA = 12

if edad < 4:
  print("Entrada gratuita")
elif es_estudiante == "s" or edad >= 65:
  precio = ENTRADA * 0.6
  print(f"Entrada: {precio:.2f} €")
else:
  print(f"Entrada: {ENTRADA} €")