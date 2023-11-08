def compose(notes, moves, start):
    song = []
    song.append(notes[start])
    current = start
    for move in moves:
        current = (current + move) % len(notes)
        song.append(notes[current])
    return song

notes = ["do", "re", "mi", "fa", "sol"]
moves = [1, -3, 4, 2]
start = 2
print(compose(notes, moves, start))