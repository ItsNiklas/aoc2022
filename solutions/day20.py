#!/usr/bin/env python3

from random import getrandbits

from utils import advent

advent.setup(2022, 20)
fd = advent.get_input()


def mixing(times, DECRYPTION_KEY) -> int:
    fd.seek(0)

    # Making entries unique by appending a random hash so that I can call .index().
    file: list[str] = list(
        map(lambda s: str(int(s) * DECRYPTION_KEY) + str(hex(getrandbits(32))), fd)
    )
    N = len(file)
    pre_mixed = file.copy()

    for _ in range(times):
        for di in pre_mixed:
            i = file.index(di)
            offset = i + int(di.split("0x")[0])

            file.pop(i)
            file.insert(offset % (N - 1), di)

    # Find index of 0 and sum 1000, 2000 & 3000
    z_i: int = list(x.startswith("00x") for x in file).index(True)
    return sum(int(file[(z_i + 1000 * i) % N].split("0x")[0]) for i in range(1, 4))


advent.print_answer(1, mixing(1, 1))
advent.print_answer(2, mixing(10, 811589153))
