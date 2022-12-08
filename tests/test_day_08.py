from __future__ import annotations

import os
import sys

import pytest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(REPO_ROOT)

from days import day_08
from days.day_08 import Grid


@pytest.fixture
def parsed_test_data() -> Grid:
    with open(os.path.join(REPO_ROOT, "data", "day_08_test.txt")) as f:
        return Grid.from_lines(f.read().splitlines())


def test_part_1(parsed_test_data: Grid) -> None:
    assert day_08.part_1(parsed_test_data) == 21


def test_part_2(parsed_test_data: Grid) -> None:
    assert day_08.part_2(parsed_test_data) == 8
