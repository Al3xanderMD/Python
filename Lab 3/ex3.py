def compare_dicts(dict1, dict2):
    # Verific daca ambele obiecte sunt dictionare
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        return False

    # Verific daca cheile din ambele dictionare sunt egale
    if set(dict1.keys()) != set(dict2.keys()):
        return False

    # Recursiv compar valorile pentru fiecare cheie
    for key in dict1:
        value1 = dict1[key]
        value2 = dict2[key]

        # Daca sunt dictionare, compar recursiv
        if isinstance(value1, dict) and isinstance(value2, dict):
            if not compare_dicts(value1, value2):
                return False
        # Dacă valorile sunt liste sau seturi, convertesc în liste sortate și compar
        elif isinstance(value1, (list, set)) and isinstance(value2, (list, set)):
            if sorted(value1) != sorted(value2):
                return False
        # În caz contrar, compar direct valorile
        elif value1 != value2:
            return False

    # Dacă toate verificările trec, dicționarele sunt echivalente
    return True

dict1 = {'a': 1, 'b': 2, 'c': [1, 2, 3], 'd' : {'a': 1, 'b': 2}}
dict2 = {'c': [3, 2, 1], 'b': 2, 'a': 1 , 'd' : {'a': 1, 'b': 2}}
result = compare_dicts(dict1, dict2)
print(result)  # True
