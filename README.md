# Advent of Code

My Python solutions to [Advent of Code](https://adventofcode.com), 2015-2016.

## Progress

| Year | Status |
|------|--------|
| 2015 | Days 1-21 and 23 complete (both parts), Day 25 part 1 |
| 2016 | Days 1-9 complete (both parts) |

More coming as I solve them.

## Layout

```
2015/
  Day1/
    part1.py
    part2.py
    test        <- your puzzle input (not in the repo)
  Day2/
  ...
2016/
  Day1/
  ...
```

Each day has a `part1.py` and `part2.py`.

## Running a solution

Requires Python 3.9 or newer. Run scripts from the **root** of the repo, because they open their input files using paths like `2016/Day9/test`:

```
python 2016/Day9/part1.py
```

## Puzzle inputs

Following the Advent of Code rules, this repo doesn't include puzzle text or personal puzzle inputs. To run a solution, download your own input from the puzzle's page and save it as a file named `test` in that day's folder.

A few days work differently:

- **2015 Day 19:** put the replacement rules in `test` and the molecule string in a separate file named `molecule`.
- **2015 Day 21:** put your boss stats in a file named `boss_stat`, in the same three-line format as the puzzle ("Hit Points: ...", "Damage: ...", "Armor: ...").
- **2015 Day 11 part 2:** asks for your part 1 answer when you run it.
- **Days where the input is a short string or number** (2015 Days 10, 11 part 1, 20, 25; 2016 Day 5): put it in `test` as plain text.

## Note

Puzzles and inputs belong to Advent of Code (Eric Wastl). Only my own solution code is in this repo.