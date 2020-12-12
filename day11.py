import sys

neibhour_offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def round(seats, calculate_seat):
    rows, cols = len(seats), len(seats[0])
    seats_new = [row[:] for row in seats]
    stabilized = True
    for r in range(rows):
        for c in range(cols):
            seats_new[r][c] = calculate_seat(seats, r, c)
            stabilized = stabilized and seats[r][c] == seats_new[r][c]
    return seats_new, stabilized

def run_till_stabilized(seats, calculate_seat):
    seats, stabilized = round(seats, calculate_seat)
    while not stabilized:
        seats, stabilized = round(seats, calculate_seat)
    return sum(row.count('#') for row in seats)

def part1_calculate_seat(seats, r, c):
    rows, cols = len(seats), len(seats[0])
    occupied = 0
    for dr, dc in neibhour_offsets:
        if 0 <= r + dr < rows and 0 <= c + dc < cols:
            occupied += seats[r + dr][c + dc] == '#'
    if seats[r][c] == 'L' and occupied == 0:
        return '#'
    if seats[r][c] == '#' and occupied >= 4:
        return 'L'
    return seats[r][c]

def part2_calculate_seat(seats, r, c):
    rows, cols = len(seats), len(seats[0])
    occupied = 0
    for dr, dc in neibhour_offsets:
        cr, cc = r + dr, c + dc
        while 0 <= cr < rows and 0 <= cc < cols and seats[cr][cc] == '.':
            cr += dr
            cc += dc
        occupied += 0 <= cr < rows and 0 <= cc < cols and seats[cr][cc] == '#'
    if seats[r][c] == 'L' and occupied == 0:
        return '#'
    if seats[r][c] == '#' and occupied >= 5:
        return 'L'
    return seats[r][c]

assert len(sys.argv) == 2
seats = [list(row) for row in open(sys.argv[1]).read().splitlines()]

part1 = run_till_stabilized(seats, part1_calculate_seat)
part2 = run_till_stabilized(seats, part2_calculate_seat)

print(f'Part 1: {part1}, Part 2: {part2}')