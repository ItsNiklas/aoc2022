#!/usr/bin/env python3

import io
import re
import sys
from collections import deque
from dataclasses import dataclass

from utils import advent

advent.setup(2022, 19)
fd = advent.get_input() if not 'debug' in sys.argv else io.StringIO("""\
Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.
""")


@dataclass
class Blueprint:
    id: int
    ore_robot_cost: int
    clay_robot_cost: int
    obsidian_robot_cost: tuple[int, int]
    geode_robot_cost: tuple[int, int]


input: list[Blueprint] = []

for line in fd:
    l = list(map(int, re.findall(r'(\d+)', line)))
    input.append(Blueprint(l[0], l[1], l[2], (l[3], l[4]), (l[5], l[6])))

for b in input:
    m_print = 100

    # inital state
    # minutes, ore_r, ore, clay_r, clay, obs_r, obs, geo_r, geo
    start = (24, 1, 0, 0, 0, 0, 0, 0, 0)
    q = deque([start])
    while q:
        minutes, ore_r, ore, clay_r, clay, obs_r, obs, geo_r, geo = q.popleft()

        # if minutes < m_print:
        #    print(25 - minutes, '|' , ore_r, ore, clay_r, clay, obs_r, obs, geo_r, geo, '|', len(q))
        #    m_print = minutes

        print(25 - minutes, '|', ore_r, ore, clay_r, clay, obs_r, obs, geo_r, geo, '|', len(q))

        if minutes == 0:
            break

        # simulate 1 minute
        ore_new = ore + ore_r
        clay_new = clay + clay_r
        obs_new = obs + obs_r
        geo_new = geo + geo_r
        minutes -= 1

        # Choices based on B:
        if ore >= b.ore_robot_cost:  # Build ore robot
            if max([b.ore_robot_cost, b.clay_robot_cost, b.obsidian_robot_cost[0],
                    b.geode_robot_cost[0]]) > ore_r:  # Do we need more?
                n = (minutes, ore_r + 1, ore_new - b.ore_robot_cost, clay_r, clay_new, obs_r, obs_new, geo_r, geo_new)
                q.append(n)

        if ore >= b.clay_robot_cost:  # Build clay robot
            if b.obsidian_robot_cost[1] > clay_r:  # Do we need more?
                n = (minutes, ore_r, ore_new - b.clay_robot_cost, clay_r + 1, clay_new, obs_r, obs_new, geo_r, geo_new)
                q.append(n)

        if all(i >= j for i, j in zip((ore, clay), b.obsidian_robot_cost)):  # Build obsidian robot
            if b.geode_robot_cost[1] > obs_r:  # Do we need more?
                n = (minutes, ore_r, ore_new - b.obsidian_robot_cost[0], clay_r, clay_new - b.obsidian_robot_cost[1],
                     obs_r + 1, obs_new, geo_r, geo_new)
                q.append(n)

        if all(i >= j for i, j in zip((ore, obs), b.geode_robot_cost)):  # Build geode robot
            q.append((minutes, ore_r, ore_new - b.geode_robot_cost[0], clay_r, clay_new, obs_r,
                      obs_new - b.geode_robot_cost[1], geo_r + 1, geo_new))

        # Build nothing
        if len(q) == 0:
            q.append((minutes, ore_r, ore_new, clay_r, clay_new, obs_r, obs_new, geo_r, geo_new))

    print(max(geo for minutes, ore_r, ore, clay_r, clay, obs_r, obs, geo_r, geo in q))
