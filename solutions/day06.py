#!/usr/bin/env python3

from utils import advent

advent.setup(2022, 6)
fd = advent.get_input()
input = fd.readline()

pt1 = False
for i in range(len(input)):
    if not pt1 and len(set(input[i:i + 4])) == len(input[i:i + 4]):
        advent.print_answer(1, i + 4)
        pt1 = True
    if len(set(input[i:i + 14])) == len(input[i:i + 14]):
        advent.print_answer(2, i + 14)
        break
