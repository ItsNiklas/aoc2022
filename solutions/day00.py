#!/usr/bin/env python3

import io
import sys

from utils import advent

advent.setup(2022, 0)
fd = advent.get_input() if not 'debug' in sys.argv else io.StringIO("""\
""")

x = int(*fd)

advent.print_answer(1, x)
advent.print_answer(2, 2 * x)
