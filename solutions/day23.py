#!/usr/bin/env python3

from itertools import count

from utils import advent

advent.setup(2022, 23)
fd = advent.get_input()
elves: set[complex] = set()
proposals: dict[complex, complex] = dict()  # To, From
invalid: list[complex] = list()

for i, line in enumerate(fd):
    for j, char in enumerate(line.strip()):
        if char == ".":
            continue
        elves.add(complex(i, j))

consider = [
    (-1, -1 + 1j, -1 - 1j),
    (1, 1 + 1j, 1 - 1j),
    (-1j, -1 - 1j, 1 - 1j),
    (1j, 1 + 1j, -1 + 1j),
]  # N, S, W, E

x8 = [1, 1 + 1j, 1j, -1 + 1j, -1, -1 - 1j, -1j, 1 - 1j]

for i in count():
    for elf in elves:
        # If no other Elves are in one of the eight positions, the Elf does not do anything
        if not any(elf + d in elves for d in x8):
            continue

        for dirs in consider:
            if not any(elf + d in elves for d in dirs):
                # move
                if elf + dirs[0] in proposals or elf + dirs[0] in invalid:
                    # Already proposed
                    del proposals[elf + dirs[0]]
                    invalid.append(elf + dirs[0])
                else:
                    proposals[elf + dirs[0]] = elf
                break

    if i == 10:
        w = max(map(lambda x: x.real, elves)) - min(map(lambda x: x.real, elves)) + 1
        l = max(map(lambda x: x.imag, elves)) - min(map(lambda x: x.imag, elves)) + 1
        advent.print_answer(1, int(l * w) - len(elves))

    if len(proposals) == 0:
        advent.print_answer(2, i + 1)
        break

    # Execute all remaining (valid) proposals
    for to, frm in proposals.items():
        elves.remove(frm)
        elves.add(to)

    invalid.clear()
    proposals.clear()
    consider.append(consider.pop(0))  # Rotate
