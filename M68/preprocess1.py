import json

# Load the JSON data from a file
with open('M68/dataset.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Function to check word count and format if greater than 99 words
def process_text(data):
    new_format = []
    
    for entry in data:
        input_text = entry["input"]
        output_text = entry["output"]

        if len(input_text.split()) > 99:
            new_format.append({"text": input_text})
        if len(output_text.split()) > 99:
            new_format.append({"text": output_text})
    
    return new_format

# Convert and filter data
result = process_text(data)

# Save the result to a new JSON file
with open('unlabeled_dataset.json', 'w') as output_file:
    json.dump(result, output_file, indent=4)

print("Conversion completed and saved to 'output_data.json'")
