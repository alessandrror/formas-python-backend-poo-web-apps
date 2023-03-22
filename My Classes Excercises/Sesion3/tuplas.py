# programa para usode tuplas

lenguajes = ('C++', 'Python', 'PHP', 'JAVA', 'JAVA')
print(f'Longitud de lenguajes: {len(lenguajes)} y su contenido: {lenguajes}')

# son inmutables, sus elementos no cambian
# --> lenguajes[0] = 'C#', operacion no soportada

# son de tamaño estático
# --> lenguajes.append('Javascript')

# contar el numero de veces que aparece el valor que recibe .count()
print(lenguajes.count('JAVA'))
# regresar el primer indice donde aparece el valor que recibe .index()
print(lenguajes.index('JAVA'))

# recorrer una tupla
for lenguaje in lenguajes :
    print(f'Lenguaje: {lenguaje}')

# convertir tupla a lista
print(f'El tipo de dato de lista es: {type(list)} y su estructura es: {list}')
lista = list(lenguajes)
print(f'El tipo de dato de lista es: {type(lista)} y su estructura es: {lista}')

# acceder a metados de una lista dentro de una tupla
aux = (1,5,6,[7,8,9])
print(aux[3])
aux[3].append(10)
print(aux)
