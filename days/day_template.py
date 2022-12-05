from __future__ import annotations

import sys
from typing import (
    Any,
    Iterable,
)


def parse_text(lines: Iterable[str]) -> Any:
    return []


def part_1(data: Any) -> Any:
    return 0


def part_2(data: Any) -> Any:
    return 0


def main(args: list[str]) -> None:
    data_file = args[0]
    with open(data_file) as f:
        parsed_data = parse_text(f.read().splitlines())

    print(f"Part 1: {part_1(parsed_data)}")
    print(f"Part 2: {part_2(parsed_data)}")


if __name__ == "__main__":
    main(sys.argv[1:])
