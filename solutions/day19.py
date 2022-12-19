#!/usr/bin/env python3

import re
from collections import deque
from dataclasses import dataclass

from utils import advent

advent.setup(2022, 19)
fd = advent.get_input()


@dataclass
class Blueprint:
    id: int
    ore_robot_cost: int
    clay_robot_cost: int
    obsidian_robot_cost: tuple[int, int]
    geode_robot_cost: tuple[int, int]


input: list[Blueprint] = []
for line in fd:
    l = list(map(int, re.findall(r"(\d+)", line)))
    input.append(Blueprint(l[0], l[1], l[2], (l[3], l[4]), (l[5], l[6])))

quality_sum = 0
max_geodes = 1

for b in input:
    m_print = -1

    # Inital state
    # minutes, ore_r, ore, clay_r, clay, obs_r, obs, geo_r, geo
    q = deque([(0, 1, 0, 0, 0, 0, 0, 0, 0)])
    g_max = 0
    cont = False
    max_ore_need = max([b.ore_robot_cost, b.clay_robot_cost, b.obsidian_robot_cost[0], b.geode_robot_cost[0]])

    while q:
        minutes, ore_r, ore, clay_r, clay, obs_r, obs, geo_r, geo = q.popleft()

        if minutes > m_print:
            g_max = max((geo for _, _, _, _, _, _, _, _, geo in q), default=0)
            m_print = minutes

        if minutes == 24 and not cont:
            cont = True
            quality_sum += b.id * g_max
            if b.id > 3: break

        if minutes == 32:
            max_geodes *= g_max
            break

        # Prune (agressive)
        if geo < g_max - 2:
            continue

        if ore > 15:
            continue
        # I'm sure more can be done here, but it ran in a reasonable time.

        # Simulate 1 minute:
        ore_new = ore + ore_r
        clay_new = clay + clay_r
        obs_new = obs + obs_r
        geo_new = geo + geo_r
        minutes += 1

        # Choices based on the blueprint:
        if ore >= b.ore_robot_cost:  # Build ore robot
            if max_ore_need > ore_r:  # Do we need more?
                q.append(
                    (minutes, ore_r + 1, ore_new - b.ore_robot_cost, clay_r, clay_new, obs_r, obs_new, geo_r, geo_new,)
                )

        if ore >= b.clay_robot_cost:  # Build clay robot
            if b.obsidian_robot_cost[1] > clay_r:  # Do we need more?
                q.append(
                    (minutes, ore_r, ore_new - b.clay_robot_cost, clay_r + 1, clay_new, obs_r, obs_new, geo_r, geo_new,)
                )

        if all(i >= j for i, j in zip((ore, clay), b.obsidian_robot_cost)):  # Build obsidian robot
            if b.geode_robot_cost[1] > obs_r:  # Do we need more?
                q.append(
                    (minutes, ore_r, ore_new - b.obsidian_robot_cost[0], clay_r, clay_new - b.obsidian_robot_cost[1],
                     obs_r + 1, obs_new, geo_r, geo_new,)
                )

        if all(i >= j for i, j in zip((ore, obs), b.geode_robot_cost)):  # Build geode robot
            q.append(
                (minutes, ore_r, ore_new - b.geode_robot_cost[0], clay_r, clay_new, obs_r,
                 obs_new - b.geode_robot_cost[1], geo_r + 1, geo_new,)
            )

        # Build nothing and wait, if it makes sense.
        if ore_new <= 6:
            q.append(
                (minutes, ore_r, ore_new, clay_r, clay_new, obs_r, obs_new, geo_r, geo_new,)
            )

advent.print_answer(1, quality_sum)
advent.print_answer(2, max_geodes)
