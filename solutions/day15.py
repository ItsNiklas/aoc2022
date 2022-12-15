#!/usr/bin/env python3

import io
import re
import sys

from utils import advent

advent.setup(2022, 15)
fd = advent.get_input() if not 'debug' in sys.argv else io.StringIO("""\
Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
""")
y_query = 2_000_000 if not 'debug' in sys.argv else 10
max_signal = 2 * y_query


def dist(p: complex, q: complex):
    return abs(p.real - q.real) + abs(p.imag - q.imag)


sensors: list[tuple[complex, float]] = list()
beacons: set[complex] = set()
ex_row: set[complex] = set()

for line in fd:
    s_x, s_y, b_x, b_y = map(int, re.findall(r'-?\d+', line))
    S = complex(s_x, s_y)
    B = complex(b_x, b_y)
    d = dist(S, B)

    sensors.append((S, d))
    beacons.add(B)

    y_diff = abs(s_y - y_query)
    ex_row |= set(complex(r, y_query) for r in range(int(S.real - d + y_diff), int(S.real + d - y_diff + 1)))

advent.print_answer(1, len(ex_row - beacons))
