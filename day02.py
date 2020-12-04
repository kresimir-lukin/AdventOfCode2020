import sys, re

assert len(sys.argv) == 2
lines = open(sys.argv[1]).read().splitlines()
part1 = part2 = 0

for line in lines:
    num1, num2, letter, password = re.search('^([0-9]+)-([0-9]+) (.): (.+)$', line).groups()
    num1, num2 = int(num1), int(num2)
    part1 += num1 <= password.count(letter) <= num2
    part2 += (password[num1-1] == letter) ^ (password[num2-1] == letter)

print(f'Part 1: {part1}, Part 2: {part2}')