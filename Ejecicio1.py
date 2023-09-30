#Tablas de multiplcar ingresando el numero de la tabla

def tabla_multiplicar(tabla, limite):
    for i in range(1,limite):
        resultado = tabla * i
        print(f"{tabla} x {i} = {resultado}")

tabla = int(input("Qué tabla de multiplicar quieres saber?"))

tabla_multiplicar(tabla,21)
