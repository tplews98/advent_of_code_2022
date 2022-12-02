import os
import sys

import pytest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(REPO_ROOT)

from days import day_02
from days.day_02 import Symbol


@pytest.fixture
def rounds_test_data() -> list[tuple[Symbol, str]]:
    with open(os.path.join(REPO_ROOT, "data", "day_02_test.txt")) as f:
        return day_02.parse_text_into_rounds(f.readlines())


def test_parse() -> None:
    lines = [l + "\n" for l in ("A X", "B X", "C Y", "B Z")]
    expected_rounds = [
        (Symbol.ROCK, "X"),
        (Symbol.PAPER, "X"),
        (Symbol.SCISSORS, "Y"),
        (Symbol.PAPER, "Z"),
    ]
    rounds = day_02.parse_text_into_rounds(lines)
    assert rounds == expected_rounds


def test_round_results() -> None:
    rounds = [
        (Symbol.ROCK, "X", 4),
        (Symbol.ROCK, "Y", 8),
        (Symbol.ROCK, "Z", 3),
        (Symbol.PAPER, "X", 1),
        (Symbol.PAPER, "Y", 5),
        (Symbol.PAPER, "Z", 9),
        (Symbol.SCISSORS, "X", 7),
        (Symbol.SCISSORS, "Y", 2),
        (Symbol.SCISSORS, "Z", 6),
    ]
    for first, second, expected_points in rounds:
        points = Symbol.round_result_part_1(first, second)
        assert points == expected_points


def test_part_1(rounds_test_data: list[tuple[Symbol, str]]) -> None:
    points = day_02.part_1(rounds_test_data)
    assert points == 15


def test_part_2(rounds_test_data: list[tuple[Symbol, str]]) -> None:
    points = day_02.part_2(rounds_test_data)
    assert points == 12
