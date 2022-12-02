# Python Advent of Code 2021

My attempt at [Advent of Code 2022](https://adventofcode.com/2022/) using
Python.

All solution code should be put in `days`. The filename for each day should be
`day_xx.py`.

All input should be put in `data`. The filename for the real input of each day
should be `day_xx_input.txt`, and test input `day_xx_test_input.txt`.

Taskfile commands:

- `run-day <day>`: Run a given day
- `run-test <day>`: Run the tests for a given day
- `run-all-days`: Run all days that have solutions
- `run-all-tests`: Run all the tests for days which have solutions
- `run-mypy`: Run mypy on all days and tests
- `autoformat`: Autoformat python code with black and isort.

python3.9 or greater is required due the typing used. Change the `PYTHON_EXE`
variable in `Taskfile` to run with a different executable than the default.
