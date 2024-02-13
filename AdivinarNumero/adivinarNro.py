import random

def jugar_adivinanza():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    print("¡Bienvenido a Adivina el número!")
    print("Estoy pensando en un número entre 1 y 100.")

    while True:
        intento = int(input("¿Cuál es tu suposición? "))

        intentos += 1

        if intento < numero_secreto:
            print("Demasiado bajo. Intenta nuevamente.")
        elif intento > numero_secreto:
            print("Demasiado alto. Intenta nuevamente.")
        else:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break

    jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ")
    if jugar_de_nuevo.lower() == "s":
        jugar_adivinanza()
    else:
        print("Gracias por jugar. ¡Hasta luego!")

if __name__ == "__main__":
    jugar_adivinanza()
