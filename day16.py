import sys, re, functools, operator

def parse_input():
    assert len(sys.argv) == 2
    lines = open(sys.argv[1]).read().splitlines()

    first_blank, second_blank = [i for i, line in enumerate(lines) if not line]
    field_lines = lines[:first_blank]
    your_ticket_lines = lines[first_blank + 1 : second_blank]
    nearby_tickets_lines = lines[second_blank + 1:]

    fields = [re.search('([^:]+): (\d+)-(\d+) or (\d+)-(\d+)', line).groups() for line in field_lines]
    fields = {name: (int(from1), int(to1), int(from2), int(to2)) for name, from1, to1, from2, to2 in fields}
    your_ticket = list(map(int, your_ticket_lines[1].split(',')))
    nearby_tickets = [list(map(int, nearby_tickets_lines[i].split(','))) for i in range(1, len(nearby_tickets_lines))]

    return fields, your_ticket, nearby_tickets

def check_valid(fields, nearby_tickets):
    valid_tickets, invalid_field_sum = [], 0
    for ticket in nearby_tickets:
        valid = True
        for value in ticket:
            if not any(from1 <= value <= to1 or from2 <= value <= to2 for from1, to1, from2, to2 in fields.values()):
                valid = False
                invalid_field_sum += value
        if valid:
            valid_tickets.append(ticket)
    return valid_tickets, invalid_field_sum

def part2(fields, your_ticket, valid_tickets):
    potential_fields = [set() for _ in range(len(your_ticket))]
    fields_order = ['' for _ in range(len(fields))]

    for i in range(len(your_ticket)):
        for field, (from1, to1, from2, to2) in fields.items():
            if all(from1 <= ticket[i] <= to1 or from2 <= ticket[i] <= to2 for ticket in valid_tickets):
                potential_fields[i].add(field)

    while any(not field for field in fields_order):
        pos = next(pos for pos, potential_vaules in enumerate(potential_fields) if len(potential_vaules) == 1)
        value = potential_fields[pos].pop()
        for potential_vaules in potential_fields:
            if value in potential_vaules:
                potential_vaules.remove(value)
        fields_order[pos] = value

    return functools.reduce(operator.mul, [your_ticket[pos] for pos, field in enumerate(fields_order) if field.startswith('departure')], 1)

fields, your_ticket, nearby_tickets = parse_input()
valid_tickets, part1 = check_valid(fields, nearby_tickets)

print(f'Part 1: {part1}, Part 2: {part2(fields, your_ticket, valid_tickets)}')