def replace_below_main_diagonal_with_zeros(matrix):
    if not matrix:
        return []

    num_rows, num_cols = len(matrix), len(matrix[0])

    result_matrix = [[0] * num_cols for _ in range(num_rows)]

    for i in range(num_rows):
        for j in range(num_cols):
            if i > j:
                matrix[i][j] = 0
                #result_matrix[i][j] = matrix[i][j]

    return matrix

input_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = replace_below_main_diagonal_with_zeros(input_matrix)
for row in result:
    print(row)
