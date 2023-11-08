def count_bits(num: int) -> int:
    count = 0
    while num:
        count += num & 1
        num >>= 1
    return count

num = int(input("Enter a number: "))
print(f"{num} has {count_bits(num)} bits")