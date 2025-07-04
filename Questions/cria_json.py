import json

def parse_questions(file_path):
    questions = []
    pk_counter = 1
    prova_id = 1  # ID fixo da prova

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file if line.strip()]  # remove linhas em branco

    i = 0
    while i < len(lines):
        line = lines[i]

        if line.startswith("Pergunta "):
            question_number = int(line.split()[1])
            question_text = lines[i + 1]
            question_pk = pk_counter

            questions.append({
                "model": "provas.pergunta",
                "pk": pk_counter,
                "fields": {
                    "prova": prova_id,
                    "texto": question_text
                }
            })
            pk_counter += 1

            i += 2  # pula para as alternativas
            answers = []
            # captura até 4 alternativas
            while i < len(lines) and lines[i].startswith(('a)', 'b)', 'c)', 'd)')):
                option_letter = lines[i][0]
                answers.append({
                    "letter": option_letter,
                    "texto": lines[i]
                })
                i += 1

            # a próxima linha é a resposta correta
            correct_letter = lines[i].strip().lower()
            i += 1

            # adiciona as respostas no JSON
            for ans in answers:
                questions.append({
                    "model": "provas.resposta",
                    "pk": pk_counter,
                    "fields": {
                        "pergunta": question_pk,
                        "texto": ans["texto"],
                        "correta": ans["letter"].lower() == correct_letter
                    }
                })
                pk_counter += 1

        else:
            i += 1

    return questions

# Executa e salva o JSON
file_path = 'azperguntas.txt'
json_data = parse_questions(file_path)

with open('output.json', 'w', encoding='utf-8') as json_file:
    json.dump(json_data, json_file, ensure_ascii=False, indent=2)

print("JSON file 'output.json' has been created.")
