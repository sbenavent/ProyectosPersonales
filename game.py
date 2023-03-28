import random
from playsound import playsound
import threading
import time

def musica():
    while True:
        playsound(r'C:\Users\sbena\OneDrive\Documentos\Cloud computing\VIDEOJUEGO\bin\music\musica.wav')
        time.sleep(1)

T=threading.Thread(target=musica, daemon=True)


T.start()   


salir = "false"
while salir != "SALIR":
   
    print("¡Bienvenido al juego! Tienes 10 intentos para adivinar un número del 1 al 100. ¿Podrás conseguirlo?")
    numeroAleatorio = random.randint(1,100)

    validation = "false" 
    contador = (int(0))

    print("Mira a ver si aciertas el número")
    while validation != "true":
        guess = int(input())
        if guess == numeroAleatorio:
            print("¡¡¡PREMIO!!!")
            validation = "true"
        if guess > numeroAleatorio:
            print("Un poquito más suave premo")
            contador = contador+1
        if guess < numeroAleatorio:
            print("Dale más caña bro")
            contador = contador+1
        if contador == 10:
            print("SE TE ACABARON LOS INTENTOS")
            print("El número correcto era", numeroAleatorio)
            validation = "true"


    print("Escribe SALIR para cerrar el juego o pulsa ENTER para intentarlo de nuevo")
    salir = input()