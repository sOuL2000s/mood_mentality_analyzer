from transformers import pipeline

def analyze_mood(sentence):
    # Load a sentiment analysis pipeline
    sentiment_analyzer = pipeline("sentiment-analysis")

    # Get the sentiment analysis result
    result = sentiment_analyzer(sentence)[0]
    mood = result['label']
    confidence = result['score']

    # Determine mentality from sentiment
    if mood == "POSITIVE":
        mentality = "Optimistic, Positive Outlook"
    elif mood == "NEGATIVE":
        mentality = "Pessimistic, Negative Outlook"
    else:
        mentality = "Neutral, Balanced Outlook"

    return {
        "mood": mood,
        "confidence": confidence,
        "mentality": mentality
    }

# Example usage
sentence = input("Enter a sentence to analyze mood and mentality: ")
analysis = analyze_mood(sentence)

print("Mood:", analysis["mood"])
print("Confidence:", analysis["confidence"])
print("Mentality:", analysis["mentality"])
