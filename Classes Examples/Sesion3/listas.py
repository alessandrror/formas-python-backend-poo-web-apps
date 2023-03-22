# programa para uso de listas
nombres = ['alicia','beto','camila','diana', 1]
# calcular su longitud (tamaño)
print(f'la longitud de nombres es: {len(nombres)}')
# son ordenadas
print(nombres)
# acceder a sus elementos por su posicion (indice index)
print(nombres[2])
# son mutables, los elementos pueden ser modificados
nombres[3] = 'eva'
print(nombres)
# podemos anadir y quitar elementos (dinamicas)
nombres.append('fran')
print(nombres)
nombres.remove('beto')
print(nombres)
nombres.insert(1, 'gabriela')
print(nombres)
# se pueden anidar
nombres.append([10, 20, 30])
print(nombres)
# recorrer una lista
for nombre in nombres:
    print(f'nombre: {nombre}')