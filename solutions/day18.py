#!/usr/bin/env python3
import functools
import sys
from operator import itemgetter

from utils import advent

sys.setrecursionlimit(1500)  # 1.5x default

advent.setup(2022, 18)
fd = advent.get_input()

cubes = set(tuple(map(int, line.strip().split(","))) for line in fd)
deltas = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

x_range = (min(cubes, key=itemgetter(0))[0], max(cubes, key=itemgetter(0))[0])
y_range = (min(cubes, key=itemgetter(1))[1], max(cubes, key=itemgetter(1))[1])
z_range = (min(cubes, key=itemgetter(2))[2], max(cubes, key=itemgetter(2))[2])

checking = set()


@functools.cache
def airpocket(a) -> bool:
    ax, ay, az = a

    global checking
    checking.add(a)

    if not x_range[0] <= ax <= x_range[1]:
        return False
    if not y_range[0] <= ay <= y_range[1]:
        return False
    if not z_range[0] <= az <= z_range[1]:
        return False

    # Recursive DFS/Floodfill for the air pocket.
    for dx, dy, dz in deltas:
        n = (ax + dx, ay + dy, az + dz)
        if n not in cubes and n not in checking and not airpocket(n):
            return False

    return True


ans1 = 0
ans2 = 0

for cx, cy, cz in cubes:
    for dx, dy, dz in deltas:
        n = (cx + dx, cy + dy, cz + dz)
        if n not in cubes:
            ans1 += 1
            if not airpocket(n):
                checking.clear()
                ans2 += 1

advent.print_answer(1, ans1)
advent.print_answer(2, ans2)
