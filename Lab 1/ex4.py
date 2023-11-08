def convert_to_underscores(string):
    words = []
    current_word = ""
    for i, char in enumerate(string):
        if char.isupper():
            if current_word:
                words.append(current_word)
            current_word = char.lower()
        else:
            current_word += char
    if current_word:
        words.append(current_word)
    return "_".join(words)

string = input("Introduceti un string in UpperCamelCase: ")
print("String-ul in lowercase_with_underscores este:", convert_to_underscores(string))
