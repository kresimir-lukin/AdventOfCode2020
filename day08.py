import sys

def execute(program):
    pc_visited = set()
    accumulator = pc = 0
    while pc < len(program) and pc not in pc_visited:
        pc_visited.add(pc)
        instruction, argument = program[pc]
        if instruction == 'acc':
            accumulator += argument
        elif instruction == 'jmp':
            pc += argument - 1
        pc += 1
    return accumulator, pc == len(program)

def execute_by_modification(pc, instruction):
    prev_instruction, program[pc][0] = program[pc][0], instruction
    accumulator, done = execute(program)
    program[pc][0] = prev_instruction
    return accumulator if done else False

def part1(program):
    return execute(program)[0]

def part2(program):
    nops = [pc for pc, (instruction, _) in enumerate(program) if instruction == 'nop']
    jmps = [pc for pc, (instruction, _) in enumerate(program) if instruction == 'jmp']
    accumulator = False
    for jmp in jmps:
        accumulator = accumulator or execute_by_modification(jmp, 'nop')
    for nop in nops:
        accumulator = accumulator or execute_by_modification(nop, 'jmp')
    return accumulator

assert len(sys.argv) == 2
program = [[instruction.split()[0], int(instruction.split()[1])] for instruction in open(sys.argv[1]).read().splitlines()]

print(f'Part 1: {part1(program)}, Part 2: {part2(program)}')