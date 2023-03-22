# programa para uso de tuplas
lenguajes = ('C++','Python','PHP','JAVA', 1, (1,2))
print(len(lenguajes))
print(lenguajes)
print(lenguajes[0])

# son inmutables, sus elementos no cambian
# lenguajes[0] = 'C#' # operacion no soportada

# son estaticas
# lenguajes.append('Javascript')

# recorrer una tupla
for lenguaje in lenguajes:
    print(f'lenguaje: {lenguaje}')

lista = list(lenguajes)
print(lista)
print(type(lista))

aux = (1,5,6,[7,8,9])
print(aux[3])
aux[3].append(7)
print(aux)