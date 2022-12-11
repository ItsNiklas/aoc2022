#!/usr/bin/env python3
from copy import deepcopy
from heapq import nlargest
from math import prod
from re import findall

from utils import advent

advent.setup(2022, 11)
fd = advent.get_input()

input = fd.read().split('\n\n')

monkey_inv, monkey_throw, monkey_operation = [], [], []
monkey_n_insp = [0] * len(input)

# PARSE
for i, s in enumerate(input):
    lines = s.splitlines()
    monkey_inv.append(list(map(int, findall(r"(\d+)", lines[1]))))
    monkey_throw.append(tuple(map(int, findall(r"(\d+)", "".join(lines[3:])))))
    monkey_operation.append(lines[2][19:])

monkey_inv2 = deepcopy(monkey_inv)

# Keep numbers manageable.
mod = prod(test for test, _, _ in monkey_throw)

# PLAY
for k in range(20):
    for i in range(len(input)):
        # Monkey i
        test, t, f = monkey_throw[i]
        monkey_n_insp[i] += len(monkey_inv[i])
        while monkey_inv[i]:
            item = eval(monkey_operation[i], {'old': monkey_inv[i].pop()}) // 3
            monkey_inv[t if not item % test else f].append(item % mod)

advent.print_answer(1, prod(nlargest(2, monkey_n_insp)))

# RESET
monkey_n_insp = [0] * len(input)

# PLAY
for k in range(10000):
    for i in range(len(input)):
        # Monkey i
        test, t, f = monkey_throw[i]
        monkey_n_insp[i] += len(monkey_inv2[i])
        while monkey_inv2[i]:
            item = eval(monkey_operation[i], {'old': monkey_inv2[i].pop()})
            monkey_inv2[t if not item % test else f].append(item % mod)

advent.print_answer(2, prod(nlargest(2, monkey_n_insp)))
