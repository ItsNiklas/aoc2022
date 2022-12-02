#!/usr/bin/env python3
from utils import advent

advent.setup(2022, 2)
fd = advent.get_input()

#         Rock  < Paper < Sci   < Rock
score = {'X': 1, 'Y': 2, 'Z': 3,
         'A': 1, 'B': 2, 'C': 3}

sum1, sum2 = 0, 0
for opp, sel in map(lambda x: x.split(), fd.readlines()):
    if score[sel] == score[opp]:
        sum1 += 3
    elif score[sel] == score[opp] % 3 + 1:
        sum1 += 6
    sum1 += score[sel]

    if sel == 'Y':
        sum2 += 3 + score[opp]
    elif sel == 'Z':
        sum2 += 6 + score[opp] % 3 + 1
    else:
        sum2 += (score[opp] + 1) % 3 + 1

advent.print_answer(1, sum1)
advent.print_answer(2, sum2)
