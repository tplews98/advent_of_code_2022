from __future__ import annotations

import string
import sys
from collections import defaultdict
from dataclasses import dataclass
from typing import (
    Collection,
    Generator,
    Iterable,
)


@dataclass
class Bag:
    compartment_1: str
    compartment_2: str

    @classmethod
    def from_str(cls, all_contents: str) -> Bag:
        num_items = len(all_contents)
        assert num_items % 2 == 0
        return cls(
            all_contents[: num_items // 2], all_contents[num_items // 2 :]
        )

    @staticmethod
    def get_item_priority(item: str) -> int:
        assert len(item) == 1
        if item.isupper():
            return ord(item) - ord("A") + 27
        elif item.islower():
            return ord(item) - ord("a") + 1
        raise ValueError(f"'{item}' is not a valid item")

    def find_shared_items(self) -> set[str]:
        return set(self.compartment_1).intersection(self.compartment_2)

    @staticmethod
    def sort_into_groups(bags: Collection[Bag]) -> dict[str, list[Bag]]:
        def get_groups(
            bags: Collection[Bag],
        ) -> Generator[list[Bag], None, None]:
            bags = list(bags)
            num_bags = len(bags)
            assert num_bags % 3 == 0
            for i in range(0, num_bags, 3):
                yield bags[i : i + 3]

        groups: defaultdict[str, list[Bag]] = defaultdict(list)
        for group in get_groups(bags):
            shared_items = set(string.ascii_letters)
            for bag in group:
                shared_items &= set(bag.compartment_1 + bag.compartment_2)
            assert len(shared_items) == 1
            groups[shared_items.pop()].extend(group)

        return groups


def parse_text_into_bags(lines: Iterable[str]) -> list[Bag]:
    return [Bag.from_str(line) for line in lines]


def part_1(bags: Iterable[Bag]) -> int:
    return sum(
        Bag.get_item_priority(item)
        for bag in bags
        for item in bag.find_shared_items()
    )


def part_2(bags: Collection[Bag]) -> int:
    groups = Bag.sort_into_groups(bags)
    total_priority = 0
    for item, item_groups in groups.items():
        total_priority += Bag.get_item_priority(item) * len(item_groups) // 3
    return total_priority


def main(args: list[str]) -> None:
    data_file = args[0]
    with open(data_file) as f:
        bags = parse_text_into_bags(f.read().splitlines())

    print(f"Part 1: Total priority of shared items: {part_1(bags)}")
    print(f"Part 2: Total priority of groups: {part_2(bags)}")


if __name__ == "__main__":
    main(sys.argv[1:])
