# retornos multiples

# TODO: incluir todos los meses
def dias_mes(mes):
    if mes==12:
        return 31
    elif mes==11:
        return 30
    elif mes==2:
        return 28
    else:
        return 0
    
print(dias_mes(12))