def find_primes(numbers):
    primes = []
    for num in numbers:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    return primes

string = input("Enter a list of numbers separated by spaces: ")
numbers = [int(num) for num in string.split()]
print(find_primes(numbers))