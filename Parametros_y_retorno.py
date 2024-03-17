#Calcular raiz cuadrada de un número
import math
def calcular_raiz_cuadrada(numero):
    raiz_cuadrada = math.sqrt(numero)
    return raiz_cuadrada
def saludar():
    nombre = input("ingrese su nombre: ")
    print(f"hola {nombre}, ¿deseas calcular la raiz cuadrada de un numero?")
    respuesta = input("si o no: ")
    if respuesta.lower() == "si" or respuesta.lower() == "si":
        variable = float(input("ingresar numero a calcular: "))
        raiz = calcular_raiz_cuadrada(variable)
        print(f"La raiz cuadrada de {variable} es: {raiz}")

saludar()
input("Adios")