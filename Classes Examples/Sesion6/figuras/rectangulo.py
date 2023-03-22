from figuras.figura import Figura

class Rectangulo(Figura):
    def __init__(self, nombre, base, altura):
        super().__init__(nombre)
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base*self.altura
    
    def calcular_perimetro(self):
        return 2*(self.base+self.altura)