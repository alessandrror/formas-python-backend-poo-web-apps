from figuras.figura import Figura
from figuras.rectangulo import Rectangulo
import math

f = Figura('Figura')
r = Rectangulo('Rectangulo', 10, 20)

f.mostrar_nombre()
r.mostrar_nombre()

print(f'el area de {f.nombre} es: {f.calcular_area()}')
print(f'el perimetro de {f.nombre} es: {f.calcular_perimetro()}')
print(f'el area de {r.nombre} es: {r.calcular_area()}')
print(f'el perimetro de {r.nombre} es: {r.calcular_perimetro()}')

