from __future__ import annotations

import enum
import sys
from dataclasses import dataclass

WIN_POINTS = 6
DRAW_POINTS = 3
LOSS_POINTS = 0


class _SymbolType(enum.IntEnum):
    ROCK = enum.auto()
    PAPER = enum.auto()
    SCISSORS = enum.auto()


@dataclass
class _SymbolInfo:
    type: _SymbolType
    points: int
    beats: _SymbolType
    loses: _SymbolType


class Symbol(_SymbolInfo, enum.Enum):
    ROCK = _SymbolType.ROCK, 1, _SymbolType.SCISSORS, _SymbolType.PAPER
    PAPER = _SymbolType.PAPER, 2, _SymbolType.ROCK, _SymbolType.SCISSORS
    SCISSORS = _SymbolType.SCISSORS, 3, _SymbolType.PAPER, _SymbolType.ROCK

    @classmethod
    def from_char(cls, char: str) -> Symbol:
        char = char.upper()
        if char in ("A", "X"):
            return cls.ROCK
        if char in ("B", "Y"):
            return cls.PAPER
        if char in ("C", "Z"):
            return cls.SCISSORS
        raise Exception(f"Invalid value '{char}'")

    @classmethod
    def from_type(cls, symbol_type: _SymbolType) -> Symbol:
        for option in cls:
            if symbol_type is option.type:
                return option
        raise Exception(f"Invalid symbole type '{symbol_type}'")

    @staticmethod
    def round_result_part_1(them: Symbol, you: str) -> int:
        you_symbol = Symbol.from_char(you)

        if them.beats is you_symbol.type:
            points = LOSS_POINTS
        elif them.loses is you_symbol.type:
            points = WIN_POINTS
        else:
            # Is a draw.
            points = DRAW_POINTS

        return points + you_symbol.points

    @staticmethod
    def round_result_part_2(them: Symbol, you: str) -> int:
        if you == "X":
            # Need to lose.
            you_symbol = Symbol.from_type(them.beats)
            points = LOSS_POINTS
        elif you == "Y":
            # Need to draw.
            you_symbol = them
            points = DRAW_POINTS
        elif you == "Z":
            you_symbol = Symbol.from_type(them.loses)
            points = WIN_POINTS
        else:
            raise Exception(f"Invalid value {you}")

        return points + you_symbol.points


def parse_text_into_rounds(lines: list[str]) -> list[tuple[Symbol, str]]:
    rounds: list[tuple[Symbol, str]] = []
    for line in lines:
        if not line:
            continue

        first, second = line.split()
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
        rounds = parse_text_into_rounds(f.read().splitlines())

    print(f"Part 1: Total points: {part_1(rounds)}")
    print(f"Part 2: Total points: {part_2(rounds)}")


if __name__ == "__main__":
    main(sys.argv[1:])
