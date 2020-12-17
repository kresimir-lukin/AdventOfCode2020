import sys

def count_active_neighbours(active, x, y, z, w, dw_min, dw_max):
    active_neighbours = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            for dz in range(-1, 2):
                for dw in range(dw_min, dw_max + 1):
                    if dx == dy == dz == dw == 0:
                        continue
                    active_neighbours += (x + dx, y + dy, z + dz, w + dw) in active
    return active_neighbours

def run_cycles(active, dw_min, dw_max):
    for _ in range(6):
        cycle_active = set()
        minx = miny = minz = minw = float('inf')
        maxx = maxy = maxz = maxw = float('-inf')
        for x, y, z, w in active:
            minx, maxx = min(minx, x), max(maxx, x)
            miny, maxy = min(miny, y), max(maxy, y)
            minz, maxz = min(minz, z), max(maxz, z)
            minw, maxw = min(minw, w), max(maxw, w)
        for x in range(minx - 1, maxx + 2):
            for y in range(miny - 1, maxy + 2):
                for z in range(minz - 1, maxz + 2):
                    for w in range(minw - 1, maxw + 2):
                        active_neighbours = count_active_neighbours(active, x, y, z, w, dw_min, dw_max)
                        if (x, y, z, w) in active and active_neighbours in (2, 3):
                            cycle_active.add((x, y, z, w))
                        if (x, y, z, w) not in active and active_neighbours == 3:
                            cycle_active.add((x, y, z, w))
        active = cycle_active
    return len(active)

assert len(sys.argv) == 2
lines = open(sys.argv[1]).read().splitlines()
active = {(x, y, 0, 0) for y, line in enumerate(lines) for x, state in enumerate(line) if state == '#'}

part1 = run_cycles(active, 0, 0)
part2 = run_cycles(active, -1, 1)

print(f'Part 1: {part1}, Part 2: {part2}')