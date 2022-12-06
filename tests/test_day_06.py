from __future__ import annotations

import os
import sys

import pytest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(REPO_ROOT)

from days import day_06


@pytest.fixture
def parsed_test_data() -> str:
    with open(os.path.join(REPO_ROOT, "data", "day_06_test.txt")) as f:
        return f.read().strip()


def test_part_1(parsed_test_data: str) -> None:
    assert day_06.part_1(parsed_test_data) == 7
    assert day_06.part_1("abcd") == 4
    assert day_06.part_1("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
    assert day_06.part_1("nppdvjthqldpwncqszvftbrmjlhg") == 6
    assert day_06.part_1("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
    assert day_06.part_1("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11


def test_part_2(parsed_test_data: str) -> None:
    assert day_06.part_2(parsed_test_data) == 19
    assert day_06.part_2("abcdefghijklmn") == 14
    assert day_06.part_2("bvwbjplbgvbhsrlpgdmjqwftvncz") == 23
    assert day_06.part_2("nppdvjthqldpwncqszvftbrmjlhg") == 23
    assert day_06.part_2("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 29
    assert day_06.part_2("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 26
