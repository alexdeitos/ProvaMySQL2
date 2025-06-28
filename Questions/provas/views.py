from django.urls import reverse
from django.shortcuts import render, redirect
from .models import Pergunta, Prova
from .forms import ProvaSelectForm
import random
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


def index(request):
    if request.method == 'POST':
        form = ProvaSelectForm(request.POST)
        if form.is_valid():
            prova_id = form.cleaned_data['prova'].id
            url = reverse('exibir_prova', args=[prova_id])
            return redirect(url)
    else:
        form = ProvaSelectForm()

    return render(request, 'index.html', {'form': form})

"""
def exibir_prova(request, prova_id):
    prova = Prova.objects.get(id=prova_id)
    perguntas = Pergunta.objects.filter(prova=prova)
    return render(request, 'exibir_prova.html', {'prova': prova, 'perguntas': perguntas})
"""
def exibir_prova(request, prova_id):
    prova = Prova.objects.get(id=prova_id)
    perguntas = prova.pergunta_set.all().order_by('?')  # Ordena as perguntas de forma aleatória

    context = {
        'prova': prova,
        'perguntas': perguntas,
    }

    return render(request, 'exibir_prova.html', context)

def resultados_prova(request):
    corretas = request.GET.get('corretas')
    incorretas = request.GET.get('incorretas')
    nao_respondidas = request.GET.get('naoRespondidas')

    return render(request, 'resultados.html', {
        'corretas': corretas,
        'incorretas': incorretas,
        'nao_respondidas': nao_respondidas,
    })

@login_required
def excluir_pergunta(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, id=pergunta_id)
    if request.method == 'POST':
        # Excluir a pergunta
        pergunta.delete()
        # Redirecionar de volta para a página de exibição da prova
        return redirect('exibir_prova', prova_id=pergunta.prova.id)
    # Se o método da requisição não for POST, renderize uma página de erro ou redirecione para outra página