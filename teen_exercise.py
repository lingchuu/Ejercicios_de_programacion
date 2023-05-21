"""Ejercicio numero diez (10)
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
Los ingredientes para cada tipo de pizza aparecen a continuación.
Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Problema:
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no,
Y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija.
Solo se puede eligir un ingrediente
además de la mozzarella y el tomate que están en todas la pizzas.

Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no
y todos los ingredientes que lleva."""

#-----------------------------------------
#  Codigo realizado por Ale Seminario, Ing. de Sistemas e Informatica.
#-----------------------------------------
PRIMER_INGREDIENTE_GENERAL="Tomate"
SEGUNDO_INGREDIENTE_GENERAL="Mozzarella"
LINEAS_DIVISORAS="-----------------------------------------"
#  Definimos variables globales

print("¿Desea una pizza vegetariana o no?")
print("Escriba 'si' si desea un pizza vegetariana")
print("Escriba 'no' si no desea un pizza vegetariana, sino otra")
decision=input()
#  Almacenamos la informacion del input() en la variable decision.

decision=decision.lower()
# Convertimos la cadena de caracteres a minusulas para que no existan problemas.

print(LINEAS_DIVISORAS)
#-----------------------------------------

if decision=="si":
    TYPE_OF_PIZZA="Vegetariana"
    print("Entonces a escojido el tipo de pizza", TYPE_OF_PIZZA,".")
    print("¡Solo se puede eligir un ingrediente!")
    print("Escoja:\nIntroduzca el numero uno (1) para escojer: 'Pimiento'")
    print("Introduzca el numero dos (2) para escojer: 'Tofu'")
    ingredientevegano=int(input())
    print(LINEAS_DIVISORAS)
    print("Usted a escojido la opcion de ingrediente numero:",ingredientevegano)
    if ingredientevegano==1:
        INGREDIENTE_SELECCIONADO="Pimiento"
        print("La pizza escojida ha sido:",TYPE_OF_PIZZA)
        print(LINEAS_DIVISORAS)
        print("La lista de ingredientes sera:")
        print("1.",PRIMER_INGREDIENTE_GENERAL)
        print("2.",SEGUNDO_INGREDIENTE_GENERAL)
        print("3.",INGREDIENTE_SELECCIONADO)

    elif ingredientevegano==2:
        INGREDIENTE_SELECCIONADO="Tofu"
        print("La pizza escojida ha sido",TYPE_OF_PIZZA)
        print(LINEAS_DIVISORAS)
        print("La lista de ingredientes sera:")
        print("1.",PRIMER_INGREDIENTE_GENERAL)
        print("2.",SEGUNDO_INGREDIENTE_GENERAL)
        print("3.",INGREDIENTE_SELECCIONADO)
    print(LINEAS_DIVISORAS)

#-----------------------------------------
elif decision=="no":
    TYPE_OF_PIZZA="de carne"
    print("Entonces a escojido el tipo de pizza", TYPE_OF_PIZZA,".")
    print("¡Solo se puede eligir un ingrediente!")
    print("Escoja:\nIntroduzca el numero uno (1) para escojer: 'Peperoni'")
    print("Introduzca el numero dos (2) para escojer: 'Jamón'")
    print("Introduzca el numero tres (3) para escojer: 'Salmón'")
    ingrediente_de_carne=int(input())
    print(LINEAS_DIVISORAS)
    print("Usted a escojido la opcion de ingrediente numero:",ingrediente_de_carne)
    if ingrediente_de_carne==int(1):
        INGREDIENTE_SELECCIONADO="Peperoni"
        print("La pizza escojida ha sido:",TYPE_OF_PIZZA)
        print(LINEAS_DIVISORAS)
        print("La lista de ingredientes sera:")
        print("1.",PRIMER_INGREDIENTE_GENERAL)
        print("2.",SEGUNDO_INGREDIENTE_GENERAL)
        print("3.",INGREDIENTE_SELECCIONADO)

    elif ingrediente_de_carne==int(2):
        INGREDIENTE_SELECCIONADO="Jamón"
        print("La pizza escojida ha sido:",TYPE_OF_PIZZA)
        print(LINEAS_DIVISORAS)
        print("La lista de ingredientes sera:")
        print("1.",PRIMER_INGREDIENTE_GENERAL)
        print("2.",SEGUNDO_INGREDIENTE_GENERAL)
        print("3.",INGREDIENTE_SELECCIONADO)
    elif ingrediente_de_carne==int(3):
        INGREDIENTE_SELECCIONADO="Salmón"
        print("La pizza escojida ha sido:",TYPE_OF_PIZZA)
        print(LINEAS_DIVISORAS)
        print("La lista de ingredientes sera:")
        print("1.",PRIMER_INGREDIENTE_GENERAL)
        print("2.",SEGUNDO_INGREDIENTE_GENERAL)
        print("3.",INGREDIENTE_SELECCIONADO)
    print(LINEAS_DIVISORAS)

#-----------------------------------------
else:
    print("Intentelo nuevamente.")
