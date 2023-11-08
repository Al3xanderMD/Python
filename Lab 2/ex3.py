def list_ops(a, b):
    intersection = list(set(a) & set(b))
    union = list(set(a) | set(b))
    a_minus_b = list(set(a) - set(b))
    b_minus_a = list(set(b) - set(a))
    return (intersection, union, a_minus_b, b_minus_a)

string1 = input("Enter a list of numbers separated by spaces: ")
a = [int(num) for num in string1.split()]
string2 = input("Enter another list of numbers separated by spaces: ")
b = [int(num) for num in string2.split()]
print(list_ops(a, b))
