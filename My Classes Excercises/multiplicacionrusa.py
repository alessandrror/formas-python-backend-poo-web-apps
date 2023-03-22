# La multiplicacion rusa
# El multiplicador se divide entre dos, si es impar, suma
# El multiplicando se multiplicad por dos
# Asi sucesivamente hasta que el multiplicador sea uno y sume

multiplicador = int(input('Ingrese el valor del multiplicador: '))
multiplicando = int(input('Ingrese el valor del multiplicando: '))
n1 = multiplicador
n2 = multiplicando
total = 0

while multiplicador >= 1 :
    if int(multiplicador%2) != 0 :
        total+= multiplicando
        print(f' --> Suma {multiplicando}')
    else:
        print(' --> Suma 0')
    multiplicador/=2
    multiplicando*=2

print(f' --> El resultado de la suma rusa de {n1} y {n2} es: {total}')