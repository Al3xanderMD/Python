def find_obstructed_seats(matrix):
    obstructed_seats = []
    rows = len(matrix)
    cols = len(matrix[0])

    # Create a list to track the tallest spectators for each column
    tallest_in_column = [-1] * cols

    for row in range(rows):
        for col in range(cols):
            current_height = matrix[row][col]

            # Check if there's a taller spectator in the same column
            if current_height > tallest_in_column[col]:
                tallest_in_column[col] = current_height

            else:
                # There is a taller spectator in the same column; mark the seat as obstructed
                obstructed_seats.append((row, col))

    return obstructed_seats

# Example usage
stadium_matrix = [
    [1, 2, 3, 2, 1, 1],
    [2, 4, 4, 3, 7, 2],
    [5, 5, 2, 5, 6, 4],
    [6, 6, 7, 6, 7, 5]
]

obstructed_seats = find_obstructed_seats(stadium_matrix)
print(obstructed_seats)  # Output: [(2, 2), (3, 4), (2, 4)]
