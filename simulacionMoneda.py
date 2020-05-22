import random

print ("Para salir del juego presiona Enter")

cara = 1
escudo = 2

lanzar = True
while lanzar:
    print(random.randint(cara, escudo))

    lanzar_moneda = input('Quieres lanzar la moneda nuevamente? Escribe si o s \n')
    if lanzar_moneda == 'si' or lanzar_moneda == 's':
        lanzar = True
    else:
        lanzar = False

print ("Gracias por jugar con la moneda !!!")
