#!/usr/bin/env python3

from utils import advent
from heapq import nlargest

advent.setup(2022, 1)
fd = advent.get_input()

elves = [sum(map(int, x.split())) for x in fd.read().split('\n\n')]

advent.print_answer(1, max(elves))
advent.print_answer(2, sum(nlargest(3, elves)))
