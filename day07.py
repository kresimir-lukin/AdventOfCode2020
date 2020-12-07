import sys, re, collections

def part1(inverse_rules):
    queue, reachable = collections.deque(['shiny gold']), set()
    while queue:
        color = queue.pop()
        for c in inverse_rules.get(color, []):
            if c not in reachable:
                reachable.add(c)
                queue.appendleft(c)
    return len(reachable)

def part2(rules, color = 'shiny gold'):
    return sum(number + number * part2(rules, c) for c, number in rules[color].items())

assert len(sys.argv) == 2
input_rules = open(sys.argv[1]).read().splitlines()

rules, inverse_rules = {}, {}
for input_rule in input_rules:
    color, rule_colors = input_rule.split(' bags contain ')
    rules[color] = {color: int(number) for number, color in re.findall('(\d+) (\w+ \w+)', rule_colors)}
    for c in rules[color]:
        inverse_rules[c] = inverse_rules.get(c, []) + [color]

print(f'Part 1: {part1(inverse_rules)}, Part 2: {part2(rules)}')