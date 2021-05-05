#! /usr/bin/env python3


import sys
from argparse import ArgumentParser
from os.path import basename


CMD = sys.argv[0]


def parse_arguments():
    parser = ArgumentParser(basename(CMD))

    parser.add_argument('-c', '--col', required=False, action='store', type=int, default=0,
        dest='col', help='zero-indexed column to filter on, defaults to 0', metavar='IDX')

    parser.add_argument('-H', '--skip-header', required=False, action='store_true',
        dest='skip_header', help='skip the first line (e.g. used for headers)')

    parser.add_argument('-s', '--sep', required=False, action='store', type=str,
        dest='separator', help='separator string, defaults to ","', metavar='SEP', default=',')

    parser.add_argument('-l', '--leq', required=False, action='store', type=float,
        dest='max', help='only print values less than or equal to this value', metavar='VAL')

    parser.add_argument('-L', '--lt', required=False, action='store', type=float,
        dest='maxopen', help='only print values less than this value', metavar='VAL')

    parser.add_argument('-g', '--geq', required=False, action='store', type=float,
        dest='min', help='only print values greater than or equal to this value', metavar='VAL')

    parser.add_argument('-G', '--gt', required=False, action='store', type=float,
        dest='minopen', help='only print values greater than this value', metavar='VAL')

    parsed = vars(parser.parse_args())

    separator = parsed['separator']
    skip_header = parsed['skip_header']
    col = parsed['col']
    maxval = parsed['max']
    maxopen = parsed['maxopen']
    minval = parsed['min']
    minopen = parsed['minopen']

    return separator, skip_header, col, maxval, maxopen, minval, minopen


def process(line: str, separator: str, col: int, maxval: float, maxopen: float, minval: float, minopen: float):
    components = line.split(separator)

    try:
        filterarg = components[col]
    except IndexError:
        print('%s: too few components: %s' % (CMD, line), file=sys.stderr)
        exit(1)

    try:
        filterarg = float(filterarg)
    except ValueError:
        print('%s: bad column: %s' % (CMD, filterarg), file=sys.stderr)
        exit(1)

    if maxval is not None and filterarg > maxval:
        return

    if maxopen is not None and filterarg >= maxopen:
        return

    if minval is not None and filterarg < minval:
        return

    if minopen is not None and filterarg <= minopen:
        return

    print(line)


def main():
    sep, skip_header, col, maxval, maxopen, minval, minopen = parse_arguments()

    for i, line in enumerate(sys.stdin):
        if i == 0 and skip_header:
            continue

        process(line.strip(), sep, col, maxval, maxopen, minval, minopen)


if __name__ == '__main__':
    try:
        main()
    except (KeyboardInterrupt, SystemExit, BrokenPipeError):
        pass
