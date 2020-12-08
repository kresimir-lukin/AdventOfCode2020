import sys

def execute(program):
    pc_visited = [False] * len(program)
    accumulator = pc = 0
    while pc < len(program) and not pc_visited[pc]:
        pc_visited[pc] = True
        instruction, argument = program[pc]
        if instruction == 'acc':
            accumulator += argument
        elif instruction == 'jmp':
            pc += argument - 1
        pc += 1
    return accumulator, pc == len(program)

def part1(program):
    return execute(program)[0]

def part2(program):
    for pc, (instruction, _) in enumerate(program):
        if instruction in ('nop', 'jmp'):
            program[pc][0] = 'jmp' if instruction == 'nop' else 'nop'
            accumulator, done = execute(program)
            program[pc][0] = instruction
            if done:
                return accumulator

assert len(sys.argv) == 2
program = [[instruction.split()[0], int(instruction.split()[1])] for instruction in open(sys.argv[1]).read().splitlines()]

print(f'Part 1: {part1(program)}, Part 2: {part2(program)}')