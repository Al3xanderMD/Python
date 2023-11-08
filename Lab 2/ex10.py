def combine_lists(*input_lists):
    max_length = max(len(lst) for lst in input_lists)

    result = []
    
    for i in range(max_length):
        combined_tuple = tuple(lst[i] if i < len(lst) else None for lst in input_lists)
        result.append(combined_tuple)

    return result

# Example usage
list1 = [1, 2, 3]
list2 = [5, 6, 7]
list3 = ["a", "b", "c"]

combined_lists = combine_lists(list1, list2, list3)
print(combined_lists)
