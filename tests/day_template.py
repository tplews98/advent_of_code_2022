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
    assert day_template.part_1(parsed_test_data) == 0


def test_part_2(parsed_test_data: Any) -> None:
    assert day_template.part_2(parsed_test_data) == 0
