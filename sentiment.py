# sentiment.py

def simple_sentiment(text):
    text = text.lower()

    positive_words = ["good", "great", "excellent", "happy", "love", "nice"]
    negative_words = ["bad", "sad", "terrible", "poor", "hate", "angry"]

    score = 0
    for w in positive_words:
        if w in text:
            score += 1

    for w in negative_words:
        if w in text:
            score -= 1

    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    else:
        return "Neutral"
