def group_by_rhyme(words):
    rhyme_groups = {}
    
    for word in words:
        last_two_chars = word[-2:]
        if last_two_chars in rhyme_groups:
            rhyme_groups[last_two_chars].append(word)
        else:
            rhyme_groups[last_two_chars] = [word]

    grouped_words = list(rhyme_groups.values())
    return grouped_words

# Example usage
word_list = ['ana', 'banana', 'carte', 'arme', 'parte']

rhyme_groups = group_by_rhyme(word_list)
print(rhyme_groups)
