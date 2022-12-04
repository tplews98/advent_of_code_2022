import os
import sys

import pytest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(REPO_ROOT)

from days import day_04
from days.day_04 import SectionAssignment


@pytest.fixture
def assignments_test_data() -> list[
    tuple[SectionAssignment, SectionAssignment]
]:
    with open(os.path.join(REPO_ROOT, "data", "day_04_test.txt")) as f:
        return day_04.parse_text_into_assignment_pairs(f.read().splitlines())


def test_parse() -> None:
    lines = ["1-1,2-2", "1-1001,5-9", "7-9,3-3"]
    expected_assignment_pairs = [
        (SectionAssignment(1, 1), SectionAssignment(2, 2)),
        (SectionAssignment(1, 1001), SectionAssignment(5, 9)),
        (SectionAssignment(7, 9), SectionAssignment(3, 3)),
    ]
    assignment_pairs = day_04.parse_text_into_assignment_pairs(lines)
    assert assignment_pairs == expected_assignment_pairs


def test_overlapping_pairs() -> None:
    assignment_pairs = [
        [(SectionAssignment(1, 1), SectionAssignment(2, 2)), False, False],
        [(SectionAssignment(1, 2), SectionAssignment(2, 2)), True, True],
        [(SectionAssignment(1, 2), SectionAssignment(2, 3)), False, True],
        [(SectionAssignment(5, 9), SectionAssignment(6, 7)), True, True],
    ]
    for pair, complete_overlap, partial_overlap in assignment_pairs:
        assert (
            SectionAssignment.does_pair_overlap_completely(pair)
            == complete_overlap
        )
        assert (
            SectionAssignment.does_pair_overlap_partially(pair)
            == partial_overlap
        )


def test_part_1(
    assignments_test_data: list[tuple[SectionAssignment, SectionAssignment]]
) -> None:
    total_complete_overlaps = day_04.part_1(assignments_test_data)
    assert total_complete_overlaps == 2


def test_part_2(
    assignments_test_data: list[tuple[SectionAssignment, SectionAssignment]]
) -> None:
    total_overlaps = day_04.part_2(assignments_test_data)
    assert total_overlaps == 4
