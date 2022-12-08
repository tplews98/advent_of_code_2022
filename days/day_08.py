from __future__ import annotations

import sys
from dataclasses import dataclass


@dataclass
class Grid:
    grid: tuple[tuple[int, ...], ...]
    size_x: int
    size_y: int

    @classmethod
    def from_lines(cls, lines: list[str]) -> Grid:
        size_y = len(lines)
        size_x = len(lines[0])
        grid = tuple(tuple(int(d) for d in tuple(line)) for line in lines)
        return cls(grid, size_x, size_y)

    def is_tree_visible(self, x: int, y: int) -> bool:
        # Is tree on the outside?
        if (
            x == 0
            or y == 0
            or x == (self.size_x - 1)
            or y == (self.size_y - 1)
        ):
            return True

        # Check if visible in x direction. Only care if it is visible in any
        # direction so short circuit later checks if it has already been found
        # to be visible.
        self_height = self.grid[y][x]
        is_visible = all(
            self.grid[y][x_iter] < self_height for x_iter in range(x)
        )
        is_visible = is_visible or all(
            self.grid[y][x_iter] < self_height
            for x_iter in range(x + 1, self.size_x)
        )
        # Check if visible in y direction.
        is_visible = is_visible or all(
            self.grid[y_iter][x] < self_height for y_iter in range(y)
        )
        is_visible = is_visible or all(
            self.grid[y_iter][x] < self_height
            for y_iter in range(y + 1, self.size_y)
        )
        return is_visible

    def get_scenic_score(self, x: int, y: int) -> int:
        self_height = self.grid[y][x]

        scenic_score_left = 0
        for x_iter in reversed(range(0, x)):
            scenic_score_left += 1
            if self.grid[y][x_iter] >= self_height:
                # Is same height or higher, stop looking.
                break

        scenic_score_right = 0
        for x_iter in range(x + 1, self.size_x):
            scenic_score_right += 1
            if self.grid[y][x_iter] >= self_height:
                # Is same height or higher, stop looking.
                break

        scenic_score_up = 0
        for y_iter in reversed(range(0, y)):
            scenic_score_up += 1
            if self.grid[y_iter][x] >= self_height:
                # Is same height or higher, stop looking.
                break

        scenic_score_down = 0
        for y_iter in range(y + 1, self.size_y):
            scenic_score_down += 1
            if self.grid[y_iter][x] >= self_height:
                # Is same height or higher, stop looking.
                break

        return (
            scenic_score_left
            * scenic_score_right
            * scenic_score_up
            * scenic_score_down
        )


def part_1(grid: Grid) -> int:
    return sum(
        1 if grid.is_tree_visible(x, y) else 0
        for x in range(grid.size_x)
        for y in range(grid.size_y)
    )


def part_2(grid: Grid) -> int:
    return max(
        grid.get_scenic_score(x, y)
        for x in range(grid.size_x)
        for y in range(grid.size_y)
    )


def main(args: list[str]) -> None:
    data_file = args[0]
    with open(data_file) as f:
        grid = Grid.from_lines(f.read().splitlines())

    print(f"Part 1: Number of visible trees = {part_1(grid)}")
    print(f"Part 2: Maximum scenic score = {part_2(grid)}")


if __name__ == "__main__":
    main(sys.argv[1:])
