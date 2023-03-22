# programa para uso de sets
clientes = {'alicia','beto','camila','diana'}

print(len(clientes))
# son desordenados
print(clientes)
# no permiten acceso indexado
# print(clientes[1])

# son inmutables
# clientes[1] = 'fran'

# son dinamicos
clientes.add('eva')
print(clientes)
clientes.discard('beto')
print(clientes)

# no acepta repetidos
clientes.add('eva')
print(clientes)

# recorrer un set
for cliente in clientes:
    print(f'cliente: {cliente}')