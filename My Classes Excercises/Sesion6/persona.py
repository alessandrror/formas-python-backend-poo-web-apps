class Persona_ :
    pass

p = Persona_()

print(type(p))

class Persona :
    def __init__(self, nombres, apellidos, dui, edad) :
        self.nombres = nombres # atributo: publico
        self._apellidos = apellidos # atributo: _protegido
        self.__dui = dui # atributo: __privado
        self.__edad = edad # atributo: __privado
        # self.mostrar_datos()
        # el constructor permite ejecutar metodos dentro de su propia instancia

# metodo privado

    def __es_adulto(self) : 
        return self.__edad >= 18

# metodo publico

    def mostrar_datos(self) :
        print('---------------------------------------------------')
        print(
            f'Nombres: {self.nombres}\n'
            f'Apellidos: {self._apellidos}\n'
            f'Edad: {self.__edad}, es adulto: {self.__es_adulto()}\n'
            f'DUI: {self.__dui}\n'
            # f'----------------------------------'
        )
