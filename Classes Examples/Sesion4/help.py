import os

while (True):
    nombre = input('nombre? ')
    edad = input('edad? ')

    # limpiar la pantalla
    os.system('cls||clear')

    print(f'nombre: {nombre}\nedad: {edad}')

    # simula una pausa
    input()

    # limpiar la pantalla
    os.system('cls||clear')

    estado = input('desea continuar: S/N ? ')

    if estado=='N':
        break

    # limpiar la pantalla
    os.system('cls||clear')

