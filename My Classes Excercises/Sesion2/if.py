# programa para determinar si una persona es mayor de edad

edad = int(input('Digite su edad: '))

if edad >= 18:
    print('Es mayor de edad')
    if edad>=50:
        print('y es de la tercera edad')
else:
    print('Es menor de edad')