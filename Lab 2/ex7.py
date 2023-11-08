def palindrome_numbers(lst):
    palindromes = []
    for num in lst:
        if str(num) == str(num)[::-1]:
            palindromes.append(num)
    return (len(palindromes), max(palindromes))

string = input("Enter a list of numbers separated by spaces: ")
numbers = [int(num) for num in string.split()]
print(palindrome_numbers(numbers))