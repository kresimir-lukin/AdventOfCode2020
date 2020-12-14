import sys

def part1(instructions):
    set0mask, set1mask, memory = 0, 0, {}
    for instruction, value in instructions:
        if instruction == 'mask':
            set0mask, set1mask = int(value.replace('X', '1'), 2), int(value.replace('X', '0'), 2)
        else:
            address, value = int(instruction), int(value)
            memory[address] = value & set0mask | set1mask
    return sum(memory.values())

def part2(insts):
    mask, memory = '', {}
    for instruction, value in instructions:
        if instruction == 'mask':
            mask = value
        else:
            address = bin(int(instruction))[2:].zfill(36)
            address = [bit_mask if bit_mask in '1X' else bit_address for bit_address, bit_mask in zip(address, mask)]
            xs = [i for i, bit in enumerate(address) if bit == 'X']
            for permutation in range(1 << len(xs)):
                for i, bit in enumerate(bin(permutation)[2:].zfill(len(xs))):
                    address[xs[i]] = bit
                memory[''.join(address)] = int(value)
    return sum(memory.values())

assert len(sys.argv) == 2
lines = open(sys.argv[1]).read().splitlines()
instructions = [line.replace('mem', '').replace('[', '').replace(']', '').split(' = ') for line in lines]

print(f'Part 1: {part1(instructions)}, Part 2: {part2(instructions)}')