import sys

def rotate(tile):
    return list(''.join(x[::-1]) for x in zip(*tile))

def flip(tile):
    return list(reversed(tile.copy()))

def build_tile_transformations(tile):
    tile90 = rotate(tile)
    tile180 = rotate(tile90)
    tile270 = rotate(tile180)
    return [tile, tile90, tile180, tile270, flip(tile), flip(tile90), flip(tile180), flip(tile270)]

def get_monster_indexes():
    monster_pattern = [
        '                  # ',
        '#    ##    ##    ###',
        ' #  #  #  #  #  #   '
    ]
    return [(r, c) for r in range(len(monster_pattern)) for c in range(len(monster_pattern[r])) if monster_pattern[r][c] == '#']

def assemble_tiles(tile_transformations):
    n = int(len(tile_transformations)**0.5)
    assembled = [[(0, 0)] * n for _ in range(n)]
    remaining = set(tile_transformations.keys())

    def _assemble_tiles(rowcolumn):
        if rowcolumn == n * n:
            return True
        r, c = rowcolumn // n, rowcolumn % n
        for tileid in list(remaining):
            for i, transformation in enumerate(tile_transformations[tileid]):
                up_ok = left_ok = True
                if r > 0:
                    up_tileid, up_transformation = assembled[r - 1][c]
                    up_tile = tile_transformations[up_tileid][up_transformation]
                    up_ok = all(transformation[0][i] == up_tile[9][i] for i in range(10))
                if c > 0:
                    left_tileid, left_transformation = assembled[r][c - 1]
                    left_tile = tile_transformations[left_tileid][left_transformation]
                    left_ok = all(transformation[i][0] == left_tile[i][9] for i in range(10))
                if up_ok and left_ok:
                    assembled[r][c] = (tileid, i)
                    remaining.remove(tileid)
                    if _assemble_tiles(rowcolumn + 1):
                        return True
                    remaining.add(tileid)
        return False
    _assemble_tiles(0)
    
    return assembled

def part1(tile_matrix):
    return tile_matrix[0][0][0] * tile_matrix[0][-1][0] * tile_matrix[-1][0][0] * tile_matrix[-1][-1][0]

def part2(tile_matrix, tile_transformations):
    n = int(len(tile_transformations)**0.5)
    image = [['.'] * (n * 8) for _ in range(n * 8)]

    for r in range(n):
        for c in range(n):
            tileid, transformation = tile_matrix[r][c]
            tile = tile_transformations[tileid][transformation]
            for i in range(1, 9):
                for j in range(1, 9):
                    image[8 * r + i - 1][8 * c + j - 1] = tile[i][j]

    for image in build_tile_transformations(image):
        monster = 0
        for r in range(len(image) - 3):
            for c in range(len(image) - 20):
                if all(image[r + dr][c + dc] == '#' for dr, dc in get_monster_indexes()):
                    monster += 1
        if monster > 0:
            total = sum(row.count('#') for row in image)
            return total - monster * len(get_monster_indexes())

assert len(sys.argv) == 2
lines = open(sys.argv[1]).read().splitlines() + ['']

tiles = {}
tileid, matrix = 0, []
for line in lines:
    if not line:
        tiles[tileid] = matrix
        tileid, matrix = 0, []
    elif line.startswith('Tile'):
        tileid = int(line.replace(':', '').split()[1])
    else:
        matrix.append(line)

tile_transformations = {tileid: build_tile_transformations(tile) for tileid, tile in tiles.items()}
tile_matrix = assemble_tiles(tile_transformations)

print(f'Part 1: {part1(tile_matrix)}, Part 2: {part2(tile_matrix, tile_transformations)}')