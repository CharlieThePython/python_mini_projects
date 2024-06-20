#Adivina el Número:

# Descripción: Desarrolla un juego donde la computadora genere un número aleatorio y el usuario tenga que adivinarlo en el menor número de intentos posibles.
# Conceptos: Bucles, condicionales, generación de números aleatorios.

# División de partes:
#1. Función para generar el número
#2. Función main desde la que se llaman el resto de funciones

#Flujo de Ejecución:

#1. Llamada a la función Main
#2. Se llama a la función que genera el número aleatorio (entre 0 y 100)
#3. Se pregunta al usuario el número en cuestión
#4.1. Si lo acierta, el juego termina
#4.2 Si no acierta, el bucle continúa y se le indica si el número es mayor o menor que el número dado
#5. En el caso de que se acaben los intentos, el juego termina
import random

def randomNumberGenerator():
    return random.randint(1,100)

def inputNumber(randomNumber):
    number = int(input("Introduce a number between 1 and 100"))
    if number != randomNumber:
        return number
    else:
        return True

def triesCounter(tries):
    return tries-1

def main():
    randomNumber = randomNumberGenerator()
    tries = 5
    print(randomNumber)
    number = inputNumber(randomNumber)
    while number != True and tries > 1:
        if number > randomNumber:
            print("The magic number is LOWER")
        else:
            print("The magic number is HIGHER")
        tries = triesCounter(tries)
        print("You have ",tries," left")
        number =inputNumber(randomNumber)
    return number

# Start
if main() == True:
    print("YOU WIN! CONGRATULATIONS")
else:
    print("YOU LOSE. I'm sorry")