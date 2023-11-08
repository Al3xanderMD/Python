def set_operations(*sets):
    result = {}

    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            set1 = sets[i]
            set2 = sets[j]

            # Calculez rezultatele diferitelor operații de set
            union_result = set1 | set2
            intersection_result = set1 & set2
            difference_1_2 = set1 - set2
            difference_2_1 = set2 - set1

            # Creez chei pentru dicționar
            key_union = f"{set1} | {set2}"
            key_intersection = f"{set1} & {set2}"
            key_diff_1_2 = f"{set1} - {set2}"
            key_diff_2_1 = f"{set2} - {set1}"

            # Adaug rezultate în dicționar
            result[key_union] = union_result
            result[key_intersection] = intersection_result
            result[key_diff_1_2] = difference_1_2
            result[key_diff_2_1] = difference_2_1

    return result

set1 = {1, 2}
set2 = {2, 3}
set3 = {3, 4}

result = set_operations(set1, set2, set3)
for key, value in result.items():
    print(f"{key}: {value}")
