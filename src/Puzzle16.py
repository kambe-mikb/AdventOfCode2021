#!/usr/bin/env python,
"""
--- Day 8: Seven Segment Search ---
You barely reach the safety of the cave when the whale smashes into the cave
mouth, collapsing it. Sensors indicate another exit to this cave at a much
greater depth, so you have no choice but to press on.

As your submarine slowly makes its way through the cave system, you notice that
the four-digit seven-segment displays in your submarine are malfunctioning;
they must have been damaged during the escape. You'll be in a lot of trouble
without them, so you'd better figure out what's wrong.

Each digit of a seven-segment display is rendered by turning on or off any of
seven segments named a through g:

  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg
So, to render a 1, only segments c and f would be turned on; the rest would be
off. To render a 7, only segments a, c, and f would be turned on.

The problem is that the signals which control the segments have been mixed up
on each display. The submarine is still trying to display numbers by producing
output on signal wires a through g, but those wires are connected to segments
randomly. Worse, the wire/segment connections are mixed up separately for each
four-digit display! (All of the digits within a display use the same
connections, though.)

So, you might know that only signal wires b and g are turned on, but that
doesn't mean segments b and g are turned on: the only digit that uses two
segments is 1, so it must mean segments c and f are meant to be on. With just
that information, you still can't tell which wire (b/g) goes to which segment
(c/f). For that, you'll need to collect more information.

For each display, you watch the changing signals for a while, make a note of
all ten unique signal patterns you see, and then write down a single four digit
output value (your puzzle input). Using the signal patterns, you should be able
to work out which pattern corresponds to which digit.

For example, here is what you might see in a single entry in your notes:

acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
cdfeb fcadb cdfeb cdbaf
(The entry is wrapped here to two lines so it fits; in your notes, it will all
be on a single line.)

Each entry consists of ten unique signal patterns, a | delimiter, and finally
the four digit output value. Within an entry, the same wire/segment connections
are used (but you don't know what the connections actually are). The unique
signal patterns correspond to the ten different ways the submarine tries to
render a digit using the current wire/segment connections. Because 7 is the
only digit that uses three segments, dab in the above example means that to
render a 7, signal lines d, a, and b are on. Because 4 is the only digit that
uses four segments, eafb means that to render a 4, signal lines e, a, f, and b
are on.

Using this information, you should be able to work out which combination of
signal wires corresponds to each of the ten digits. Then, you can decode the
four digit output value. Unfortunately, in the above example, all of the digits
in the output value (cdfeb fcadb cdfeb cdbaf) use five segments and are more
difficult to deduce.

For now, focus on the easy digits. Consider this larger example:

be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb |
fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec |
fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef |
cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega |
efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga |
gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf |
gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf |
cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd |
ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg |
gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc |
fgae cfgab fg bagce
Because the digits 1, 4, 7, and 8 each use a unique number of segments, you
should be able to tell which combinations of signals correspond to those
digits.Counting only digits in the output values (the part after | on each
line), in the above example, there are 26 instances of digits that use a unique
number of segments (highlighted above).

In the output values, how many times do digits 1, 4, 7, or 8 appear?

352

Through a little deduction, you should now be able to determine the remaining
digits. Consider again the first example above:

acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
cdfeb fcadb cdfeb cdbaf
After some careful analysis, the mapping between signal wires and segments only
make sense in the following configuration:

 dddd
e    a
e    a
 ffff
g    b
g    b
 cccc
So, the unique signal patterns would correspond to the following digits:

acedgfb: 8
cdfbe: 5
gcdfa: 2
fbcad: 3
dab: 7
cefabd: 9
cdfgeb: 6
eafb: 4
cagedb: 0
ab: 1
Then, the four digits of the output value can be decoded:

cdfeb: 5
fcadb: 3
cdfeb: 5
cdbaf: 3
Therefore, the output value for this entry is 5353.

Following this same process for each entry in the second, larger example above,
the output value of each entry can be determined:

fdgacbe cefdb cefbgd gcbe: 8394
fcgedb cgb dgebacf gc: 9781
cg cg fdcagb cbg: 1197
efabcd cedba gadfec cb: 9361
gecf egdcabf bgf bfgea: 4873
gebdcfa ecba ca fadegcb: 8418
cefg dcbef fcge gbcadfe: 4548
ed bcgafe cdgba cbgef: 1625
gbdfcae bgc cg cgb: 8717
fgae cfgab fg bagce: 4315
Adding all of the output values in this larger example produces 61229.

For each entry, determine all of the wire/segment connections and decode the
four-digit output values. What do you get if you add up all of the output
values?

Adding all of the output values produces 936117
"""
import functools
import itertools
import operator
import typing as T

__author__ = "kambe-mikb"
__all__ = ["getInput"]


def getInput(infile: str) -> T.Generator:
    return (v.rstrip("\n") for v in open(infile, "r", encoding="utf-8"))


EXAMPLE_INPUT1 = [
    "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |"
    " cdfeb fcadb cdfeb cdbaf",
    ]
EXAMPLE_INPUT2 = [
    "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb |"
    " fdgacbe cefdb cefbgd gcbe",
    "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec |"
    " fcgedb cgb dgebacf gc",
    "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef |"
    " cg cg fdcagb cbg",
    "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega |"
    " efabcd cedba gadfec cb",
    "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga |"
    " gecf egdcabf bgf bfgea",
    "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf |"
    " gebdcfa ecba ca fadegcb",
    "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf |"
    " cefg dcbef fcge gbcadfe",
    "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd |"
    " ed bcgafe cdgba cbgef",
    "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg |"
    " gbdfcae bgc cg cgb",
    "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc |"
    " fgae cfgab fg bagce",
    ]


DIGITS = [
    set(("a", "b", "c", "e", "f", "g")),  # 0
    set(("c", "f")),  # 1
    set(("a", "c", "d", "e", "g")),  # 2
    set(("a", "c", "d", "f", "g")),  # 3
    set(("b", "c", "d", "f")),  # 4
    set(("a", "b", "d", "f", "g")),  # 5
    set(("a", "b", "d", "e", "f", "g")),  # 6
    set(("a", "c", "f")),  # 7
    set(("a", "b", "c", "d", "e", "f", "g")),  # 8
    set(("a", "b", "c", "d", "f", "g"))  # 9
    ]


if __name__ == "__main__":
    digit_lens = (
        len(DIGITS[1]), len(DIGITS[4]), len(DIGITS[7]), len(DIGITS[8])
        )
    segment_strings = [
        u.split()
        for l in getInput("Day08-input.txt")
        for u in l.split(" | ")
        ]
    input_string_list = itertools.compress(
        segment_strings, itertools.cycle([True, False])
        )
    output_string_list = itertools.compress(
        segment_strings, itertools.cycle([False, True])
        )
    total = 0
    for input_strings, output_strings in zip(
            input_string_list, output_string_list
            ):
        segment = {}
        input_sets = [{d for d in s} for s in input_strings]
        input_lens = [len(s) for s in input_sets]
        digit7 = input_sets[input_lens.index(3)]
        digit1 = input_sets[input_lens.index(2)]
        digit4 = input_sets[input_lens.index(4)]
        digit8 = input_sets[input_lens.index(7)]
        segment["a"] = digit7 - digit1
        t1 = functools.reduce(
            lambda x, y: x & y,
            (
                input_sets[i]
                for i in range(len(input_lens))
                if input_lens[i] == 5
                )
            )
        segment["d"] = t1 & digit4
        segment["b"] = digit4 - digit1 - segment["d"]
        segment["g"] = t1 - segment["a"] - segment["d"]
        t2 = functools.reduce(
            lambda x, y: x & y,
            (
                input_sets[i]
                for i in range(len(input_lens))
                if input_lens[i] == 6
                )
            )
        segment["f"] = t2 - segment["a"] - segment["b"] - segment["g"]
        segment["c"] = digit1 - segment["f"]
        segment["e"] = digit8 - functools.reduce(
            lambda x, y: x | y, segment.values()
            )
        segment_map = {list(k).pop(): v for v, k in segment.items()}
        translation = str.maketrans(segment_map)
        output_sets = [
            {d for d in s.translate(translation)} for s in output_strings
            ]
        for output_set in output_sets:
            if output_set not in DIGITS:
                raise ValueError(f"{output_set} not in {DIGITS}")
        print(
            " ".join(output_strings)
            + ": "
            + "".join(
                (str(DIGITS.index(output_set)) for output_set in output_sets)
                )
            )
        total += functools.reduce(
            lambda x, y: x * 10 + y,
            (DIGITS.index(output_set) for output_set in output_sets)
            )
    print(f"\nAdding all of the output values produces {total}")
