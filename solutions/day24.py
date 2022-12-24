#!/usr/bin/env python3

from utils import advent
from itertools import count

advent.setup(2022, 24)
fd = advent.get_input()

blizz: set[tuple[complex, complex]] = set()  # Location & Direction
start: complex = None
end: complex = None
N, M = 0, 0

dirs = {"^": -1, "v": 1, ">": 1j, "<": -1j}

for i, line in enumerate(fd):
    for j, char in enumerate(line.strip()):
        if i == 0 and char == ".":
            start = complex(i, j)
        elif i > 0 and char == ".":
            end = complex(i, j)
        elif char != "#" and char != ".":
            blizz.add((complex(i, j), dirs[char]))
    N = len(line) - 2
    M = i


def inbounds(c: complex) -> bool:
    if c == start or c == end:
        return True
    if c.imag < 1 or c.imag > N - 1:
        return False
    if c.real < 1 or c.real > M - 1:
        return False
    return True


locations = {start}
goals = [end, start, end]

for i in count():
    blizz_new = set()
    for loc, direction in blizz:
        new = loc + direction
        if not inbounds(new):
            # Out ouf bounds, walk backwards to 'wrap around'
            while inbounds(new - direction):
                new -= direction
        blizz_new.add((new, direction))
    blizz = blizz_new

    locations = {node + d for d in [1, -1, 1j, -1j, 0] for node in locations}
    locations -= {node for node, _ in blizz}
    locations = set(filter(inbounds, locations))

    if goals[0] in locations:
        if len(goals) != 2:
            advent.print_answer(2 - len(goals) // 2, i + 1)
        locations = {goals.pop(0)}
        if not goals:
            break
