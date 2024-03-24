#Diccionario de informacion personal
informacion_personal = {
    "nombre": "Santiago",
    "apellido": "Guerra",
    "edad": 32,
    "ciudad": "Galapagos",
    "provincia": "Puerto Baquerizo Moreno"
}
print(informacion_personal)

#Cambio de valor en la clave
informacion_personal["ciudad"] = "Andorra"
print(informacion_personal["ciudad"])

#Agrego clave:valor en diccionario
informacion_personal["profesion"] = "Mecanico"
print(informacion_personal)

#Verifico si existe clave:valor celular y agrego
if "celular" in informacion_personal:
    print(informacion_personal["celular"])
else:
    informacion_personal["celular"] = "0935729751"
    print(informacion_personal)

#Elimino clave
informacion_personal.pop("edad")
print(informacion_personal)