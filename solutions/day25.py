#!/usr/bin/env python3

from utils import advent

advent.setup(2022, 25)
fd = advent.get_input()


def SNAFU_to_int(num: str) -> int:
    dec: int = 0
    for i, v in enumerate(reversed(num.strip())):
        match v:
            case '=':
                dec += 5 ** i * -2
            case '-':
                dec += 5 ** i * -1
            case _:
                dec += 5 ** i * int(v)
    return dec


def int_to_SNAFU(n: int) -> str:
    converted: str = ""
    while n != 0:
        if (remainder := n % 5) > 2:
            remainder -= 5
            converted = ("=" if remainder == -2 else "-") + converted
        else:
            converted = str(remainder) + converted

        n = (n - remainder) // 5

    return converted


advent.print_answer(1, int_to_SNAFU(sum(map(SNAFU_to_int, fd))))
