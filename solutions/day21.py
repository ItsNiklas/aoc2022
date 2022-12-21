#!/usr/bin/env python3
import functools
import re
from typing import Union

from sympy import parsing, solvers

from utils import advent

advent.setup(2022, 21)
fd = advent.get_input()

nums: dict[str, Union[int, str]] = dict()
adj: dict[str, tuple[str, str, str]] = dict()

for line in fd:
    match = re.search(r'\d+', line)
    if match:
        nums |= {line[:4]: int(match.group(0))}
    else:
        adj |= {line[:4]: (line[6:10], line[13:17], line[11])}


@functools.cache
def resolve(node: str, human: bool) -> Union[int, str]:
    if human and node == 'humn':
        return 'humn'

    if node in nums:
        return nums[node]

    lhs, rhs, op = adj[node]
    lhs_r, rhs_r = resolve(lhs, human), resolve(rhs, human)

    if human:
        if node == 'root':
            return 'Eq (' + str(lhs_r) + ',' + str(rhs_r) + ')'
        if type(rhs_r) is str:
            return '(' + str(lhs_r) + op + rhs_r + ')'
        if type(lhs_r) is str:
            return '(' + lhs_r + op + str(rhs_r) + ')'

    match op:
        case '+': return lhs_r + rhs_r
        case '-': return lhs_r - rhs_r
        case '*': return lhs_r * rhs_r
        case '/': return lhs_r // rhs_r


advent.print_answer(1, resolve('root', human=False))

eq = parsing.sympy_parser.parse_expr(resolve('root', human=True))
advent.print_answer(2, solvers.solve(eq, numerical=False)[0])
