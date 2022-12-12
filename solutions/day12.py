#!/usr/bin/env python3
import functools
from heapq import heappop, heappush

from utils import advent

advent.setup(2022, 12)
fd = advent.get_input()

input = fd.readlines()
N, M = len(input), len(input[0])

start = next(complex(i, line.index('S')) for i, line in enumerate(input) if 'S' in line)
goal = next(complex(i, line.index('E')) for i, line in enumerate(input) if 'E' in line)


def dijkstra(source: complex, destination: complex):
    @functools.cache
    def h(vertex: complex):  # Height
        if not (0 <= vertex.real < N and 0 <= vertex.imag < M): return 999
        if vertex == start: return ord('a')
        if vertex == goal: return ord('z')
        return ord(input[int(vertex.real)][int(vertex.imag)])

    def neighbors(v: complex):
        return filter(lambda n: h(v) + 1 >= h(n), [v + 1, v - 1, v + 1j, v - 1j])

    # Store the distances from the source node to all other nodes
    distances = {source: 0}
    # Create a priority queue to track which node to explore next
    queue = []
    heappush(queue, (0, str(source)))

    while queue:
        # Get the node with the smallest distance from the source
        distance, node = heappop(queue)
        node = complex(node)
        # Stop if we have reached the destination node
        if node == destination: break

        # Update the distances of the node's neighbors
        for neighbor in neighbors(node):
            new_distance = distance + 1
            if neighbor not in distances or new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heappush(queue, (new_distance, str(neighbor)))

    return distances[destination]


advent.print_answer(1, dijkstra(start, goal))

starts = (complex(i, line.index('a')) for i, line in enumerate(input) if 'a' in line)
advent.print_answer(2, min(dijkstra(start, goal) for start in starts))
