def loop(mapping):
    visited = set()
    result = []
    current_key = 'start'

    while current_key in mapping and current_key not in visited:
        visited.add(current_key)
        result.append(mapping[current_key])
        current_key = mapping[current_key]

    # Dacă întâlnim o buclă și cheia curentă este egală cu 
    # ultimul element din rezultat, elimin pentru a evita duplicarea.
    if current_key in visited and current_key == result[-1]:
        result.pop()

    return result

mapping = {'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}
result = loop(mapping)
print(result)  # ['a', '6', 'z', '2']
