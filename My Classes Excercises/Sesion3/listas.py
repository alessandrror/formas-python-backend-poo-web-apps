# programa para uso de listas
nombres = ['alicia', 'beto', 'camila', 'diana']
# calcular su  longitud 
print(f'La longitud de nombres es: {len(nombres)}')
# son ordenadas
print(nombres)
# acceder a sus elementos por su posicion (indice index)
print(nombres[2])
# son mutables, los elementos pueden ser modificados
nombres[3] = 'eva'
print(nombres[3])
# dinamicas, podemos añadir y quitar elementos 
nombres.append('fran')
print(nombres)
nombres.remove('beto')
print(nombres)
nombres.insert(1, 'gabriela')
print(nombres)
nombres.pop(2)
print(nombres)
nombres.pop(-2)
print(nombres)
# se pueden anidar
nombres.append([10,20,30])
print(nombres)
# recorrer una lista
for nombre in nombres :
    print(f' --> nombre: {nombre}')
# vaciar todos los elementos de la lista
nombres.clear()
print(f'Numero de elementos en nombres: {len(nombres)} --> {nombres}')