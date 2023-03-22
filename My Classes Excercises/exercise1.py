Renta = None
AFP = None
SeguroSocial = None
SueldoBase = None
RentaTotal = None
AFPTotal = None
SeguroSocialTotal = None
Nombre = None
X = None

AFP = 7.25/100
SeguroSocial = 3/100

Nombre = input('Ingrese su nombre: ')
SueldoBase = int(input('Ingrese su sueldo nominal: '))

if (SueldoBase >0 and SueldoBase < 365 ) :
    print('Ingrese un valor válido.')

SeguroSocial = (SueldoBase * SeguroSocial)
AFPTotal = (SueldoBase*AFP)

if (SueldoBase >= 365 and SueldoBase < 472.01) :
    X = input('Si usted desea descontar unicamente Renta, presione 1. Si desea descontar AFP y Seguro Social, presione 2.')
    if (X == 1) :
        Renta = 10/100
        SueldoNeto = SueldoBase - (SueldoBase*Renta)
        print(Nombre,', su sueldo base es ',SueldoBase,' si se descuenta ', RentaTotal, ' de Renta.')
        print('Su sueldo neto es de: ', SueldoNeto)
    
    elif (X == 2) :
        SueldoNeto = SueldoBase - ((SueldoBase*AFP) - (SueldoBase*SeguroSocial))
        print(Nombre,', su sueldo base es ',SueldoBase,' y si se descuenta de AFP, ', AFPTotal,' y ',SeguroSocialTotal,' de Seguro Social.')
        print('Su sueldo neto es de: ', SueldoNeto)

    else :
        print('Ingrese una opción válida.')

if (SueldoBase >= 472.01 and SueldoBase < 895.25) :
	Renta = 10/100
	RentaTotal = (SueldoBase*Renta) + 17.67
	SueldoNeto = SueldoBase - AFPTotal - SeguroSocialTotal - RentaTotal
	print(Nombre,", su sueldo base es ",SueldoBase," y se descuenta ", RentaTotal, " de Renta, ", AFPTotal, " de AFP y ", SeguroSocialTotal, " de Seguro Social.")
	print("Su sueldo neto es de: ", SueldoNeto)

if (SueldoBase >= 895.25 and SueldoBase < 2038.10 ) :
	Renta = 20/100
	RentaTotal = (SueldoBase*Renta) + 60.00
	SueldoNeto = SueldoBase - ((SueldoBase*AFP) - (SueldoBase*SeguroSocial) - (SueldoBase*Renta))
	print(Nombre,", su sueldo base es ",SueldoBase," y se descuenta ", RentaTotal, " de Renta, ", AFPTotal, " de AFP y ", SeguroSocialTotal, " de Seguro Social.")
	print("Su sueldo neto es de: ", SueldoNeto)

if (SueldoBase >= 2038.10) :
	Renta = 30/100
	RentaTotal = (SueldoBase*Renta) + 288.57
	SueldoNeto = SueldoBase - ((SueldoBase*AFP) - (SueldoBase*SeguroSocial) - (SueldoBase*Renta))
	print(Nombre,", su sueldo base es ",SueldoBase," y se descuenta ", RentaTotal, " de Renta, ", AFPTotal, " de AFP y ", SeguroSocialTotal, " de Seguro Social.")
	print("Su sueldo neto es de: ", SueldoNeto)

print('Fin del programa')