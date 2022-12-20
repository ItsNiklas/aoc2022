#!/usr/bin/env python3

import io
import sys
from random import getrandbits

from utils import advent

advent.setup(2022, 20)
fd = advent.get_input() if not 'debug' in sys.argv else io.StringIO("""\
1
2
-3
3
-2
0
4
""")

# Making entries unique so that I can call .index() by appending a random hash.
file: list[str] = list(map(lambda s: s.strip() + str(hex(getrandbits(32))), fd))
N = len(file)

for di in file.copy():
    i = file.index(di)
    offset = i + int(di.split('0x')[0])

    file.pop(i)
    file.insert(offset % (N - 1), di)

    if 'debug' in sys.argv: print(file)

z_i = list(x.startswith('00x') for x in file).index(True)
advent.print_answer(1, sum(int(file[(z_i + 1000 * i) % N].split('0x')[0]) for i in range(1, 4)))
