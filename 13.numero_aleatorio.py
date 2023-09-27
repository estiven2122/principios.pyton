#Adivina el número
import random

print("!Bienvenido al Juego de adivina el numero!")
print("Trata de adivinar un número entre 1 y el 40")

numero_secreto = random.randint(1,40)

adivinado = False

while not adivinado:
    numero_usuario = int(input("Ingrsa un numero: "))

    if(numero_usuario == numero_secreto):
        print("Felicidades numero Correcto")
        adivinado = True
    elif numero_usuario < numero_secreto:
        print("El numero secreo es alto")
    else:
        print("El numero secreto es mas bajo")

