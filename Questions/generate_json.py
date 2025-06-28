import json
import re
import os

# Define the prova_id
prova_id = 4

# Caminho completo para o arquivo questions.txt
current_directory = os.path.dirname(os.path.abspath(__file__))
questions_file_path = os.path.join(current_directory, 'perguntas.txt')

# Leitura do arquivo de texto
with open(questions_file_path, 'r', encoding='utf-8') as file:
    data = file.read()

# Regex para capturar cada pergunta e suas respostas
question_pattern = re.compile(
    r'Question #(\d+)\s*\n(.*?)\s*\nA\.\s(.*?)\s*\nB\.\s(.*?)\s*\nC\.\s(.*?)\s*\nD\.\s(.*?)'
    r'(?:\s*\nE\.\s(.*?))?(?:\s*\nF\.\s(.*?))?\s*\nCorrect Answer: ([A-Z,]+)',
    re.DOTALL
)

# Inicialização das listas de perguntas e respostas
questions = []
answers = []
pergunta_pk = 1
resposta_pk = 1

# Processar cada pergunta
for match in question_pattern.finditer(data):
    numero_questao = match.group(1).strip()
    texto = match.group(2).strip()
    texto_com_numero = f"{numero_questao}. {texto}"
    respostas = [match.group(i).strip() for i in range(3, 9) if match.group(i)]
    corretas = match.group(9).strip().split(',')

    # Adicionar pergunta ao JSON
    questions.append({
        "model": "provas.pergunta",
        "pk": pergunta_pk,
        "fields": {
            "prova": prova_id,
            "texto": texto_com_numero,
            "imagem": None
        }
    })

    # Adicionar respostas ao JSON
    for i, resposta in enumerate(respostas):
        answers.append({
            "model": "provas.resposta",
            "pk": resposta_pk,
            "fields": {
                "pergunta": pergunta_pk,
                "texto": resposta,
                "correta": chr(65 + i) in corretas  # 'A' == chr(65), 'B' == chr(66), etc.
            }
        })
        resposta_pk += 1

    pergunta_pk += 1

# Combinar perguntas e respostas
output = questions + answers

# Salvar no arquivo JSON
output_file_path = os.path.join(current_directory, 'questions.json')
with open(output_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(output, json_file, indent=4)

print("Arquivo questions.json gerado com sucesso!")

