#!/usr/bin/env python,
"""
"""
import typing as T

__author__ = "kambe-mikb"
__all__ = ["getInput"]


def getInput(infile: str) -> T.Generator:
    return (v.rstrip("\n") for v in open(infile, "r", encoding="utf-8"))


if __name__ == "__main__":
    # NUMBER_OF_DAYS = 80
    # input = [*getInput("Day06-input.txt")]
    NUMBER_OF_DAYS = 18
    input = ["3,4,3,1,2"]

    fishes = [int(i) for line in input for i in line.split(",")]
    print(f"Initial state: {','.join((str(fish) for fish in fishes))}")

    for day in range(1, NUMBER_OF_DAYS + 1):
        days = "days:" if day > 1 else "day: "
        new_fishes = []
        for index, fish in enumerate(fishes):
            if fish > 0:
                fishes[index] -= 1
            else:
                fishes[index] = 6
                new_fishes.append(8)
        fishes.extend(new_fishes)
        print(
            f"After {day: >2d} {days} {','.join((str(fish) for fish in fishes))}"
            )

    print(f"\nNumber of fish after {NUMBER_OF_DAYS} {days} {len(fishes)}")
