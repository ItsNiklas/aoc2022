#!/usr/bin/env python3

import re

from utils import advent

advent.setup(2022, 22)
fd = advent.get_input()

board: dict[complex, str] = dict()

for i, line in enumerate(fd):
    if line == "\n":
        break

    for j, char in enumerate(line):
        if char == " " or char == "\n":
            continue
        board |= {complex(i, j): char}

notes = re.findall(r"(\d+|\D+)", fd.read().strip())

location: complex = (
        min(c.imag for c, obj in board.items() if c.real == 0 and obj == ".") * 1j
)
direction: complex = 1j

for n in notes:
    if n == "L":
        direction *= 1j
    elif n == "R":
        direction *= -1j
    else:
        for _ in range(int(n)):
            new = location + direction
            if new not in board:
                # Out ouf bounds, walk backwards to 'wrap around'
                while new - direction in board:
                    new -= direction
            if board[new] == "#":
                break
            location = new

mapping = {1j: 0, 1: 1, -1j: 2, -1: 3}
advent.print_answer(
    1, int(1000 * (location.real + 1) + 4 * (location.imag + 1) + mapping[direction])
)
