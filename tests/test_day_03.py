from __future__ import annotations

import os
import sys

import pytest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(REPO_ROOT)

from days import day_03
from days.day_03 import Bag


@pytest.fixture
def bags_test_data() -> list[Bag]:
    with open(os.path.join(REPO_ROOT, "data", "day_03_test.txt")) as f:
        return day_03.parse_text_into_bags(f.read().splitlines())


def test_parse() -> None:
    lines = ["abcdef", "abcDEF", "aAaBbB", "abcdefZYXWVUghijklTSRQPO"]
    expected_bags = [
        Bag("abc", "def"),
        Bag("abc", "DEF"),
        Bag("aAa", "BbB"),
        Bag("abcdefZYXWVU", "ghijklTSRQPO"),
    ]
    bags = day_03.parse_text_into_bags(lines)
    assert bags == expected_bags

    wrong_length_lines = ["a", "ZYX"]
    for line in wrong_length_lines:
        with pytest.raises(AssertionError):
            day_03.parse_text_into_bags([line])


def test_get_shared_items() -> None:
    bag = Bag("aaa", "bbb")
    assert bag.find_shared_items() == set()

    bag = Bag("aaa", "aaa")
    assert bag.find_shared_items() == {"a"}

    bag = Bag("ALzZ", "abcdefzzzZZZAAA")
    assert bag.find_shared_items() == {"A", "z", "Z"}


def test_get_priorites() -> None:
    assert Bag.get_item_priority("a") == 1
    assert Bag.get_item_priority("m") == 13
    assert Bag.get_item_priority("z") == 26
    assert Bag.get_item_priority("A") == 27
    assert Bag.get_item_priority("Z") == 52
    assert Bag.get_item_priority("F") == 32


def test_get_groups() -> None:
    bags = [
        Bag("aaa", "abc"),
        Bag("aaa", "ABC"),
        Bag("aaa", "ZYX"),
        Bag("L", "M"),
        Bag("M", "L"),
        Bag("X", "L"),
    ]
    expected_groups = {
        "A": [Bag("A", "B"), Bag("B", "A"), Bag("A", "Z")],
        "l": [Bag("lll", "LLL"), Bag("abc", "lmn"), Bag("zYx", "lLa")],
    }
    bags = [bag for group in expected_groups.values() for bag in group]
    assert Bag.sort_into_groups(bags) == expected_groups


def test_part_1(bags_test_data: list[Bag]) -> None:
    total_priority = day_03.part_1(bags_test_data)
    assert total_priority == 157


def test_part_2(bags_test_data: list[Bag]) -> None:
    total_priority = day_03.part_2(bags_test_data)
    assert total_priority == 70

    # Run with duplicate bags, testing that the items can handle having
    # multiple groups for them. Priority should be double.
    total_priority = day_03.part_2(bags_test_data * 2)
    assert total_priority == 70 * 2
