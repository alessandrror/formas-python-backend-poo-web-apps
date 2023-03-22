from figuras.figura import Figura
from figuras.rectangulo import Rectangulo
from figuras.circulo import Circulo

f = Figura('Figura')
r = Rectangulo('Rectangulo', 10, 20)
c = Circulo('Circulo', 5)

f.mostrar_nombre()
r.mostrar_nombre()
c.mostrar_nombre()

print(f'El area de {f.nombre} es: {f.calcular_area():.2f}')
print(f'El perimetro de {f.nombre} es: {f.calcular_perimetro():.2f}')

print(f'El area de {r.nombre} es: {r.calcular_area():.2f}')
print(f'El perimetro de {r.nombre} es: {r.calcular_perimetro():.2f}')

print(f'El area de {c.nombre} es: {c.calcular_area():.2f}')
print(f'El perimetro de {c.nombre} es: {c.calcular_perimetro():.2f}')
