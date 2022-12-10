#!/usr/bin/env python3

from utils import advent

advent.setup(2022, 10)
fd = advent.get_input()

X, cycle, signal = 1, 0, 0
crt = [" "] * 240


def sig():
    global signal
    if not (cycle - 20) % 40: signal += cycle * X


def draw():
    if abs(X - (cycle - 1) % 40) <= 1: crt[cycle - 1] = '█'


for line in fd:  # Execution cycle
    cycle += 1
    sig(), draw()
    if len(line) > 5:  # addx V
        cycle += 1
        sig(), draw()
        X += int(line[5:])
    else:  # noop
        pass

advent.print_answer(1, signal)
advent.print_answer(2, '\n' + '\n'.join(" ".join(crt[i:i + 40]) for i in range(0, 240, 40)))
