from __future__ import annotations

import copy
import re
import sys
from dataclasses import dataclass
from typing import (
    Any,
    Iterable,
)


@dataclass
class Move:
    num_to_move: int
    from_stack: int
    to_stack: int

    @classmethod
    def from_str(cls, line: str) -> Move:
        move_match = re.match(r"^move (\d+) from (\d) to (\d)$", line)
        assert move_match is not None
        return cls(
            num_to_move=int(move_match.group(1)),
            from_stack=int(move_match.group(2)),
            to_stack=int(move_match.group(3)),
        )


def perform_moves_on_stacks_part_1(
    stacks: list[list[str]], moves: Iterable[Move]
) -> list[list[str]]:
    # Deepcopy so the original stacks aren't modified.
    stacks_new = copy.deepcopy(stacks)
    for move in moves:
        for _ in range(move.num_to_move):
            stacks_new[move.to_stack - 1].append(
                stacks_new[move.from_stack - 1].pop()
            )

    return stacks_new


def perform_moves_on_stacks_part_2(
    stacks: list[list[str]], moves: Iterable[Move]
) -> list[list[str]]:
    # Deepcopy so the original stacks aren't modified.
    stacks_new = copy.deepcopy(stacks)
    for move in moves:
        to_move = []
        for _ in range(move.num_to_move):
            to_move.append(stacks_new[move.from_stack - 1].pop())
        stacks_new[move.to_stack - 1] += list(reversed(to_move))

    return stacks_new


def stacks_to_str(stacks: list[list[str]]) -> None:
    max_height = max(len(stack) for stack in stacks)
    lines = [" " + "   ".join([str(i + 1) for i in range(len(stacks))]) + " "]
    for idx in range(max_height):
        line = ""
        for stack in stacks:
            if line:
                line += " "
            try:
                val = stack[idx]
            except IndexError:
                line += "   "
            else:
                line += f"[{val}]"
        lines.append(line)

    return "\n".join(reversed(lines))


def _parse_stacks(lines: Iterable[str]) -> Any:
    # Example stack data:
    #     [D]
    # [N] [C]
    # [Z] [M] [P]
    #  1   2   3
    #
    # Stacks occur every 4th element in a line, starting from index 1. Can
    # parse assuming this. The above will be parsed into:
    # [["Z", "N"], ["M", "C", "D"], ["P"]]

    # Reverse so the stack numbers are on the first line.
    lines = [line for line in lines if line.strip()]
    lines.reverse()

    # Get the stack entries on each level.
    stacks_split = [line[1::4] for line in lines]
    stacks = []
    for idx in range(len(stacks_split[0])):
        # Combine the stack entries for each level for this particular stack.
        stacks.append(
            [line[idx] for line in stacks_split[1:] if line[idx].strip()]
        )

    return stacks


def parse_text_into_stacks_and_moves(
    lines: Iterable[str],
) -> tuple[list[list[str]], list[Move]]:
    # Find the first line starting with "move". Everything above it will be the
    # stacks, everything below it (including itself) will be the moves.
    move_idx = None
    for idx, line in enumerate(lines):
        if line.startswith("move"):
            move_idx = idx
            break
    assert move_idx is not None

    stacks = _parse_stacks(lines[:move_idx])
    moves = [Move.from_str(line) for line in lines[move_idx:]]
    return stacks, moves


def part_1(stacks: list[list[str]], moves: Iterable[Move]) -> str:
    stacks_new = perform_moves_on_stacks_part_1(stacks, moves)
    return "".join(stack[-1] for stack in stacks_new)


def part_2(stacks: list[list[str]], moves: Iterable[Move]) -> Any:
    stacks_new = perform_moves_on_stacks_part_2(stacks, moves)
    return "".join(stack[-1] for stack in stacks_new)


def main(args: list[str]) -> None:
    data_file = args[0]
    with open(data_file) as f:
        stacks, moves = parse_text_into_stacks_and_moves(f.read().splitlines())

    print(f"Part 1: Top stack order = {part_1(stacks, moves)}")
    print(f"Part 2: Top stack order = {part_2(stacks, moves)}")


if __name__ == "__main__":
    main(sys.argv[1:])
