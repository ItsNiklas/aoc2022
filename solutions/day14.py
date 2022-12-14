#!/usr/bin/env python3

import itertools

from utils import advent

advent.setup(2022, 14)
fd = advent.get_input()

rock = set()

for line in fd:
    line = [complex(n.replace(",", "+") + "j") for n in line.strip().split(" -> ")]

    for fr, to in itertools.pairwise(line):
        rock.add(to)
        if fr.real == to.real:
            rock.update(
                complex(fr.real, c)
                for c in range(
                    int(fr.imag), int(to.imag), -1 if to.imag < fr.imag else 1
                )
            )
        else:
            rock.update(
                complex(r, fr.imag)
                for r in range(
                    int(fr.real), int(to.real), -1 if to.real < fr.real else 1
                )
            )

abyss: float = max(c.imag for c in rock) + 1


def simulate(floor: bool = False):
    sand, new = set(), None
    while True:
        if new is None:
            new = 500 + 0j

        # Fallen into the Abyss?
        elif not floor and new.imag >= abyss:
            return len(sand)

        # A unit of sand comes to rest at 500,0.
        elif floor and new in sand:
            return len(sand)

        # Down one step?
        elif new + 1j not in rock and new + 1j not in sand and new.imag < abyss:
            new += 1j

        # One step down and to the left?
        elif new + 1j - 1 not in rock and new + 1j - 1 not in sand and new.imag < abyss:
            new += 1j - 1

        # One step down and to the right?
        elif new + 1j + 1 not in rock and new + 1j + 1 not in sand and new.imag < abyss:
            new += 1j + 1

        # All three possible destinations are blocked.
        # Comes to rest.
        else:
            sand.add(new)
            new = None


advent.print_answer(1, simulate(floor=False))
advent.print_answer(2, simulate(floor=True))
