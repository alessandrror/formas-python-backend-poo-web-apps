from django.shortcuts import render

# Create your views here.
def function_index(request) :
    return render(request, 'empleados/index.html')

def listar_empleados(request) :
    empleados = {
        'titulo': 'Tabla de Empleados',
        'atributos': [
            {'nombre': 'Alexis', 
            'edad': '21'},
            {'nombre': 'Enrique',
            'edad': '32'},
            {'nombre': 'Alan',
            'edad': '35'},
            {'nombre': 'Alicia',
            'edad': '26'},
            {'nombre': 'Elisa',
            'edad': '25'},
            {'nombre': 'Anderson',
            'edad': '28'},
        ]
    }
    return render(request, 'empleados/lista-empleados.html', empleados)