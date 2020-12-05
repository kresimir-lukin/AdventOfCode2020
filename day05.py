import sys

assert len(sys.argv) == 2
boarding_passes = open(sys.argv[1]).read().split()

seats = set()
for boarding_pass in boarding_passes:
    row = int(boarding_pass[:7].replace('F', '0').replace('B', '1'), 2)
    col = int(boarding_pass[-3:].replace('L', '0').replace('R', '1'), 2)
    seats.add(row * 8 + col)

part1 = max(seats)
part2 = next(seat for seat in range(min(seats)+1, max(seats)) if seat not in seats)

print(f'Part 1: {part1}, Part 2: {part2}')