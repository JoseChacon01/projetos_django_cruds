from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render #render faz a redenderização, converte phyton para html
from django.http import HttpResponse

def olamundo(request):
    return HttpResponse('<h1>Olá Mundo</h1>')

def disciplina(request):
    return HttpResponse('<h1>Beck-End</h1>') 

def home(request):
    return HttpResponse('<h1>Pagina Inicial</h1>')    

def minha_idade(request, idade):
    return HttpResponse('A idade é '+str (idade))    

def meu_nome(request, nome):
    return HttpResponse ('O nome é: '+nome)

def minha_nota(request, nota):
    dobro = 2*float(nota)
    return HttpResponse ('Dobro da nota: '+str(dobro))


def cadastro(request, nome, idade):
    return HttpResponse ('O nome é: '+nome+' e idade: '+str(idade))

def pagina1(request):
    return HttpResponse('<h1><a href="/pagina2/">link_para_Pagina_2</a></h1>')

    
def pagina2(request):
    return HttpResponse('<h1><a href="/pagina1/">link_para_Pagina_1</a></h1>')

def home (request):
    context = {
        'nome': 'IFRN',
        'curso': 'Sistemas para Internet',
        'periodo': '3º Periodo',
        'media': 80,
        'notas': [50, 70],
        }
    return render (request, 'index.html', context)
    
def contato (request):
    return render (request, 'contato.html')