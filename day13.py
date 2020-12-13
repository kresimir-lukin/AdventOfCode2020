import sys
from functools import reduce

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

def part1(timestamp, buses):
    wait = busid = float('inf')
    for bus in buses:
        if bus > 0:
            next_stop = (timestamp // bus + 1) * bus
            bus_wait = next_stop - timestamp
            if bus_wait < wait:
                wait, busid = bus_wait, bus
    return wait * busid

def part2(buses):
    dividers = []
    remainders = []
    for i, bus in enumerate(buses):
        if bus > 0:
            dividers.append(bus)
            remainders.append(bus - i)
    return chinese_remainder(dividers, remainders)

assert len(sys.argv) == 2
timestamp, buses = open(sys.argv[1]).read().splitlines()
timestamp, buses = int(timestamp), [0 if bus == 'x' else int(bus) for bus in buses.split(',')]

print(f'Part 1: {part1(timestamp, buses)}, Part 2: {part2(buses)}')