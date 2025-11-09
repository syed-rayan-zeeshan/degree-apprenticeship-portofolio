# BBC Audience Trend Analyzer (Beginner / No Libraries)
# Reads fake BBC viewing data and shows which categories are most popular.

import json  # built-in, safe to use

# Try to load data from a JSON file
try:
    with open("bbc_audience_data.json", "r", encoding="utf-8") as f:
        audience_data = json.load(f)
except FileNotFoundError:
    print("Error: bbc_audience_data.json not found. Using example data instead.\n")
    audience_data = [
        {"category": "News", "views": 125000},
        {"category": "Sport", "views": 97000},
        {"category": "Music", "views": 64000},
        {"category": "Drama", "views": 52000},
        {"category": "Education", "views": 43000},
        {"category": "News", "views": 88000},
        {"category": "Sport", "views": 105000},
        {"category": "Music", "views": 71000},
        {"category": "Drama", "views": 66000},
        {"category": "Education", "views": 50000}
    ]

# Dictionary to store total views per category
category_totals = {}

# Add up views for each category
for entry in audience_data:
    category = entry["category"]
    views = entry["views"]

    if category in category_totals:
        category_totals[category] += views
    else:
        category_totals[category] = views

# Sort by most popular
sorted_categories = sorted(category_totals.items(), key=lambda x: x[1], reverse=True)

# Print report
print("=== BBC Audience Trend Report ===\n")
for category, total in sorted_categories:
    print(f"{category:<12}: {total:,} views")

# Simple text-based bar chart
print("\n=== Bar Chart ===")
for category, total in sorted_categories:
    bar_length = total // 10000  # 1 block per 10,000 views
    print(f"{category:<12}: " + "█" * bar_length)

# Find the top category
top_category = sorted_categories[0][0]
print(f"\nMost popular category: {top_category}")
