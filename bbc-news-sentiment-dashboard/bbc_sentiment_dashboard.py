# BBC News Sentiment Dashboard (Beginner / No Libraries)
# Checks BBC-style headlines and guesses whether they sound positive, neutral, or negative.

# A small list of BBC-style headlines
headlines = [
    "BBC wins award for outstanding journalism",
    "Storm causes power outages across the UK",
    "New technology could improve healthcare",
    "Sports team suffers another defeat",
    "Government announces new climate policy",
    "BBC releases new music chart",
    "Science breakthrough discovered by BBC researchers",
    "Travel restrictions updated for international flights",
    "BBC Earth documentary wins global acclaim",
    "Radio 1 Chart Show celebrates top hits"
]

# Simple word lists to guess sentiment
positive_words = ["wins", "award", "improve", "breakthrough", "celebrates", "outstanding", "success", "new", "acclaim"]
negative_words = ["defeat", "storm", "power", "restriction", "outages", "delay", "crisis", "problem"]

# Counters
positive = 0
neutral = 0
negative = 0

# Go through each headline
for headline in headlines:
    headline_lower = headline.lower()
    found_positive = any(word in headline_lower for word in positive_words)
    found_negative = any(word in headline_lower for word in negative_words)

    if found_positive and not found_negative:
        positive += 1
        sentiment = "Positive"
    elif found_negative and not found_positive:
        negative += 1
        sentiment = "Negative"
    else:
        neutral += 1
        sentiment = "Neutral"

    print(f"'{headline}' → {sentiment}")

# Print summary
print("\n=== Sentiment Summary ===")
print("Positive headlines:", positive)
print("Neutral headlines:", neutral)
print("Negative headlines:", negative)

# Make a simple text-based bar chart
print("\n=== Bar Chart ===")
print("Positive: " + "█" * positive)
print("Neutral:  " + "█" * neutral)
print("Negative: " + "█" * negative)
