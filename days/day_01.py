#!/usr/bin/env python3.11

import sys


def parse_text_into_bundles(lines: list[str]) -> list[list[int]]:
    bundles: list[list[int]] = []
    current_bundle = []
    for line in lines:
        line = line.strip()
        if line:
            # Part of same bundle.
            current_bundle.append(int(line))
        elif current_bundle:
            # Current line is empty so bundle has finished, add it to list and
            # reset current bundle.
            bundles.append(current_bundle)
            current_bundle = []

    # Add final bundle if there was no newline at end of file.
    if current_bundle:
        bundles.append(current_bundle)

    return bundles


def part_1(bundles: list[list[int]]) -> int:
    max_calories_in_bundles = max(sum(bundle) for bundle in bundles)
    return max_calories_in_bundles


def part_2(bundles: list[list[int]]) -> int:
    sorted_bundles = sorted(
        bundles, key=lambda bundle: sum(bundle), reverse=True
    )
    top_3_bundle_sum = sum(sum(bundle) for bundle in sorted_bundles[:3])
    return top_3_bundle_sum


def main(args: list[str]) -> None:
    data_file = args[0]
    with open(data_file) as f:
        bundles = parse_text_into_bundles(f.readlines())

    print(f"Part 1: Max calories in bundle: {part_1(bundles)}")
    print(f"Part 2: Calories in top 3 bundles: {part_2(bundles)}")


if __name__ == "__main__":
    main(sys.argv[1:])
