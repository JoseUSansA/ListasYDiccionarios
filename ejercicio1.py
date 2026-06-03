contador_comandantes = 0
contador_cadete = 0
cantidad_pilotos = int(input("Ingrese cantidad de pilotos: "))

for i in range(cantidad_pilotos):
    nombre = input("Ingrese nombre del piloto: ")
    nivel = int(input("Ingrese nivel del piloto: "))

    if nivel > 40:
        contador_comandantes += 1
    else:
        contador_cadete += 1
print(f"¡La flota estelar cuenta con {contador_comandantes} Comandantes Galácticos y {contador_cadete} Cadetes Estelares!")