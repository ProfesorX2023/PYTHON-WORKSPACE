from random import randint

intentos = 0
estimado = 0
numero_secreto = randint(1,100)
nombre = input("Dime tu nombre: ")

print(f"Bueno {nombre}, he pensado un número entre 1 y 100 \n Tienes 8 intentos para adivinar")

while intentos < 8:
    estimado = int(input("¿Cúal es el número?: "))
    intentos += 1

    if estimado < numero_secreto:
        print("El número que escribiste parece ser muy pequeño, intenta con uno más grande")
    elif estimado > numero_secreto:
        print("El número que escribiste parece ser muy grande, intenta con uno más pequeño")
    else:
        print(f"Felicidades {nombre}! Has adivinado en {intentos} intentos")
        break

if estimado != numero_secreto:
    print(f"Lo siento, se ha agotado los intentos. El número secreto era: {numero_secreto}")