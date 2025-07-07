from bs4 import BeautifulSoup
import re

# Read the HTML file
with open('testeSysOps.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find all question blocks
question_blocks = soup.find_all('div', class_='result-pane--question-result-pane-wrapper--2bGiz')

# Initialize output string
output = ""

# Process each question block
for idx, block in enumerate(question_blocks, 1):
    # Extract question text
    question_text = block.find('div', id='question-prompt').get_text(strip=True)
    
    # Extract all answer options
    answer_blocks = block.find_all('div', class_='result-pane--answer-result-pane--Niazi')
    answers = []
    correct_answer_text = None
    
    # Process each answer
    for answer_block in answer_blocks:
        answer_text = answer_block.find('div', id='answer-text').get_text(strip=True)
        answers.append(answer_text)
        # Check for correct answer using class or "Resposta correta" label
        if 'answer-result-pane--answer-correct--PLOEU' in answer_block.get('class', []):
            correct_answer_text = answer_text.strip()
        else:
            # Fallback: Check for "Resposta correta" label
            correct_label = answer_block.find('span', class_='result-pane--answer-by-user-label--PSH86')
            if correct_label and correct_label.get_text(strip=True) in ('Resposta correta', 'Seleção correta','Sua resposta está correta','Sua seleção está correta'):
                correct_answer_text = answer_text.strip()
        
        # Debugging: Print classes for each answer block
        print(f"Question {idx}, Answer: {answer_text}, Classes: {answer_block.get('class', [])}")

    # Debugging: Print detected correct answer
    print(f"Question {idx}: Correct answer detected as: {correct_answer_text}")
    
    # Format the output for this question
    output += f"Pergunta {idx}\n{question_text}\n"
    for i, answer in enumerate(answers):
        # Normalize answer for comparison
        answer_normalized = answer.strip()
        # Add asterisk to the correct answer
        marker = ' *' if correct_answer_text and answer_normalized == correct_answer_text else ''
        output += f"{chr(97 + i)}) {answer}{marker}\n"
    output += "\n"

# Write the output to a file
with open('formatted_questions_sys.txt', 'w', encoding='utf-8') as f:
    f.write(output)

print("Questions have been extracted and formatted in 'formatted_questions_sys.txt'")
