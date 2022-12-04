#!/usr/bin/env python3
import re

from utils import advent

advent.setup(2022, 4)
fd = advent.get_input()
pat = re.compile(r"(\d+)-(\d+),(\d+)-(\d+)\n")

input = [list(map(int, re.match(pat, l).groups())) for l in fd.readlines()]

sum1 = sum(x >= a and y <= b or a >= x and b <= y for a, b, x, y in input)
sum2 = sum(b >= x and a <= y for a, b, x, y in input)

advent.print_answer(1, sum1)
advent.print_answer(2, sum2)
