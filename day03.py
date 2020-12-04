import sys, functools, operator

def count_trees(forest, slopes):
    rows, cols = len(forest), len(forest[0])
    slope_trees = []
    for sr, sc in slopes:
        trees = sum(forest[i * sr][(i * sc) % cols] == '#' for i in range(rows // sr))
        slope_trees.append(trees)
    return functools.reduce(operator.mul, slope_trees, 1)

assert len(sys.argv) == 2
forest = open(sys.argv[1]).read().splitlines()

part1 = count_trees(forest, [(1, 3)])
part2 = count_trees(forest, [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)])

print(f'Part 1: {part1}, Part 2: {part2}')