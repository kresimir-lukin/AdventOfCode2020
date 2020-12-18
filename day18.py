import sys

def evaluate_without_precedence(expression):
    number, nested = 0, []
    for ch in '(' + expression + ')':
        if ch.isdigit():
            number = 10 * number + int(ch)
        elif ch == '(':
            nested.append([0, '+'])
        elif ch in '+*)':
            result, operator = nested[-1]
            if operator == '+':
                result += number
            elif operator == '*':
                result *= number
            nested[-1] = [result, ch]
            number = nested.pop()[0] if ch == ')' else 0
    return number

def evaluate_with_precedence(expression):
    number, nested = 0, []
    for ch in '(' + expression + ')':
        if ch.isdigit():
            number = 10 * number + int(ch)
        elif ch == '(':
            nested.append([1, 0, '+'])
        elif ch in '+*)':
            result, previous, operator = nested[-1]
            if operator == '+':
                previous += number
            elif operator == '*':
                result *= previous
                previous = number
            nested[-1] = [result, previous, ch]
            number = result * nested.pop()[1] if ch == ')' else 0
    return number

assert len(sys.argv) == 2
expressions = open(sys.argv[1]).read().splitlines()

part1 = sum(evaluate_without_precedence(expression) for expression in expressions)
part2 = sum(evaluate_with_precedence(expression) for expression in expressions)

print(f'Part 1: {part1}, Part 2: {part2}')