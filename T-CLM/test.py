import json

with open('T-CLM/labeled_dataset.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

length = len(data)

print(length)