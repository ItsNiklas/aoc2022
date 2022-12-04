#!/usr/bin/env python3
from utils import advent


def prio(e: set) -> int:
    e = e.pop()
    return ord(e) - (ord('A') - 27 if e.isupper() else ord('a') - 1)


advent.setup(2022, 3)
fd = advent.get_input()

input = [l.rstrip() for l in fd.readlines()]
sum1 = sum(prio(set(l[:len(l) // 2]) & set(l[len(l) // 2:])) for l in input)

input = zip(*[iter(input)] * 3)
sum2 = sum(prio(set(a) & set(b) & set(c)) for a, b, c in input)

advent.print_answer(1, sum1)
advent.print_answer(2, sum2)
