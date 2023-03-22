from persona import Persona

alicia = Persona('alicia', 'hernandez', '123456789', 25)
beto = Persona('beto', 'garcia', '987654321', 35)

# propiedad publica, puede acceder
print(f'nombre de alicia: {alicia.nombres}')

# propiedad protegida, accede por herencia
print(f'apellido de alicia: {alicia._apellidos}')

# propiedad privada, no puede acceder y da error
# print(f'edad de alicia: {alicia.__edad}')

# ------------------------------------------------

# es privado y no permite invocar el metodo
# alicia.__es_adulto()

# es publico y permite invocar el metodo
alicia.mostrar_datos()
beto.mostrar_datos()