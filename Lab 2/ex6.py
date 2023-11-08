def find_items(*lists, x):
    items = []
    for lst in lists:
        for item in lst:
            if sum(1 for l in lists if item in l) == x:
                if item not in items:
                    items.append(item)
    return items

list1 = [1, 2, 3]
list2 = [2, 3, 4]
list3 = [4, 5, 6]
list4 = [4, 1, "test"]

num = int(input("Enter X number: "))

result = find_items(list1, list2, list3, list4, x=num)
print(result)
