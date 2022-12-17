#!/usr/bin/env python3

import itertools

import numpy as np

from utils import advent

advent.setup(2022, 17)
fd = advent.get_input()

jet = itertools.cycle(fd.read().strip())
rocks = itertools.cycle([[(0, 0), (1, 0), (2, 0), (3, 0)],  # Line
                         [(0, 1), (1, 1), (2, 1), (1, 2), (1, 0)],  # Plus
                         [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],  # Rev L
                         [(0, 0), (0, 1), (0, 2), (0, 3)],  # Column
                         [(0, 0), (0, 1), (1, 0), (1, 1)]])  # Cube

chamber = np.zeros((7, 10000), dtype=np.ubyte)
chamber.T[0] = np.ones(7)  # Floor

for _ in range(2022):
    rock = next(rocks).copy()
    start = (2, chamber.T.any(1).argmin() + 3)  # Start Anchor of rock

    # print(*reversed(chamber.T[0:start[1]]), '---------------', sep='\n')

    # Spawn rock at Start
    rock = list(map(lambda loc: (loc[0] + start[0], loc[1] + start[1]), rock))
    moving = True

    while moving:
        # being pushed by a jet of hot gas
        j_dx = 1 if next(jet) == '>' else -1
        for x, y in rock:
            if not 0 <= x + j_dx < 7:  # move into the walls?
                break  # We hit a wall
            if chamber[x + j_dx][y] == 1:  # moved into a stopped rock?
                break
        else:
            rock = list(map(lambda loc: (loc[0] + j_dx, loc[1]), rock))  # We didn't hit anything

        # falling one unit down
        for x, y in rock:
            if chamber[x][y - 1] == 1:  # moved into a stopped rock / floor?
                moving = False
                break
        else:
            rock = list(map(lambda loc: (loc[0], loc[1] - 1), rock))  # We didn't hit anything

        if not moving:
            for x, y in rock:  # Fix rock:
                chamber[x][y] = 1

advent.print_answer(1, chamber.T.any(1).argmin() - 1)
