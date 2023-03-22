# programa para determinar si una persona es mayor de edad
# condiciones multiples
edad = int(input('Digite su edad: '))

if edad > 0 and edad<18:
    print('es menor de edad')
elif edad>=18 and edad<60:
    print('es mayor de edad')
elif edad>=60 and edad<=105:
    print('es de la tercera edad')
else:
    print('la edad no es valida')