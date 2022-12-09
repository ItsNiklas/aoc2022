#!/usr/bin/env python3

from utils import advent

advent.setup(2022, 9)
fd = advent.get_input()

visited = set()
visited2 = set()
pos: list[tuple[int, int]] = [(0, 0)] * 10


def pull(idx_head, idx_tail):
    (xhead, yhead), (xtail, ytail) = pos[idx_head], pos[idx_tail]
    xdiff, ydiff = abs(xhead - xtail), abs(yhead - ytail)

    if xdiff < 2 and ydiff < 2: return  # No pull, too close.
    if xdiff == 2:
        xtail = (xtail + xhead) // 2  # Adjust x-axis if too far
        if ydiff == 1: ytail = yhead  # Force diagonal movement
    if ydiff == 2:
        ytail = (ytail + yhead) // 2  # Adjust y-axis if too far
        if xdiff == 1: xtail = xhead  # Force diagonal movement

    pos[idx_head], pos[idx_tail] = (xhead, yhead), (xtail, ytail)  # Write result


for line in fd:
    direction, steps = line.split()
    for _ in range(int(steps)):
        match direction:  # Move the head
            case 'U':
                pos[0] = (pos[0][0], pos[0][1] + 1)
            case 'D':
                pos[0] = (pos[0][0], pos[0][1] - 1)
            case 'R':
                pos[0] = (pos[0][0] + 1, pos[0][1])
            case 'L':
                pos[0] = (pos[0][0] - 1, pos[0][1])

        for i in range(9): pull(i, i + 1)  # Pull all knots following the head

        visited.add(pos[1])
        visited2.add(pos[-1])

advent.print_answer(1, len(visited))
advent.print_answer(2, len(visited2))
