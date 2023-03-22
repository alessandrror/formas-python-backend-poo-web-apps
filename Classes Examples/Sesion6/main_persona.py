from persona import Persona

alicia = Persona('alicia','hernandez', '1234567889', 25)
beto = Persona('beto','garcia', '0987654321', 35)

print(f'nombre de alicia: {alicia.nombres}')
print(f'apellido de alicia: {alicia._apellidos}')
# edad es privado
# print(f'edad de alicia: {alicia.__edad}') 

# es privado
# print(alicia.__es_adulto())

alicia.mostrar_datos()
beto.mostrar_datos()