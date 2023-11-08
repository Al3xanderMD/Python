def validate_dict(rules, dictionary):
    # Creez un set pentru a stoca cheile care corespund regulilor
    valid_keys = set()

    # Repet regulile și verific dacă fiecare cheie din dicționar respectă regula
    for key, prefix, middle, suffix in rules:
        if key in dictionary:
            value = dictionary[key]
            if value.startswith(prefix) and middle in value[1:-1] and value.endswith(suffix):
                valid_keys.add(key)

    # Verific dacă toate cheile de potrivire a regulilor sunt prezente în dicționar
    return valid_keys == set(rules)

rules = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
dictionary = {"key1": "come inside, it's too cold out", "key3": "this is not valid"}

result = validate_dict(rules, dictionary)
print(result)  # False
