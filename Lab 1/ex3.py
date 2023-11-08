def count_occurrences(string, substring):
    return string.count(substring)

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
print("The number of occurrences of the first string in the second is:", count_occurrences(string2, string1))
