def most_common_letter(text: str) -> str:
    filtered = "".join([char.lower() for char in text if char.isalpha()])
    freq = {}
    for char in filtered:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    max_freq = 0
    max_char = ""
    for char, count in freq.items():
        if count > max_freq:
            max_freq = count
            max_char = char
    return max_char

string = input("Introduceti un string: ")
print("Cea mai comuna litera este:", most_common_letter(string))
