contador_comandantes = 0
contador_cadete = 0
pilotos = []

while True:
    try:
        cantidad_pilotos = int(input("Ingrese cantidad de pilotos: "))
        if cantidad_pilotos>0:
            break
        print("Error: debe ser un número positivo.")
    except ValueError:
        print("Error: debe ingresar un número entero.")

for i in range(cantidad_pilotos):
    while True:
        nombre = input("Ingrese nombre del piloto: ").strip()
        if len(nombre)>=6 and " " not in nombre:
            break
        print("Error: el nombre debe tener al menos 6 caracteres y sin espacios")

    while True:
        try:
            nivel = int(input("Ingrese nivel del piloto: "))
            if nivel>0:
                break
            print("Error: debe ser un número positivo.")
        except ValueError:
            print("Error: debe ser un número entero.")
    piloto = {"nombre_piloto":nombre, "nivel_piloto":nivel}
    pilotos.append(piloto)
    if nivel > 40:
        contador_comandantes += 1
    else:
        contador_cadete += 1

print(f"¡La flota estelar cuenta con {contador_comandantes} Comandantes Galácticos y {contador_cadete} Cadetes Estelares!")

for p in pilotos:
    print(f"Piloto: {p["nombre_piloto"]} | Nivel: {p["nivel_piloto"]}")