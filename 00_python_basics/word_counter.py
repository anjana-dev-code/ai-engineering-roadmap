def top_words(text,n):

    text = text.lower()

    text = text.replace(";", "")
    text = text.replace("?", "")
    text = text.replace("!", "")
    text = text.replace(",", "")
    text = text.replace(".", "")

    words = text.split()

    counts = {}

    for word in words:
        if word in counts:
           counts[word] += 1
        else:
           counts[word] = 1

    ranked = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)

    return ranked[:n]


print(top_words("Is it a dog? Yes; it is a dog!", 2))

print(top_words("It is a dog!, It is a cat!", 4))