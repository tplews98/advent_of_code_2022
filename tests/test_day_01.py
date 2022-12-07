from __future__ import annotations

import os
import sys

import pytest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(REPO_ROOT)

from days import day_01


@pytest.fixture
def bundles_test_data() -> list[list[int]]:
    with open(os.path.join(REPO_ROOT, "data", "day_01_test.txt")) as f:
        return day_01.parse_text_into_bundles(f.read().splitlines())


def test_parse() -> None:
    lines = ["1", "", "2", "4", "9", "", "16", "1234"]
    expected_bundles = [[1], [2, 4, 9], [16, 1234]]
    bundles = day_01.parse_text_into_bundles(lines)
    assert bundles == expected_bundles


def test_part_1(bundles_test_data: list[list[int]]) -> None:
    result = day_01.part_1(bundles_test_data)
    assert result == 24000


def test_part_2(bundles_test_data: list[list[int]]) -> None:
    result = day_01.part_2(bundles_test_data)
    assert result == 45000
