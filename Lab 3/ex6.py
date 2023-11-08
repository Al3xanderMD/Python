def count_unique_and_duplicates(lst):
    # Creez un set pentru a stoca elemente unice și o listă pentru a stoca duplicatele
    unique_elements = set()
    duplicate_elements = []

    for item in lst:
        if item in unique_elements:
            duplicate_elements.append(item)
        else:
            unique_elements.add(item)

    return len(unique_elements), len(duplicate_elements)

my_list = [1, 2, 2, 3, 4, 4, 5]
result = count_unique_and_duplicates(my_list)
print(result)  # (5, 2) 
