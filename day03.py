import sys, functools, operator

def count_trees(forest, slope_r, slope_c):
    rows, cols = len(forest), len(forest[0])
    row = col = 0
    trees = 0
    while row < rows:
        trees += forest[row][col] == '#'
        row += slope_r
        col = (col + slope_c) % cols
    return trees

assert len(sys.argv) == 2
forest = open(sys.argv[1]).read().splitlines()

part1 = count_trees(forest, 1, 3)
part2 = [count_trees(forest, sr, sc) for sr, sc in [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]]

print(f'Part 1: {part1}, Part 2: {functools.reduce(operator.mul, part2, 1)}')