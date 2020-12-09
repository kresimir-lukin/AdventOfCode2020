import sys

def part1(numbers, preamble = 25):
    candidates = numbers[:preamble]
    for i in range(preamble, len(numbers)):
        if not any(candidates[n1] + candidates[n2] == numbers[i] for n1 in range(preamble - 1) for n2 in range(n1 + 1, preamble)):
            return numbers[i]
        candidates = candidates[1:] + [numbers[i]]

def part2(numbers, invalid_number):
    for n1 in range(len(numbers) - 1):
        current_sum = numbers[n1]
        for n2 in range(n1 + 1, len(numbers)):
            current_sum += numbers[n2]
            if current_sum == invalid_number:
                return min(numbers[n1:n2+1]) + max(numbers[n1:n2+1])

assert len(sys.argv) == 2
numbers = list(map(int, open(sys.argv[1]).read().split()))

invalid_number = part1(numbers)
print(f'Part 1: {invalid_number}, Part 2: {part2(numbers, invalid_number)}')