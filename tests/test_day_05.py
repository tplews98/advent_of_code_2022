from __future__ import annotations

import os
import sys

import pytest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(REPO_ROOT)

from days import day_05
from days.day_05 import Move


@pytest.fixture
def parsed_test_data() -> tuple[list[list[str]], list[Move]]:
    with open(os.path.join(REPO_ROOT, "data", "day_05_test.txt")) as f:
        return day_05.parse_text_into_stacks_and_moves(f.read().splitlines())


def test_parse() -> None:
    lines = [
        "[A] [B]        ",
        "[D] [E] [F]    ",
        "[G] [H] [I] [J]",
        " 1   2   3   4 ",
        "",
        "move 2 from 1 to 2",
        "move 1 from 4 to 3",
        "move 4 from 2 to 1",
    ]
    expected_stacks = [["G", "D", "A"], ["H", "E", "B"], ["I", "F"], ["J"]]
    expected_moves = [Move(2, 1, 2), Move(1, 4, 3), Move(4, 2, 1)]
    stacks, moves = day_05.parse_text_into_stacks_and_moves(lines)
    assert stacks == expected_stacks
    assert moves == expected_moves


def test_stacks_to_str() -> None:
    stacks = [["G", "D", "A"], ["H", "E", "B"], ["I", "F"], ["J"]]
    expected_str = "\n".join(
        [
            "[A] [B]        ",
            "[D] [E] [F]    ",
            "[G] [H] [I] [J]",
            " 1   2   3   4 ",
        ]
    )
    assert day_05.stacks_to_str(stacks) == expected_str


def test_part_1(parsed_test_data: tuple[list[list[str]], list[Move]]) -> None:
    expected_top_stacks = "CMZ"
    top_stacks = day_05.part_1(*parsed_test_data)
    assert top_stacks == expected_top_stacks


def test_part_2(parsed_test_data: tuple[list[list[str]], list[Move]]) -> None:
    expected_top_stacks = "MCD"
    top_stacks = day_05.part_2(*parsed_test_data)
    assert top_stacks == expected_top_stacks
