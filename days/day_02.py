from __future__ import annotations

import enum
import sys


class Symbol(enum.IntEnum):
    ROCK = enum.auto()
    PAPER = enum.auto()
    SCISSORS = enum.auto()

    @classmethod
    def from_char(cls, char: str) -> Symbol:
        char = char.strip().upper()
        if char in ("A", "X"):
            return cls.ROCK
        if char in ("B", "Y"):
            return cls.PAPER
        if char in ("C", "Z"):
            return cls.SCISSORS
        raise Exception(f"Invalid value {char}")

    @property
    def points(self) -> int:
        if self is Symbol.ROCK:
            return 1
        if self is Symbol.PAPER:
            return 2
        if self is Symbol.SCISSORS:
            return 3
        raise Exception(f"Invalid value {self}")

    def beats(self) -> Symbol:
        if self is Symbol.ROCK:
            return Symbol.SCISSORS
        elif self is Symbol.PAPER:
            return Symbol.ROCK
        else:
            # Is scissors.
            return Symbol.PAPER

    def loses(self) -> Symbol:
        if self is Symbol.ROCK:
            return Symbol.PAPER
        elif self is Symbol.PAPER:
            return Symbol.SCISSORS
        else:
            # Is scissors.
            return Symbol.ROCK

    def round_result_part_1(them: Symbol, you: str) -> int:
        loss_points = 0
        draw_points = 3
        win_points = 6

        you_symbol = Symbol.from_char(you)

        if them.beats() is you_symbol:
            points = loss_points
        elif them.loses() is you_symbol:
            points = win_points
        else:
            # Is a draw.
            points = draw_points

        return points + you_symbol.points

    def round_result_part_2(them: Symbol, you: str) -> int:
        loss_points = 0
        draw_points = 3
        win_points = 6

        if you == "X":
            # Need to lose.
            you_symbol = them.beats()
            points = loss_points
        elif you == "Y":
            # Need to draw.
            you_symbol = them
            points = draw_points
        elif you == "Z":
            you_symbol = them.loses()
            points = win_points
        else:
            raise Exception(f"Invalid value {you}")

        return points + you_symbol.points


def parse_text_into_rounds(lines: list[str]) -> list[tuple[Symbol, str]]:
    rounds: list[tuple[Symbol, str]] = []
    for line in lines:
        if not line:
            continue

        first, second = line.strip().split()
        rounds.append((Symbol.from_char(first), second))

    return rounds


def part_1(rounds: list[tuple[Symbol, str]]) -> int:
    return sum(
        Symbol.round_result_part_1(round[0], round[1]) for round in rounds
    )


def part_2(rounds: list[tuple[Symbol, str]]) -> int:
    return sum(
        Symbol.round_result_part_2(round[0], round[1]) for round in rounds
    )


def main(args: list[str]) -> None:
    data_file = args[0]
    with open(data_file) as f:
        rounds = parse_text_into_rounds(f.readlines())

    print(f"Part 1: Total points: {part_1(rounds)}")
    print(f"Part 1: Total points: {part_2(rounds)}")


if __name__ == "__main__":
    main(sys.argv[1:])
