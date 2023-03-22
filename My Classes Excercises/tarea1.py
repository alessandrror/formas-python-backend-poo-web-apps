# Crea un programa que capture los datos de N empleados:
# 1. Nombre
# 2. Cargo 
# 3. Sueldo

# Crear el siguiente menu: 
# 1. agregar empleado
# 2. imprimir lista
# 3. salir

# Para cada empleado construir un diccionario
# que se ira agregando a una lista y que
# se imprimira con la opcion 2 del menu.

import os

empleados = []
menu = None
x = None

print('Bienvenido al programa para agregar empleados.')
while menu != 3 :
    print('Las opciones a ingresar son:')
    print('1 - Agregar un empleado')
    print('2 - Imprimir la lista de empleados')
    print('3 - Salir del programa')
    x = int(input('Ingrese la opción deseada: '))
    os.system('cls||clear')
    add = True

    if x == 1 :
        while add == True :
            print('Ingrese los valores del empleado en el siguiente orden: ')
            nextEmployee = True
            empleado = {}
            empleado['Empleado'] = str(input('Nombre: '))
            empleado['Cargo'] = str(input('Cargo: '))
            empleado['Salario'] = int(input('Sueldo: '))
            empleados.append(empleado)
            while nextEmployee == True :
                status = input('¿Desea ingresar otro empleado? Responda S/N: ')
                if status == 'N' : 
                    add = False
                    nextEmployee = False
                    os.system('cls||clear')
                elif status == 'S' :
                    input('Presione enter para continuar ')
                    nextEmployee = False
                    os.system('cls||clear')
                else : 
                    print('Ingreso una opcion no valida')
                    os.system('cls||clear')
    elif x == 2 :
        print('El listado de empleados es el siguiente: ')
        i = 1
        for employee in empleados :
            print(f'Empleado {i}:')
            i+=1
            j = 0
            for k,v in employee.items() :
                print(f' --> {k}: {v}')
            if j < len(employee) - 1 :
                input('Presione enter el siguiente empleado ')
            j+=1
        input('No hay más empleados por ver ')
        input('Presione enter para continuar ')
        os.system('cls||clear')
    elif x == 3 :
        input('Programa finalizado ')
        os.system('cls||clear')
        menu = 3
    else :
        print('Usted seleccionó una opción no válida')
        print('Vuelva a ingresar una opción')
        os.system('cls||clear')
