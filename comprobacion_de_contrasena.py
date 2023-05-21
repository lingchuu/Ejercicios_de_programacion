# Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
# pregunte al usuario por la contraseña e imprima por pantalla
# si la contraseña introducida por el usuario coincide
# con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

CONTR = "seguridad"
CONTR = input("¿Cual es tu contraseña?\n")
CONTR = CONTR.lower()
if CONTR == "seguridad":
    print("La contraseña es correcta")
else:
    print("La contraseña es incorrecta")

print("-----------------------------\n"+"Programa finalizado.\n"+"Adios")
