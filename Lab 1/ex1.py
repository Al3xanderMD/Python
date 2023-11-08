def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def gcd_multiple(numbers):
    result = numbers[0]
    for i in range(1, len(numbers)):
        result = gcd(result, numbers[i])
    return result

total = 0
numbers = []
count = int(input("How many numbers do you want to enter? "))
for i in range(count):
    num = int(input("Enter number {}: ".format(i+1)))
    numbers.append(num)

print("The greatest common divisor is:", gcd_multiple(numbers))
