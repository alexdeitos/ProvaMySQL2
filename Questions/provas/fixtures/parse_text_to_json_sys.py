import json
import re

def parse_questions(file_path):
    questions_data = []
    pk_counter = 1596
    prova_id = 2  # ID for the Prova instance

    # Add a single Prova entry
#    questions_data.append({
#        "model": "provas.prova",
#        "pk": prova_id,
#        "fields": {
#            "nome": "Azure Fundamentals"
#        }
#    })

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = [line.strip() for line in file if line.strip()]  # Remove blank lines
            print(f"Loaded {len(lines)} lines from {file_path}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found. Please check the file path.")
        return questions_data
    except UnicodeDecodeError:
        print(f"Error: File '{file_path}' cannot be decoded with UTF-8. Check the encoding.")
        return questions_data

    i = 0
    while i < len(lines):
        line = lines[i]

        if line.startswith("Pergunta "):
            # Extract question number and text
            try:
                question_number = int(line.split()[1])
                question_text = lines[i + 1]
                question_pk = pk_counter + 1  # Reserve next pk for Pergunta

                print(f"Processing Question {question_number}: {question_text}")
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

                # Move to answers
                i += 2
                answers = []
                while i < len(lines) and lines[i].startswith(('a)', 'b)', 'c)', 'd)', 'e)')):
                    answer_text = lines[i]
                    # Check if this is the correct answer (ends with *)
                    is_correct = answer_text.endswith('*')
                    # Remove * from the text for storage
                    clean_answer_text = re.sub(r'\s*\*$', '', answer_text)
                    answers.append({
                        "texto": clean_answer_text,
                        "correta": is_correct
                    })
                    print(f"  Answer: {clean_answer_text}, Correct: {is_correct}")
                    i += 1

                # Add Resposta entries
                for ans in answers:
                    questions_data.append({
                        "model": "provas.resposta",
                        "pk": pk_counter + 1,
                        "fields": {
                            "pergunta": question_pk,
                            "texto": ans["texto"],
                            "correta": ans["correta"]
                        }
                    })
                    pk_counter += 1
                    print(f"  Added Resposta: {ans['texto']}, Correct: {ans['correta']}")
            except IndexError:
                print(f"Error: Insufficient lines for Question {question_number}. Check file format.")
                i += 1
                continue
        else:
            i += 1

    print(f"Total entries in questions_data: {len(questions_data)}")
    return questions_data

# Execute and save the JSON
file_path = 'formatted_questions_sys.txt'
json_data = parse_questions(file_path)

try:
    with open('output_sys.json', 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, ensure_ascii=False, indent=2)
    print("JSON file 'output_sys.json' has been created.")
except IOError as e:
    print(f"Error: Failed to write to 'output_sys.json'. Check permissions or file access. Error: {e}")
