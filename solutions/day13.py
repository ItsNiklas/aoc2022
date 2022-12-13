#!/usr/bin/env python3
from functools import cmp_to_key
from itertools import count

from utils import advent

advent.setup(2022, 13)
fd = advent.get_input()

input = list(map(eval, fd.read().split()))
N = len(input)


def cmp(a, b) -> int:
    type_a, type_b = type(a), type(b)

    if type_a == type_b == int:
        return (a > b) - (a < b)  # Vanilla comparison -> LT, GT, EQ.
    elif type_a == type_b == list:
        for i in count(): # One of the lists is exhausted, or they are of equal length.
            if i == len(a) or i == len(b):
                return cmp(len(a), len(b))

            res = cmp(a[i], b[i])  # Compare list elements recursively.
            if res != 0:
                return res  # Non-match found.
    else:
        return cmp([a], b) if int == type_a else cmp(a, [b])  # Rerun after conversion


# Iterate over pairs and sum indices if LT is returned.
s = sum(idx // 2 + 1 for idx in range(0, N, 2) if cmp(input[idx], input[idx + 1]) < 0)
advent.print_answer(1, s)

# Add divider packets and sort with the custom comparison defined above.
packets = input + [[[2]]] + [[[6]]]
packets.sort(key=cmp_to_key(cmp))
advent.print_answer(2, (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))
