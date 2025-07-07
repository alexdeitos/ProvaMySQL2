import json
import re

def parse_questions(file_path):
    questions_data = []
    pk_counter = 1445
    prova_id = 2  # ID for the Prova instance

    # Add a single Prova entry
    questions_data.append({
        "model": "provas.prova",
        "pk": prova_id,
        "fields": {
            "nome": "AWS SysOps"
        }
    })

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file if line.strip()]  # Remove blank lines

    i = 0
    while i < len(lines):
        line = lines[i]

        if line.startswith("Question #"):
            # Extract question number and text (multi-line support)
            question_number = int(line.split('#')[1].strip())
            question_lines = []
            i += 1
            while i < len(lines) and not re.match(r'^[A-E]\.', lines[i]):  # Updated to A-E for 5 options
                question_lines.append(lines[i])
                i += 1
            question_text = ' '.join(question_lines).strip()

            question_pk = pk_counter + 1  # Reserve next pk for Pergunta

            # Add Pergunta entry
            questions_data.append({
                "model": "provas.pergunta",
                "pk": question_pk,
                "fields": {
                    "prova": prova_id,
                    "texto": question_text
                }
            })
            pk_counter += 1

            # Collect answers (multi-line support)
            answers = []
            correct_answer_letters = set()

            while i < len(lines) and re.match(r'^[A-E]\.', lines[i]):  # Updated to A-E
                answer_lines = [lines[i]]
                i += 1
                while i < len(lines) and not re.match(r'^[A-E]\.|Correct Answer:', lines[i]):
                    answer_lines.append(lines[i])
                    i += 1
                answer_text = ' '.join(answer_lines).strip()
                answers.append({
                    "texto": answer_text,
                    "letter": answer_text[0]  # Extract the letter (A, B, C, etc.)
                })

            # Check for Correct Answer line and handle multiple answers
            if i < len(lines) and lines[i].startswith("Correct Answer:"):
                correct_answer_letters = set(lines[i].split(":")[1].strip().split(","))
                i += 1

            # Add Resposta entries
            for ans in answers:
                questions_data.append({
                    "model": "provas.resposta",
                    "pk": pk_counter + 1,
                    "fields": {
                        "pergunta": question_pk,
                        "texto": ans["texto"],
                        "correta": ans["letter"] in correct_answer_letters
                    }
                })
                pk_counter += 1

        else:
            i += 1

    return questions_data

# Execute and save the JSON
file_path = '100perguntas.txt'
json_data = parse_questions(file_path)

with open('sysops.json', 'w', encoding='utf-8') as json_file:
    json.dump(json_data, json_file, ensure_ascii=False, indent=2)

print("JSON file 'sysops.json' has been created.")