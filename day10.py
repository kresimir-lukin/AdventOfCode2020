import sys

def part1(joltages):
    jump1 = jump3 = 0
    for previous, current in zip(joltages, joltages[1:]):
        jump1 += (current - previous) == 1
        jump3 += (current - previous) == 3
    return jump1 * jump3

def part2(joltages):
    ways = [1] + [0] * (len(joltages) - 1)
    for i in range(1, len(joltages)):
        ways[i] += sum(ways[i-j] for j in range(1, 4) if i-j >= 0 and joltages[i] - joltages[i-j] <= 3)
    return ways[-1]

assert len(sys.argv) == 2
joltages = list(map(int, open(sys.argv[1]).read().split()))
joltages = [0] + sorted(joltages) + [max(joltages) + 3]

print(f'Part 1: {part1(joltages)}, Part 2: {part2(joltages)}')