from __future__ import annotations

import sys
import textwrap
from dataclasses import (
    dataclass,
    field,
)
from typing import (
    Iterable,
    Optional,
)


@dataclass
class Directory:
    name: str
    parent: Optional[Directory] = None
    directories: list[Directory] = field(default_factory=list)
    files: list[File] = field(default_factory=list)

    @classmethod
    def from_line(cls, line: str, curr_dir: Directory) -> Directory:
        return cls(line.removeprefix("dir "), curr_dir)

    def parse_ls_output_and_update(self, output: Iterable[str]) -> None:
        for line in output:
            if line.startswith("dir "):
                # Line is a directory. Parse it and add to list (if not already in).
                new_dir = Directory.from_line(line, self)
                if not any(d.name == new_dir.name for d in self.directories):
                    self.directories.append(new_dir)
            else:
                # Line is a file. Parse it and add to list (if not already in).
                new_file = File.from_line(line, self)
                if not any(f.name == new_file.name for f in self.files):
                    self.files.append(new_file)

    def find_size(self) -> int:
        size = 0
        size += sum(sub_dir.find_size() for sub_dir in self.directories)
        size += sum(file.size for file in self.files)
        return size

    def get_directory_tree_str(self) -> str:
        lines = [f"- {self.name} (dir)"]
        # Ignore mypy error for combining directories and files list,
        # intentionally doing this. The only thing that matters is they both
        # have a `name` attribute and `get_directory_tree_str` method.
        sub_dirs_and_files = sorted(
            self.directories + self.files, key=lambda thing: thing.name  # type: ignore[operator]
        )
        for sub_dir_or_file in sub_dirs_and_files:
            sub_dir_tree_str = sub_dir_or_file.get_directory_tree_str()
            # Indent the subtree and add to list.
            lines.append(textwrap.indent(sub_dir_tree_str, "  "))
        return "\n".join(lines)


@dataclass
class File:
    name: str
    size: int
    parent: Directory

    @classmethod
    def from_line(cls, line: str, curr_dir: Directory) -> File:
        size_str, name = line.split()
        return cls(name, int(size_str), curr_dir)

    def get_directory_tree_str(self) -> str:
        return f"- {self.name} (file, size={self.size})"


def parse_text_into_fs(lines: list[str]) -> Directory:
    idx = 0

    # First line should always be "$ cd /"
    assert lines[0] == "$ cd /"
    root_dir = Directory("/")
    curr_dir = root_dir
    idx += 1

    while idx < len(lines):
        line = lines[idx]
        # Should always be parsing the next command
        assert line.startswith("$")
        if line == "$ cd ..":
            # Changing directory to parent.
            assert curr_dir.parent is not None
            curr_dir = curr_dir.parent
            idx += 1
        elif line.startswith("$ cd"):
            # Changing directory, should only be one match,
            matching_dir = [
                d
                for d in curr_dir.directories
                if line.removeprefix("$ cd ") == d.name
            ]
            assert len(matching_dir) == 1
            curr_dir = matching_dir[0]
            idx += 1
        elif line == "$ ls":
            # List a directory. Find the end of the output (where next $ is)
            # and then parse it.
            new_idx = idx + 1
            while new_idx < len(lines) and not lines[new_idx].startswith("$"):
                new_idx += 1
            # Found end of output, parse the contents of the dir.
            curr_dir.parse_ls_output_and_update(lines[idx + 1 : new_idx])
            idx = new_idx
        else:
            raise NotImplementedError(f"Unknown command '{line}'")

    return root_dir


def get_all_sub_dirs(root_dir: Directory) -> list[Directory]:
    directories: list[Directory] = []
    directories.extend(root_dir.directories)
    for sub_dir in root_dir.directories:
        directories.extend(get_all_sub_dirs(sub_dir))
    return directories


def part_1(root_dir: Directory) -> int:
    all_directories = get_all_sub_dirs(root_dir) + [root_dir]
    return sum(
        directory.find_size()
        for directory in all_directories
        if directory.find_size() < 100000
    )


def part_2(root_dir: Directory) -> int:
    root_dir_size = root_dir.find_size()
    space_needed_to_delete = 30000000 - 70000000 + root_dir_size
    if space_needed_to_delete > root_dir_size:
        raise Exception("Not possible to delete enough free up required space")

    smallest_size_dir_to_delete = root_dir_size
    for directory in get_all_sub_dirs(root_dir):
        dir_size = directory.find_size()
        # If the directory has a size big enough to free up required space if
        # deleted and is smaller than the current smallest, set it to be the
        # current smallest.
        if space_needed_to_delete <= dir_size < smallest_size_dir_to_delete:
            smallest_size_dir_to_delete = dir_size

    return smallest_size_dir_to_delete


def main(args: list[str]) -> None:
    data_file = args[0]
    with open(data_file) as f:
        root_dir = parse_text_into_fs(f.read().splitlines())

    print(f"Part 1: Size of dirs < 100000 = {part_1(root_dir)}")
    print(f"Part 2: Smallest dir size to delete = {part_2(root_dir)}")


if __name__ == "__main__":
    main(sys.argv[1:])
