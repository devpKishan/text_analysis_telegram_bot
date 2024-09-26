# analysis.py
import re

def analyze_message(message):
    words = re.split(r"\W+", message.text)[:-2]
    characters = len(message.text) - 16
    sentences = len(re.split(r"\.|\n", message.text))
    syllables = sum(1 for word in words if len(word) > 1 and re.search(r"[aeiouy]", word))
    unique_words = set(words)
    misspelled_words = [word for word in words if word not in unique_words]
    repeated_words = set([word for word in words for w in words if word == w])
    nouns = re.findall(r'\b[A-Z][a-z]*\b', message.text)
    verbs = re.findall(r'\b\w+ing\b|\b\w+ed\b|\b\w+es\b', message.text)
    adjectives = re.findall(r'\b\w+ous\b', message.text)
    adverbs = re.findall(r'\b\w+ly\b', message.text)

    return {
        "words": len(words),
        "characters": characters,
        "sentences": sentences,
        "syllables": syllables,
        "unique_words": len(unique_words),
        "misspelled_words": misspelled_words,
        "repeated_words": repeated_words,
        "nouns": nouns,
        "verbs": verbs,
        "adjectives": adjectives,
        "adverbs": adverbs,
    }
