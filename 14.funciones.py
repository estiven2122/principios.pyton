def saludo():
    print("Hola amigo")

saludo()

def saludo(nombre, apellido):
    print(f"Hola {nombre} {apellido}")

saludo("Estiven", "Hurtado")

def suma(num1, num2):
    total = num1 + num2
    print(f"La suma de {num1} + {num2} = {total}")

suma(2,4)

def saludo2(nombre, apellido="dominguez"):
    print(f"Hola {nombre} {apellido}")

saludo2("Estiven", "Hurtado")