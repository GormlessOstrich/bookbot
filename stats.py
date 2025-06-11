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

def get_values(char_dict):
    return char_dict["num"]

def dict_sort(char_dict):
    new_list = []
    for key, value in char_dict.items():
        new_dict = {
            "char": key,
            "num": value
            }
        if key.isalpha():
            new_list.append(new_dict)
    new_list.sort(reverse=True, key=get_values)
    return new_list