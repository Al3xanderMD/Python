import re

def extract_number(text: str) -> int:
    match = re.search(r'\d+', text)
    if match:
        return int(match.group())
    else:
        return None

string = input("Enter a string with a number: ")
print("The number is:", extract_number(string))