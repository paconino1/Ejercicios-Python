""" ==============================================================================
 Autor: Francisco Niño Caballero

 Enunciado: Ejercicio 16: Validación de Contraseña
 Crea un programa que solicite una clave de acceso. El programa debe repetir la petición
 mientras la clave introducida sea incorrecta. Permite un máximo de 3 intentos antes de
 bloquear el acceso.
 ============================================================================== """

CONTRASEÑA = "contraseña123"
intento = ""
num_intentos = 0

while intento != CONTRASEÑA and num_intentos < 3:
    intento = input("Introduce la contraseña: ")
    if intento == CONTRASEÑA:
        print("Acceso concedido.")
        break
    else:
        num_intentos += 1
        if num_intentos == 3:
            print("Acceso bloqueado. Has agotado los intentos.")
        else:
            print("Contraseña incorrecta. Inténtalo de nuevo.")