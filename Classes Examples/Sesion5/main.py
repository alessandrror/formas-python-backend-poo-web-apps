from calculos.planilla import isss, afp, desc_isr
from utilerias import menu, mensaje
print(mensaje)
print(menu.MENU)
op = int(input('digite un opcion: '))

while op>=1 and op<=6:
    sueldo = float(input('digite sueldo: $'))

    if op==1:
        print(f'El ISSS es $ {isss(sueldo):.2f}')
    elif op==2:
        print(f'El AFP es $ {afp(sueldo):.2f}')
    elif op==3:
        print(f'El ISR es $ {desc_isr(sueldo):.2f}')
    # TODO: programar las opciones faltantes

    input()
    menu.limpiar()
    print(menu.MENU)
    op = int(input('digite un opcion: '))