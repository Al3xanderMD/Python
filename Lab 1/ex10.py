def count_words(text: str) -> int:
    return len(text.split())

string = input("Enter a string: ")
print("The number of words is:", count_words(string))