#!/usr/bin/env python3
from math import prod

import numpy as np

from utils import advent


def calc_visible(a):
    v = np.zeros_like(a)
    max_tree = -1
    for k, tree in enumerate(a):
        if tree > max_tree: v[k] = 1
        max_tree = max(tree, max_tree)

    # Reversed views
    max_tree = -1
    for k, tree in enumerate(a[::-1]):
        if tree > max_tree: v[::-1][k] = 1
        max_tree = max(tree, max_tree)
    return v


def scenic(a):
    # Wanted to use itertools, but it's not clean here.
    s = 0
    for tree in a[1:]:
        s += 1
        if tree >= a[0]: break
    return s


def calc_scenic_score(x, y):
    if x == 0 or x == n - 1 or y == 0 or y == n - 1: return 0  # Skip edges (optimization)
    scores = map(scenic, [forest[x:, y], forest[x, y:], forest[:x + 1, y][::-1], forest[x, :y + 1][::-1]])
    return prod(scores)


advent.setup(2022, 8)
fd = advent.get_input()

forest = np.asarray([list(l.strip()) for l in fd], int)
n = len(forest)
visible = np.zeros_like(forest)

for i in range(n):
    # l to r, r to l // t to b, b to t
    visible[i, :] = np.fmax(visible[i, :], calc_visible(forest[i, :]))
    visible[:, i] = np.fmax(visible[:, i], calc_visible(forest[:, i]))

advent.print_answer(1, visible.sum())
advent.print_answer(2, max(calc_scenic_score(i, j) for i, j in np.ndindex(forest.shape)))
