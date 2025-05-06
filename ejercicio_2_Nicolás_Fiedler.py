import random

print("¡Bienvenid@! Este es un juego donde deberás escoger dos límites. Entre los límites que escogiste, habrá un número aleatorio que deberás intentar adivinar")
print("El límite inferior debe ser menor al límite superior.")

lim1 = int(input("Ingrese el límite inferior: "))
lim2 = int(input("Ingrese el límite superior: "))
num_secreto = random.randint(lim1, lim2)

print(f"El número secreto está entre los límites {lim1} y {lim2}.")
print(num_secreto)

intento1 = int(input("Intente adivinar: "))
if intento1 == num_secreto:
    print("¡Adivinaste el número secreto en el primer intento!")
else:
    if intento1 < num_secreto:
        print("El numero es mayor")
    else:
        print("El número es menor")
    intento2 = int(input("Intente de nuevo: "))
    if intento2 == num_secreto:
        print("¡Felicidades! Adivinaste en el segundo intento.")
    else:
        if intento2 < num_secreto:
            print("El número es mayor.")
        else:
            print("El número es menor.")
    print("Te daré una pista:")
    if abs (num_secreto - intento1) > 3 and (num_secreto - intento2) < 3:
        print(f"El número secreto está más cerca de {intento2} que de {intento1}")
    else:
        print(f"El número secreto está más cerca de {intento1} que de {intento2}")

    intento3 = int(input("Intenta una vez más: "))
    if intento3 == num_secreto:
        print("¡Ganaste en el último intento!")
    else:
        print(f"Perdiste. El número secreto era {num_secreto}")