#!/usr/bin/env python3

import re

from utils import advent


def dist(p: complex, q: complex) -> float:
    return abs(p.real - q.real) + abs(p.imag - q.imag)


advent.setup(2022, 15)
fd = advent.get_input()

y_query = 2_000_000
max_signal = 2 * y_query

sensors: list[tuple[complex, float]] = list()
beacons: set[complex] = set()
ex_row: set[complex] = set()

for line in fd:
    s_x, s_y, b_x, b_y = map(int, re.findall(r"-?\d+", line))
    S = complex(s_x, s_y)
    B = complex(b_x, b_y)
    d = dist(S, B)

    sensors.append((S, d))
    beacons.add(B)

    y_range = int(d - abs(s_y - y_query))
    ex_row |= set(complex(s_x + dr, y_query) for dr in range(-y_range, y_range + 1))

advent.print_answer(1, len(ex_row - beacons))

for S, d in sensors:
    # Walk along perimeter of S.
    curr: complex = S + complex(0, d + 1)

    for ds in [1 - 1j, -1 - 1j, -1 + 1j, 1 + 1j]:
        while dist(curr + ds, S) == d + 1:
            curr += ds
            # Check curr (if inbounds).
            if 0 <= curr.imag <= max_signal and 0 <= curr.real <= max_signal:
                # Is curr covered by any other sensor? If not: Distress beacon.
                for S_, d_ in sensors:
                    if dist(S_, curr) <= d_:
                        break
                else:
                    advent.print_answer(2, int(curr.real * 4_000_000 + curr.imag))
                    exit()
