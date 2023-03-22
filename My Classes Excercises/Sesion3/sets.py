# programa para uso de sets
clientes = {'alicia', 'beto', 'camila', 'diana'}
print(len(clientes))

# son desordenados y debido a eso no son indexados
print(clientes)
# print(clientes[1]) no se puede recorrer por index

# los sets son dinamicos
clientes.add('eva')
print(clientes)

clientes.remove('beto')
print(clientes)

clientes.discard('camila')
print(clientes)

# son inmutables por index 
# clientes[1] = 'fran'

# no acepta repetido
clientes.add('eva')
print(clientes)

# recorrer un set
for cliente in clientes :
    print(f' --> Nombre: {cliente}')

