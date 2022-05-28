# -*- coding: utf-8 -*-
"""
@file    pair_gen.py
@author  Benjamin Foreman (bennyforeman1@gmail.com)
@date    2022-05-27

This program generates all sets of round robin pairings from a given list.

Usage:
    pair_gen.py [-h] [-o [OUTFILE]] [infile]

    positional arguments:
    infile                The input file.

    optional arguments:
    -h, --help            show this help message and exit
    -o [OUTFILE], --outfile [OUTFILE]
                            The output file.

Input file format:
    One item per line.

    Example:
        sally
        bob
        jane

Output file format:
    --- Pairing Set 1 ---
        sally - bob
        jane - None

    --- Pairing Set 2 ---
        sally - jane
        None - bob

    --- Pairing Set 3 ---
        sally - None
        jane - sally

Todo:
    - Add unit tests
    - Add options for output file formatting
"""

import argparse as ap
import sys


def split_at_index(arr, index):
    """
    This function splits an array at a given index and returns the splits.

    Args:
        arr (list): A list of items to split.
        index (int): The index to split at.

    Returns:
        list: A list of items split at a given index.

    Example:
        >>> split_at_index(["a", "b", "c", "d"], 1)
        (['a', 'b'], ['c', 'd'])
    """

    return arr[:index], arr[index:]


def generate_rotations(arr):
    """
    This function generates all rotations of an array.

    Args:
        arr (list): A list of items to rotate.

    Yields:
        list: Rotation of the given array.

    Example:
        >>> list(generate_rotations(["a", "b", "c", "d"]))
        [
            ['a', 'b', 'c', 'd'],
            ['b', 'c', 'd', 'a'],
            ['c', 'd', 'a', 'b'],
            ['d', 'a', 'b', 'c']
        ]
    """

    for pivot in range(len(arr)):
        yield arr[pivot:] + arr[:pivot]


def generate_pairings(items):
    """
    This function generates all sets of unique pairings of items in a list.

    Args:
        items (list): A list of items to pair.

    Yields:
        list: Unique set of pairings.

    Example:
        >>> list(generate_pairings(["sally", "bob", "jane"]))
        [
            [('sally', 'bob'), ('jane', 'None')],
            [('sally', 'jane'), ('None', 'bob')],
            [('sally', 'None'), ('jane', 'sally')]
        ]

    See Also:
        https://en.wikipedia.org/wiki/Round-robin_tournament#Scheduling_algorithm
    """

    if len(items) % 2 != 0:
        items.append(None)

    fixed, others = items[0], items[1:]

    for schedule in ([fixed, *rotation] for rotation in generate_rotations(others)):
        row1, row2 = split_at_index(schedule, len(schedule) // 2)

        yield list(zip(row1, reversed(row2)))


def main():
    parser = ap.ArgumentParser(
        description="This program generates all sets of round robin pairings from a given list.",
    )
    parser.add_argument(
        "infile",
        nargs="?",
        type=ap.FileType("r"),
        help="The input file.",
        default=None if sys.stdin.isatty() else sys.stdin,
    )
    parser.add_argument(
        "-o",
        "--outfile",
        nargs="?",
        type=ap.FileType("w"),
        help="The output file.",
        default=sys.stdout,
    )
    args = parser.parse_args()

    # check for no input
    if args.infile is None:
        parser.print_help()
        return

    items = [line.strip() for line in args.infile]

    padding_len = max(len(item) for item in items)

    for i, pairing_set in enumerate(generate_pairings(items), 1):
        header = f"--- Pairing Set {i} ---\n"
        args.outfile.write(header.rjust(padding_len + len(header) // 2 + 2))

        for a, b in pairing_set:
            args.outfile.write(f"{str(a).rjust(padding_len)} - {b}\n")

        # add a newline between each pairing set
        args.outfile.write("\n" * (i != len(items) - 1))


if __name__ == "__main__":
    main()
