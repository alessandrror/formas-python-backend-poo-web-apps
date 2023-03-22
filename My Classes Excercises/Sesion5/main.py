from calculos.planilla import isss, afp, desc_isr, sueldo_gravable, total_descuentos, sueldo_pagar 
from utilerias import menu, mensaje
print(mensaje)

print(menu.MENU)
op = int(input('Digite una opción: '))

while op >=1 and op <= 6 :
    sueldo = float(input('Ingrese su sueldo: $'))

    if op == 1 :
        print(f'El ISSS es $ {isss(sueldo):.2f}')
    if op == 2 :
        print(f'El AFP es $ {afp(sueldo):.2f}')
    if op == 3 :
        print(f'El ISR es $ {desc_isr(sueldo):.2f}')
    if op == 4 :
        print(f'El Sueldo Gravable es $ {sueldo_gravable(sueldo):.2f}')
    if op == 5 :
        print(f'El Total de Descuento es $ {total_descuentos(sueldo):.2f}')
    if op == 6 :
        print(f'El Sueldo a Pagar es $ {sueldo_pagar(sueldo):.2f}')

    input()
    menu.limpiar()
    print(menu.MENU)
    op = int(input('Digite una opción: '))