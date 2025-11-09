
import json
import os

# Get absolute path of the script folder
script_dir = os.path.dirname(os.path.abspath(__file__))
json_file = os.path.join(script_dir, "bbc_data.json")

print("Looking for JSON file here:", json_file)  # debug line

try:
    with open(json_file, "r", encoding="utf-8") as f:
        programmes = json.load(f)
except FileNotFoundError:
    print("ERROR: JSON file not found.")
    exit()

# Ask for category
category = input("Enter a category (e.g., sports, music, news, culture): ").lower()

# Find matches
matches = [item["title"] for item in programmes if item["category"].lower() == category]

# Display results
if matches:
    print(f"\nRecommendations for '{category.title()}':")
    for title in matches:
        print("•", title)
else:
    print(f"No programmes found for category '{category.title()}'.")
