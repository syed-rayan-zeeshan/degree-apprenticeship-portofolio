import json

def load_data():
    """
    Loads the BBC content data from a JSON file.
    """
    try:
        with open("bbc_data.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Error: Could not find bbc_data.json file.")
        return []

def recommend_content(keyword, data):
    """
    Recommends BBC content based on user's category keyword.
    """
    return [item for item in data if keyword.lower() in item["category"].lower()]

def display_recommendations(recommendations, keyword):
    """
    Displays recommended BBC programmes in a nice format.
    """
    print(f"\n🎬 Recommendations for '{keyword.capitalize()}':")
    if not recommendations:
        print(" No matches found for that category.")
    else:
        for item in recommendations:
            print(f"• {item['title']}  ({item['category']})")

def main():
    """
    Runs the BBC Content Recommender application.
    """
    print("===  BBC Content Recommender ===")
    print("Discover BBC shows and programmes by topic!\n")

    data = load_data()
    if not data:
        return

    keyword = input("Enter a category (e.g. sports, music, news): ").strip()
    recommendations = recommend_content(keyword, data)
    display_recommendations(recommendations, keyword)

if __name__ == "__main__":
    main()

