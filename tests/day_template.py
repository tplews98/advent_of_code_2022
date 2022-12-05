from __future__ import annotations

import os
import sys
from typing import Any

import pytest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(REPO_ROOT)

from days import day_template


@pytest.fixture
def parsed_test_data() -> Any:
    with open(os.path.join(REPO_ROOT, "data", "day_template_test.txt")) as f:
        return day_template.parse_text(f.read().splitlines())


def test_parse() -> None:
    lines: Any = []
    expected_parsed_data: Any = []
    parsed_data = day_template.parse_text(lines)
    assert parsed_data == expected_parsed_data


def test_part_1(parsed_test_data: Any) -> None:
    expected_part_1_ans = 0
    part_1_ans = day_template.part_1(parsed_test_data)
    assert part_1_ans == expected_part_1_ans


def test_part_2(parsed_test_data: Any) -> None:
    expected_part_2_ans = 0
    part_2_ans = day_template.part_2(parsed_test_data)
    assert part_2_ans == expected_part_2_ans
