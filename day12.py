import sys

directions = {
    'N': (0, 1),
    'S': (0, -1),
    'E': (1, 0),
    'W': (-1, 0)
}

def part1(instructions):
    angle_direction = { 0: 'E', 90: 'N', 180: 'W', 270: 'S' }
    ferryx = ferryy = angle = 0
    for action, value in instructions:
        if action in 'LR':
            value = value if action == 'L' else 360 - value
            angle = (angle + value) % 360
        else:
            dx, dy = directions[angle_direction[angle]] if action == 'F' else directions[action]
            ferryx += value * dx
            ferryy += value * dy
    return abs(ferryx) + abs(ferryy)

def part2(instructions):
    waypointx, waypointy = 1, 10
    ferryx = ferryy = 0
    for action, value in instructions:
        if action in 'LR':
            value = value if action == 'L' else 360 - value
            if value == 180:
                waypointx, waypointy = -waypointx, -waypointy
            elif value == 90:
                waypointx, waypointy = waypointy, -waypointx
            else:
                waypointx, waypointy = -waypointy, waypointx
        elif action == 'F':
            ferryx += value * waypointx
            ferryy += value * waypointy
        else:
            waypointx += value * directions[action][1]
            waypointy += value * directions[action][0]
    return abs(ferryx) + abs(ferryy)

assert len(sys.argv) == 2
instructions = [(instruction[0], int(instruction[1:])) for instruction in open(sys.argv[1]).read().split()]

print(f'Part 1: {part1(instructions)}, Part 2: {part2(instructions)}')