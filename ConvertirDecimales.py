# Escribe un programa que solicite al usuario
# con decimales y almacenalo en una variable.
# A continuacion, el programa debe solicitar al usuario que ingrese
# un numero enetero y guardarlo en otra variable.
# En una tercera variable se debera guardar el resultado de la suma
# de los dos numeros ingresados por el usuario.
# Por ultimo, se debe mostrar en pantalla el texto
# "El resultado de la suma es [suma]", donde "[suma]"
# se reemplazara por el resultado de la opracion

valorDecimal = float(input("Ingrese un decimal: "))

valorEntero = int(input("Ingrese un entero: "))

suma = valorDecimal + valorEntero
print("El resultado de la suma es ", (suma))
# print("El resultado de la suma es " + str(suma))
