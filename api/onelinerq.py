import json

# Define the input file and output file names
input_file = "data/quotes.txt"
output_file = "quotes.json"

# Define an empty list to hold the quotes
quotes = []

# Open the input file and read the lines
with open(input_file, "r") as f:
    lines = f.readlines()

# Loop through the lines and extract the quote and author
for i, line in enumerate(lines):
    quote, author = line.strip().split(" - ")
    quotes.append({"id": i+1, "quote": quote, "author": author})

# Create a dictionary with the quotes list
data = {"quotes": quotes}

# Write the dictionary to the output file as JSON
with open(output_file, "w") as f:
    json.dump(data, f, indent=4)