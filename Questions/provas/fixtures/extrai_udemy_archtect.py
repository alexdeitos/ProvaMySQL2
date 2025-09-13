from bs4 import BeautifulSoup

# Read the HTML file
# Replace 'solutionsArchtect.html' with the path to your HTML file
with open("solutionsArchtect.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, "html.parser")

# Find all question blocks
question_blocks = soup.find_all(
    "div", class_="result-pane--question-format--PBvdY"
)

# Initialize output string
output = ""

# Process each question block
for idx, block in enumerate(question_blocks, 1):
   question_text = [p.get_text(strip=True) for p in block.find_all("p")]
    
   # Extract all answer options
   answer_blocks = block.find_all('div', class_='result-pane--answer-result-pane--Niazi')
   answers = []
   correct_answer_text = None
   print(answer_blocks)
   #for answer_block in answer_blocks:
   #     print(answer_block)

    
# Write the output to a file
with open("formatted_questions_arch.txt", "w", encoding="utf-8") as f:
    f.write(output)

print("Questions have been extracted and formatted in 'formatted_questions_arch.txt'")
