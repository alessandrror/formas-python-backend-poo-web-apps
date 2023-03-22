from django.shortcuts import render

# Create your views here.
def function_index(request) :
    return render(request, 'inicio/index.html')

def listar_personas(request) :
    personas = {
        'titulo': 'Lista de personas',
        'nombres': [
            'alicia',
            'beto',
            'carlos',
            'diana',
        ]
    }
    return render(request, 'inicio/lista-personas.html', personas)