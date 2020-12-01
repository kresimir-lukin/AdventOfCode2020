import sys

def two_pointer_sum(numbers, target_sum, left):
    right = len(numbers) - 1
    while left < right:
        candidates = numbers[left], numbers[right]
        if sum(candidates) == target_sum:
            return candidates
        if sum(candidates) > target_sum:
            right -= 1
        else:
            left += 1

def part1(numbers):
    candidates = two_pointer_sum(numbers, 2020, 0)
    return candidates[0] * candidates[1]

def part2(numbers):
    for i, number in enumerate(numbers):
        candidates = two_pointer_sum(numbers, 2020 - number, i + 1)
        if candidates:
            return number * candidates[0] * candidates[1]

assert len(sys.argv) == 2
numbers = list(map(int, open(sys.argv[1]).read().split()))
numbers.sort()

print(f'Part 1: {part1(numbers)}, Part 2: {part2(numbers)}')