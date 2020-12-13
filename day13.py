import sys, helpers

def part1(timestamp, buses):
    wait = busid = float('inf')
    for _, bus in buses:
        next_stop = (timestamp // bus + 1) * bus
        bus_wait = next_stop - timestamp
        if bus_wait < wait:
            wait, busid = bus_wait, bus
    return wait * busid

def part2(buses):
    dividers = [bus for _, bus in buses]
    remainders = [bus - i for i, bus in buses]
    return helpers.chinese_remainder(dividers, remainders)

assert len(sys.argv) == 2
timestamp, buses = open(sys.argv[1]).read().splitlines()
timestamp, buses = int(timestamp), [(i, int(bus)) for i, bus in enumerate(buses.split(',')) if bus != 'x']

print(f'Part 1: {part1(timestamp, buses)}, Part 2: {part2(buses)}')