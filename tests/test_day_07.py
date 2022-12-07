from __future__ import annotations

import os
import sys

import pytest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(REPO_ROOT)

from days import day_07
from days.day_07 import Directory


@pytest.fixture
def parsed_test_root_dir() -> Directory:
    with open(os.path.join(REPO_ROOT, "data", "day_07_test.txt")) as f:
        return day_07.parse_text_into_fs(f.read().splitlines())


def test_get_directory_tree_str(parsed_test_root_dir: Directory) -> None:
    expected_str = """\
- / (dir)
  - a (dir)
    - e (dir)
      - i (file, size=584)
    - f (file, size=29116)
    - g (file, size=2557)
    - h.lst (file, size=62596)
  - b.txt (file, size=14848514)
  - c.dat (file, size=8504156)
  - d (dir)
    - d.ext (file, size=5626152)
    - d.log (file, size=8033020)
    - j (file, size=4060174)
    - k (file, size=7214296)\
"""
    assert parsed_test_root_dir.get_directory_tree_str() == expected_str


def test_part_1(parsed_test_root_dir: Directory) -> None:
    part_1_ans = day_07.part_1(parsed_test_root_dir)
    assert part_1_ans == 95437


def test_part_2(parsed_test_root_dir: Directory) -> None:
    part_2_ans = day_07.part_2(parsed_test_root_dir)
    assert part_2_ans == 24933642
