def find_most_frequent_word(text: str) -> str:
    words = text.split(" ")
    highest_count = 0
    winner = ""
    for w in words:
        if words.count(w) > highest_count:
            highest_count = words.count(w)
            winner = w
    return winner