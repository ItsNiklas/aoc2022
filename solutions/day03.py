#!/usr/bin/env python3
from utils import advent

advent.setup(2022, 3)
fd = advent.get_input()

input = [l.rstrip() for l in fd.readlines()]

def prio(e: str) -> int:
    return ord(e) - (ord('A') - 27 if e.isupper() else ord('a') - 1)

sum1 = sum(
    prio(next(iter(set(l[:len(l) // 2]) & set(l[len(l) // 2:])))) for l in input
)

sum2 = sum(
    prio(next(iter(set(a) & set(b) & set(c)))) for a, b, c in zip(*(iter(input),) * 3)
)

advent.print_answer(1, sum1)
advent.print_answer(2, sum2)