#!/usr/bin/env python3

from utils import advent

advent.setup(2022, 7)
fd = advent.get_input()


class Directory:
    def __init__(self, name, parent=None):
        self.name: str = name
        self.parent: Directory = parent
        self.files: list[tuple[str, int]] = []
        self.subdirectories: list[Directory] = []

        self.total_size: int = 0

    def add_file(self, file_name, size):
        self.files.append((file_name, size))

    def add_subdirectory(self, subdirectory):
        self.subdirectories.append(subdirectory)

    def get_subdirectory(self, name):
        return list(filter(lambda s: s.name == name, self.subdirectories)).pop()

    def traverse_for_deletion(self, space_to_be_cleared):
        assert self.total_size != 0

        if self.total_size >= space_to_be_cleared:
            global smallest_deletion
            smallest_deletion = min(smallest_deletion, self.total_size)

        for subdirectory in self.subdirectories:  # Traverse subdirectories recursively
            subdirectory.traverse_for_deletion(space_to_be_cleared)

    def traverse_to_parent(self):
        if self.parent:  # If current directory has a parent, traverse to it
            return self.parent

    def calc_total_sizes(self):
        if self.total_size == 0:
            self.total_size = sum(subd.calc_total_sizes() for subd in self.subdirectories) + sum(
                size for file, size in self.files)
        return self.total_size

    def get_sum_of_small_folders(self):
        assert self.total_size != 0
        return sum(subd.get_sum_of_small_folders() for subd in self.subdirectories) + (
            self.total_size if self.total_size <= 100000 else 0)


current_dir = None
for line in fd.read().splitlines():
    if line == "$ cd /":  # Create root
        current_dir = Directory('/')
    elif line.startswith('$'):
        if line[2:].startswith("cd"):  # Change directory up or down
            if line[5:] == '..':  # Traverse to parent
                current_dir = current_dir.parent
            else:  # Traverse to subdirectory
                current_dir = current_dir.get_subdirectory(line[5:])
    elif line.startswith("dir"):  # Read to current directory
        current_dir.add_subdirectory(Directory(f'{line[4:]}', current_dir))
    else:  # Read file
        current_dir.add_file(line.split(" ")[1], int(line.split(" ")[0]))

# Set current directory to root node.
while current_dir.parent is not None:
    current_dir = current_dir.traverse_to_parent()

current_dir.calc_total_sizes()
advent.print_answer(1, current_dir.get_sum_of_small_folders())

smallest_deletion = float('inf')
current_dir.traverse_for_deletion(30000000 - (70000000 - current_dir.total_size))
advent.print_answer(2, smallest_deletion)
