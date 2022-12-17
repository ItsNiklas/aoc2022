#!/usr/bin/env python3
import functools
import re

from utils import advent

advent.setup(2022, 16)
fd = advent.get_input()

pressures = dict()
adj = dict()

for line in fd:
    labels = re.findall(r"([A-Z]{2})", line)
    pressures |= {labels[0]: int(re.search(r"(\d+)", line).group())}
    adj |= {labels[0]: labels[1:]}


# DFS
@functools.cache
def search(valves: frozenset, loc: str, time: int):
    if time == 0:
        return 0

    res_open = 0
    # Open Valve
    if loc not in valves and pressures[loc] != 0:
        res_open = (time - 1) * pressures[loc] + search(
            valves | frozenset([loc]), loc, time - 1
        )

    # Move
    res_move = max(search(valves, neigh, time - 1) for neigh in adj[loc])

    return max(res_open, res_move)


advent.print_answer(1, search(frozenset(), "AA", 30))
