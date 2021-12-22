#!/usr/bin/env python,
"""
--- Day 5: Hydrothermal Venture ---
You come across a field of hydrothermal vents on the ocean floor! These vents
constantly produce large, opaque clouds, so it would be best to avoid them if
possible.

They tend to form in lines; the submarine helpfully produces a list of nearby
lines of vents (your puzzle input) for you to review. For example:

0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2

Each line of vents is given as a line segment in the format x1,y1 -> x2,y2
where x1,y1 are the coordinates of one end the line segment and x2,y2 are the
coordinates of the other end. These line segments include the points at both
ends. In other words:

An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.
For now, only consider horizontal and vertical lines: lines where either
x1 = x2 or y1 = y2.

So, the horizontal and vertical lines from the above list would produce the
following diagram:

.......1..
..1....1..
..1....1..
.......1..
.112111211
..........
..........
..........
..........
222111....
In this diagram, the top left corner is 0,0 and the bottom right corner is 9,9.
Each position is shown as the number of lines which cover that point or . if no
line covers that point. The top-left pair of 1s, for example, comes from
2,2 -> 2,1; the very bottom row is formed by the overlapping lines
0,9 -> 5,9 and 0,9 -> 2,9.

To avoid the most dangerous areas, you need to determine the number of points
where at least two lines overlap. In the above example, this is anywhere in the
diagram with a 2 or larger - a total of 5 points.

Consider only horizontal and vertical lines. At how many points do at least two
lines overlap?

"""
import collections
import math
import typing as T

__author__ = "kambe-mikb"
__all__ = ["getInput"]


def getInput(infile: str) -> T.Generator:
    return (v.rstrip("\n") for v in open(infile, "r", encoding="utf-8"))


Point = collections.namedtuple("Point", ["x", "y"])


if __name__ == "__main__":
    input = [
        "0,9 -> 5,9",
        "8,0 -> 0,8",
        "9,4 -> 3,4",
        "2,2 -> 2,1",
        "7,0 -> 7,4",
        "6,4 -> 2,0",
        "0,9 -> 2,9",
        "3,4 -> 1,4",
        "0,0 -> 8,8",
        "5,5 -> 8,2",
        ]
    # input = [*getInput("Day04-input.txt")]

    maxval = 0
    points = []
    for line in input:
        start_s, stop_s = line.split(" -> ")
        startx_s, starty_s = start_s.split(",")
        stopx_s, stopy_s = stop_s.split(",")
        startx = int(startx_s)
        starty = int(starty_s)
        stopx = int(stopx_s)
        stopy = int(stopy_s)

        # Only consider vertical or horizontal lines
        if not(startx == stopx or starty == stopy):
            continue

        maxval = max(maxval, startx, starty, stopx, stopy)
        points.append((Point(startx, starty), Point(stopx, stopy)))

    dimension = pow(10, math.ceil(math.log10(maxval)))
    vent_map = [[0] * dimension for r in range(dimension)]
    for start, stop in points:
        if start.y == stop.y:  # horizontal line
            for col in range(min(start.x, stop.x), max(start.x, stop.x) + 1):
                vent_map[start.y][col] += 1
        elif start.x == stop.x:  # vertical line
            for row in range(min(start.y, stop.y), max(start.y, stop.y) + 1):
                vent_map[row][start.x] += 1

    danger_count = 0
    for y in vent_map:
        print("".join([(f"{x}" if x else ".") for x in y]))
        danger_count += len(y) - y.count(0) - y.count(1)

    print(f"\nCount of dangerous points: {danger_count}")
