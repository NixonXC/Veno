import json

# Open the input text file and read the questions
with open('data/roasts.txt', 'r', encoding='utf-8') as f:
    questions = f.readlines()

filename = input("What should be the filename? ")

# Process each question and convert it to a dictionary in JSON format
questions_dict = {"roasts": []}
for i, question in enumerate(questions):
    question = question.strip()  # Remove any leading or trailing whitespace
    questions_dict["roasts"].append({
        "id": str(i + 1),
        "roast": question
    })

# Write the questions to a JSON file
with open(f'{filename}.json', 'w', encoding='utf-8') as f:
    json.dump(questions_dict, f, indent=2, ensure_ascii=False)
