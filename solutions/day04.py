#!/usr/bin/env python3

from utils import advent, helpers

advent.setup(2022, 4)
fd = advent.get_input()

input = list(zip(*[iter(helpers.get_ints(fd, True, r"\d+"))] * 4))

sum1 = sum(x >= a and y <= b or a >= x and b <= y for a, b, x, y in input)
sum2 = sum(b >= x and a <= y for a, b, x, y in input)

advent.print_answer(1, sum1)
advent.print_answer(2, sum2)