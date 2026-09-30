# ==============================================================================
# Autor: Francisco Niño Caballero
#
# Enunciado: Ejercicio 3: Cálculo del Salario Bruto
# Diseña un script que pida las horas trabajadas en la semana por un desarrollador y su tarifa por
# hora en euros (decimal). El programa debe calcular y mostrar el salario bruto semanal.
# ==============================================================================

horas_semanales = float(input("Introduzca las horas que ha trabajado esta semana: "))
tarifa_hora = int(input("Introduzca su tarifa por hora en euros: "))

salario_bruto_semanal = horas_semanales * tarifa_hora

print(f"Su salario es de {salario_bruto_semanal:.2f} €")