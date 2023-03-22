# uso de parametros con valores por defecto
# valores multiples de retorno

def calculo_descuentos(sueldo, isss=0.03, afp=0.0725):
    desc_afp = sueldo * afp
    if sueldo < 1000:
        desc_isss = sueldo * isss
    else:
        desc_isss = 30

    return desc_isss, desc_afp, desc_afp+desc_isss


d1 = calculo_descuentos(800)
print('los descuentos en d1 son:', d1)
d2 = calculo_descuentos(800, 0.04)
print('los descuentos en d2 son:', d2)
d3 = calculo_descuentos(800, 0.04, 0.1)
print('los descuentos en d3 son:', d3)
d4 = calculo_descuentos(800, afp=0.1)
print('los descuentos en d4 son:', d4)
d5 = calculo_descuentos(800, isss=0.04)
print('los descuentos en d5 son:', d5)
d6 = calculo_descuentos(800, afp=0.08, isss=0.04)
print('los descuentos en d6 son:', d6)
