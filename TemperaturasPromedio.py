# Crear_un_codigo_que_me_de_las_temperaturas_de_dos_ciudades_distintas
def calcular_promedio(temperaturas):
  if not temperaturas or not all(isinstance(dia, dict) and "temp" in dia for dia in temperaturas):
    return None  # Indicate invalid data or no data
  temps = [dia["temp"] for dia in temperaturas if isinstance(dia, dict)]  # Extract temperatures
  suma = sum(temps)
  promedio = round(suma / len(temps), 2)
  return promedio

temperatures = [
  # Ciudad: Puyo
  [
    {"city": "Puyo"},
    [
      {"day": "Monday", "temp": 23},
      {"day": "Tuesday", "temp": 12},
      {"day": "Wednesday", "temp": 32},
      {"day": "Thursday", "temp": 25},
      {"day": "Friday", "temp": 18},
      {"day": "Saturday", "temp": 22},
      {"day": "Sunday", "temp": 28},
    ],
    [
      {"day": "Monday", "temp": 12},
      {"day": "Tuesday", "temp": 22},
      {"day": "Wednesday", "temp": 15},
      {"day": "Thursday", "temp": 27},
      {"day": "Friday", "temp": 17},
      {"day": "Saturday", "temp": 32},
      {"day": "Sunday", "temp": 19},
    ],
    [
      {"day": "Monday", "temp": 28},
      {"day": "Tuesday", "temp": 32},
      {"day": "Wednesday", "temp": 23},
      {"day": "Thursday", "temp": 22},
      {"day": "Friday", "temp": 12},
      {"day": "Saturday", "temp": 25},
      {"day": "Sunday", "temp": 18},
    ],
    [
      {"day": "Monday", "temp": 20},
      {"day": "Tuesday", "temp": 31},
      {"day": "Wednesday", "temp": 18},
      {"day": "Thursday", "temp": 29},
      {"day": "Friday", "temp": 31},
      {"day": "Saturday", "temp": 24},
      {"day": "Sunday", "temp": 21},
    ],
  ],
  # Ciudad: Guayaquil
  [
    {"city": "Guayaquil"},
    [
      {"day": "Monday", "temp": 32},
      {"day": "Tuesday", "temp": 26},
      {"day": "Wednesday", "temp": 31},
      {"day": "Thursday", "temp": 30},
      {"day": "Friday", "temp": 18},
      {"day": "Saturday", "temp": 30},
      {"day": "Sunday", "temp": 28},
    ],
    [
      {"day": "Monday", "temp": 15},
      {"day": "Tuesday", "temp": 24},
      {"day": "Wednesday", "temp": 18},
      {"day": "Thursday", "temp": 16},
      {"day": "Friday", "temp": 24},
      {"day": "Saturday", "temp": 32},
      {"day": "Sunday", "temp": 20},
    ],
    [
      {"day": "Monday", "temp": 16},
      {"day": "Tuesday", "temp": 30},
      {"day": "Wednesday", "temp": 32},
      {"day": "Thursday", "temp": 21},
      {"day": "Friday", "temp": 29},
      {"day": "Saturday", "temp": 15},
      {"day": "Sunday", "temp": 22},
    ],
    [
      {"day": "Monday", "temp": 25},
      {"day": "Tuesday", "temp": 15},
      {"day": "Wednesday", "temp": 24},
      {"day": "Thursday", "temp": 27},
      {"day": "Friday", "temp": 32},
      {"day": "Saturday", "temp": 24},
      {"day": "Sunday", "temp": 29},
    ],
  ],
  # Ciudad : Ambato
  [
    {"city": "Ambato"},
    [
      {"day": "Monday", "temp": 17},
      {"day": "Tuesday", "temp": 15},
      {"day": "Wednesday", "temp": 18},
      {"day": "Thursday", "temp": 27},
      {"day": "Friday", "temp": 14},
      {"day": "Saturday", "temp": 20},
      {"day": "Sunday", "temp": 15},
    ],
    [
      {"day": "Monday", "temp": 16},
      {"day": "Tuesday", "temp": 14},
      {"day": "Wednesday", "temp": 20},
      {"day": "Thursday", "temp": 14},
      {"day": "Friday", "temp": 18},
      {"day": "Saturday", "temp": 15},
      {"day": "Sunday", "temp": 15},
    ],
    [
      {"day": "Monday", "temp": 20},
      {"day": "Tuesday", "temp": 17},
      {"day": "Wednesday", "temp": 15},
      {"day": "Thursday", "temp": 14},
      {"day": "Friday", "temp": 15},
      {"day": "Saturday", "temp": 18},
      {"day": "Sunday", "temp": 18},
    ],
    [
      {"day": "Monday", "temp": 19},
      {"day": "Tuesday", "temp": 14},
      {"day": "Wednesday", "temp": 20},
      {"day": "Thursday", "temp": 18},
      {"day": "Friday", "temp": 16},
      {"day": "Saturday", "temp": 15},
      {"day": "Sunday", "temp": 14},
    ],
    ]
]
print("Hola!")
print("Soy Stefania")
print("Calcularemos las temperaturas de diferentes ciudades")
for ciudad_temps in temperatures:
  ciudad_nombre = ciudad_temps[0]["city"]
  print(f"Ciudad: {ciudad_nombre}")
  for semana in ciudad_temps[1:]:
    promedio_semana = calcular_promedio(semana)
    if promedio_semana is None:
      print(f"Error: Datos de temperatura inválidos para la semana.")
      continue
    print(f"El promedio de la semana es: {promedio_semana} grados Celsius")