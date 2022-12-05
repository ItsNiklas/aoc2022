#!/usr/bin/env python3
import re
from collections import deque
from copy import deepcopy

from utils import advent

advent.setup(2022, 5)
fd = advent.get_input()

in1, in2 = map(lambda s: s.splitlines(), fd.read().rstrip().split("\n\n"))

number_stacks = (len(in1[-1])-3) // 4 + 1
stacks = [deque() for _ in range(number_stacks)]

for line in reversed(in1[:-1]):
    for i in range(number_stacks):
        c = line[4 * i + 1]
        if c != ' ': stacks[i].append(c)

stacks2 = deepcopy(stacks)

in2 = (map(int, *re.findall(r"(\d+) from (\d+) to (\d+)", l)) for l in in2)
for amt, fro, to in in2:
    crates = [stacks2[fro - 1].pop() for _ in range(amt)]
    crates.reverse()

    for i in range(amt):
        stacks[to - 1].append(stacks[fro - 1].pop())
        stacks2[to - 1].append(crates[i])

advent.print_answer(1, "".join(s.pop() for s in stacks))
advent.print_answer(2, "".join(s.pop() for s in stacks2))
