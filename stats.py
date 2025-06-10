def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    lowercase = text.lower()
    count = {}
    for char in lowercase:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    return count