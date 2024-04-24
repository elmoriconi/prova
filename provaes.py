def word_frequency(text, stopwords):
    text = text.lower()
    text = text.replace(".", "").replace(",", "").replace(":", "").replace("?", "")
    words = list(text.split())
    words = set(words)
    stopwords = set(stopwords)
    words = words.difference(stopwords)
    print(words)

stopwords = ["the", "and", "is", "in", "on", "of"]
text = "The cat in the hat. The cat is blue and red. The cat and the dog." 
word_frequency(text, stopwords)