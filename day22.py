import sys

def multiply(player):
    score, multiplier = 0, 1
    while player:
        score += multiplier * player.pop()
        multiplier += 1
    return score

def part1(player1, player2):
    player1, player2 = player1[:], player2[:]
    while player1 and player2:
        player1_top, player2_top = player1.pop(0), player2.pop(0)
        player1 += [player1_top, player2_top] if player1_top > player2_top else []
        player2 += [player2_top, player1_top] if player2_top > player1_top else []
    return player1 if player1 else player2

def part2(player1, player2):
    states = set()
    while player1 and player2:
        state = (tuple(player1), tuple(player2))
        if state in states:
            return (1, player1)

        player1_top, player2_top = player1.pop(0), player2.pop(0)

        if player1_top <= len(player1) and player2_top <= len(player2):
            winner, _ = part2(player1[:player1_top], player2[:player2_top])
        else:                
            winner = 1 if player1_top > player2_top else 2

        player1 += [player1_top, player2_top] if winner == 1 else []
        player2 += [player2_top, player1_top] if winner == 2 else []
        states.add(state)

    return (1, player1) if player1 else (2, player2)

assert len(sys.argv) == 2
player1_line, player2_line = open(sys.argv[1]).read().replace('\r\n', '\n').replace('\n\n', '|').replace('\n', ' ').split('|')

player1 = list(map(int, player1_line.split(':')[1].split()))
player2 = list(map(int, player2_line.split(':')[1].split()))

winner1 = part1(player1, player2)
_, winner2 = part2(player1, player2)

print(f'Part 1: {multiply(winner1)}, Part 2: {multiply(winner2)}')