# from django.urls import reverse
# from django.shortcuts import render, redirect
# from .models import Pergunta, Prova
# from .forms import ProvaSelectForm
# import random
# from django.shortcuts import get_object_or_404
# from django.contrib.auth.decorators import login_required
# from django.views.decorators.csrf import csrf_exempt
# import logging
# import json
# from django.template.loader import render_to_string
# 
# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger(__name__)
# 
# def index(request):
#     if request.method == 'POST':
#         form = ProvaSelectForm(request.POST)
#         if form.is_valid():
#             prova_id = form.cleaned_data['prova'].id
#             url = reverse('exibir_prova', args=[prova_id])
#             return redirect(url)
#     else:
#         form = ProvaSelectForm()
# 
#     return render(request, 'index.html', {'form': form})
# 
# """
# def exibir_prova(request, prova_id):
#     prova = Prova.objects.get(id=prova_id)
#     perguntas = Pergunta.objects.filter(prova=prova)
#     return render(request, 'exibir_prova.html', {'prova': prova, 'perguntas': perguntas})
# """
# #def exibir_prova(request, prova_id):
# #    prova = Prova.objects.get(id=prova_id)
# #    perguntas = prova.pergunta_set.all().order_by('?')  # Ordena as perguntas de forma aleatória
# #
# #    context = {
# #        'prova': prova,
# #        'perguntas': perguntas,
# #    }
# #
# #    return render(request, 'exibir_prova.html', context)
# 
# def exibir_prova(request, prova_id):
#     try:
#         prova = Prova.objects.get(id=prova_id)
#         perguntas = prova.pergunta_set.all().order_by('?')[:60]  # Seleciona até 60 perguntas aleatoriamente
# 
#         context = {
#             'prova': prova,
#             'perguntas': perguntas,
#         }
#         return render(request, 'exibir_prova.html', context)
#     except Prova.DoesNotExist:
#         # Opcional: Lidar com o caso de prova não encontrada
#         return render(request, 'erro.html', {'mensagem': 'Prova não encontrada.'}, status=404)
# 
# def resultados_prova(request):
#     corretas = request.GET.get('corretas')
#     incorretas = request.GET.get('incorretas')
#     nao_respondidas = request.GET.get('naoRespondidas')
# 
#     return render(request, 'resultados.html', {
#         'corretas': corretas,
#         'incorretas': incorretas,
#         'nao_respondidas': nao_respondidas,
#     })
# 
# @login_required
# def excluir_pergunta(request, pergunta_id):
#     pergunta = get_object_or_404(Pergunta, id=pergunta_id)
#     if request.method == 'POST':
#         # Excluir a pergunta
#         pergunta.delete()
#         # Redirecionar de volta para a página de exibição da prova
#         return redirect('exibir_prova', prova_id=pergunta.prova.id)
#     # Se o método da requisição não for POST, renderize uma página de erro ou redirecione para outra página
# 
# @csrf_exempt
# def exportar_pdf(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         perguntas = data['perguntas']
#         pontuacao = data['pontuacao']
#         total_perguntas = len(perguntas)
# 
#         # Renderiza o conteúdo LaTeX
#         latex_content = render_to_string('provas/pdf_template.tex', {
#             'perguntas': perguntas,
#             'pontuacao': pontuacao,
#             'total_perguntas': total_perguntas
#         })
# 
#         # Salva o conteúdo LaTeX em um arquivo temporário
#         with open('temp.tex', 'w') as f:
#             f.write(latex_content)
# 
#         # Gera o PDF usando latexmk
#         subprocess.run(['latexmk', '-pdf', 'temp.tex'], check=True)
# 
#         # Lê o PDF gerado
#         with open('temp.pdf', 'rb') as f:
#             pdf_content = f.read()
# 
#         # Remove arquivos temporários
#         subprocess.run(['latexmk', '-c'], check=True)  # Limpa arquivos auxiliares
#         import os
#         os.remove('temp.tex')
#         os.remove('temp.pdf')
# 
#         response = HttpResponse(pdf_content, content_type='application/pdf')
#         response['Content-Disposition'] = 'attachment; filename="respostas_prova.pdf"'
#         return response
# 
#     return JsonResponse({'error': 'Método não permitido'}, status=405)
#     
from django.urls import reverse
from django.shortcuts import render, redirect
from .models import Pergunta, Prova
from .forms import ProvaSelectForm
import random
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import logging
import json
from django.template.loader import render_to_string  # Ensure this is present
from django.http import JsonResponse, HttpResponse  # Added HttpResponse
import subprocess
import os

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

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

def exibir_prova(request, prova_id):
    try:
        prova = Prova.objects.get(id=prova_id)
        perguntas = prova.pergunta_set.all().order_by('?')[:60]  # Seleciona até 60 perguntas aleatoriamente

        context = {
            'prova': prova,
            'perguntas': perguntas,
        }
        return render(request, 'exibir_prova.html', context)
    except Prova.DoesNotExist:
        return render(request, 'erro.html', {'mensagem': 'Prova não encontrada.'}, status=404)

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
        pergunta.delete()
        return redirect('exibir_prova', prova_id=pergunta.prova.id)

from django.utils.text import slugify  # For safe file naming if needed
from django.template.defaultfilters import slugify  # If using custom filters

@csrf_exempt
def exportar_pdf(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            perguntas = data.get('perguntas', [])
            pontuacao = data.get('pontuacao', 0)
            total_perguntas = len(perguntas)

            logger.debug("Received data: perguntas=%d, pontuacao=%d", len(perguntas), pontuacao)

            latex_content = render_to_string('provas/pdf_template.tex', {
                'perguntas': perguntas,
                'pontuacao': pontuacao,
                'total_perguntas': total_perguntas
            })

            with open('temp.tex', 'w', encoding='utf-8') as f:
                f.write(latex_content)
            logger.debug("temp.tex content: %s", latex_content[:500])  # Log first 500 chars

            try:
                result = subprocess.run(['pdflatex', '-interaction=nonstopmode', 'temp.tex'], 
                                      capture_output=True, text=True, check=True, cwd=os.getcwd())
                logger.debug("pdflatex output: %s", result.stdout)
                if result.stderr:
                    logger.error("pdflatex errors: %s", result.stderr)
            except subprocess.CalledProcessError as e:
                logger.error("pdflatex failed: %s", e.stderr)
                return HttpResponse("Erro ao compilar LaTeX: " + e.stderr, status=500)

            if os.path.exists('temp.pdf'):
                with open('temp.pdf', 'rb') as f:
                    pdf_content = f.read()
                os.remove('temp.tex')
                os.remove('temp.pdf')
                response = HttpResponse(pdf_content, content_type='application/pdf')
                response['Content-Disposition'] = 'attachment; filename="respostas_prova.pdf"'
                return response
            else:
                logger.error("temp.pdf not found")
                return HttpResponse("PDF não gerado", status=500)

        except json.JSONDecodeError as e:
            logger.error("Invalid JSON: %s", e)
            return HttpResponse("Dados JSON inválidos", status=400)
        except Exception as e:
            logger.error("Unexpected error: %s", e)
            return HttpResponse("Erro inesperado", status=500)

    return JsonResponse({'error': 'Método não permitido'}, status=405)
