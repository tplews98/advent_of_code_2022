from __future__ import annotations

import sys


def _find_idx_after_uniq_chars(data: str, num_uniq_chars: int) -> int:
    for idx in range(num_uniq_chars - 1, len(data)):
        if (
            len(set(data[idx - num_uniq_chars + 1 : idx + 1]))
            == num_uniq_chars
        ):
            # Last `num_uniq_chars` chars are different, return idx + 1 for
            # index after.
            return idx + 1
    raise Exception(
        f"Could not find {num_uniq_chars} consecutive unique chars"
    )


def part_1(data: str) -> int:
    # Start of packet has 4 unique chars.
    return _find_idx_after_uniq_chars(data, 4)


def part_2(data: str) -> int:
    # Start of message has 14 unique chars.
    return _find_idx_after_uniq_chars(data, 14)


def main(args: list[str]) -> None:
    data_file = args[0]
    with open(data_file) as f:
        data = f.read().strip()

    print(f"Part 1: Number of characters before first packet = {part_1(data)}")
    print(
        f"Part 2: Number of characters before first message = {part_2(data)}"
    )


if __name__ == "__main__":
    main(sys.argv[1:])
