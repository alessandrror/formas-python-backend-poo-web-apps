# Implementar la clase circulo que herede de
# figura y calcular area y perimetro

# area = pi*r^2
# perimetro = 2*pi*r

# radian es un arco con longitud de radio
# un circulo tiene 6.28 radianes

from figuras.figura import Figura
import math

class Circulo(Figura) :
    def __init__(self, nombre, radio):
        super().__init__(nombre)
        self.radio = radio

    def calcular_area(self):
        return math.pi*((self.radio)^2)

    def calcular_perimetro(self):
        return (2*math.pi*(self.radio))
