from __future__ import annotations

import sys
from dataclasses import dataclass
from typing import Iterable


@dataclass
class SectionAssignment:
    start: int
    end: int

    def __post__init__(self) -> None:
        assert self.end >= self.start

    @classmethod
    def from_str(cls, string: str) -> SectionAssignment:
        start_end_list = string.split("-")
        return cls(int(start_end_list[0]), int(start_end_list[1]))

    @staticmethod
    def does_pair_overlap_completely(
        pair: tuple[SectionAssignment, SectionAssignment]
    ) -> bool:
        first, second = pair
        return (first.start <= second.start and first.end >= second.end) or (
            second.start <= first.start and second.end >= first.end
        )

    @staticmethod
    def does_pair_overlap_partially(
        pair: tuple[SectionAssignment, SectionAssignment]
    ) -> bool:
        first, second = pair
        return (first.start <= second.start <= first.end) or (
            second.start <= first.start <= second.end
        )


def parse_text_into_assignment_pairs(
    lines: Iterable[str],
) -> list[tuple[SectionAssignment, SectionAssignment]]:
    return [
        (
            SectionAssignment.from_str(line.split(",")[0]),
            SectionAssignment.from_str(line.split(",")[1]),
        )
        for line in lines
    ]


def part_1(
    assignment_pairs: Iterable[tuple[SectionAssignment, SectionAssignment]]
) -> int:
    return len(
        [
            pair
            for pair in assignment_pairs
            if SectionAssignment.does_pair_overlap_completely(pair)
        ]
    )


def part_2(
    assignment_pairs: Iterable[tuple[SectionAssignment, SectionAssignment]]
) -> int:
    return len(
        [
            pair
            for pair in assignment_pairs
            if SectionAssignment.does_pair_overlap_partially(pair)
        ]
    )


def main(args: list[str]) -> None:
    data_file = args[0]
    with open(data_file) as f:
        assignment_pairs = parse_text_into_assignment_pairs(
            f.read().splitlines()
        )

    print(
        "Part 1: Number of complete overlaps in pairs: "
        f"{part_1(assignment_pairs)}"
    )
    print(
        "Part 2: Number of partial overlaps in pairs: "
        f"{part_2(assignment_pairs)}"
    )


if __name__ == "__main__":
    main(sys.argv[1:])
