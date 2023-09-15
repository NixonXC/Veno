import json

with open('jokes.txt', 'r', encoding='utf-8') as f:
    jokes = f.readlines()

filename = input("What should be the filename? ")

jokes_dict = {"programjokes": []}
for i, joke in enumerate(jokes):
    joke = joke.strip() 
    if '...' in joke:
        parts = joke.split("...", maxsplit=1) 
    else:
        parts = joke.split("?", maxsplit=1) 
    if len(parts) != 2:
        continue  
    jokes_dict["programjokes"].append({
        "id": str(i + 1),
        "setup": parts[0].strip(),
        "punchline": parts[1].strip()
    })

# Write the jokes to a JSON file
with open(f'{filename}.json', 'w', encoding='utf-8') as f:
    json.dump(jokes_dict, f, indent=2, ensure_ascii=False)
