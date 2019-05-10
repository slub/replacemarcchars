#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import argparse

REPLACE_METHODS = {
    'decimal': (('#29;', '#30;', '#31;'), ("\x1D", "\x1E", "\x1F")),
    'unicode': (('\u001d', '\u001e', '\u001f'), ("\x1D", "\x1E", "\x1F")),
    'hex': (('\x1D', '\x1E', '\x1F'), ("\x1D", "\x1E", "\x1F"))
}


def run():
    parser = argparse.ArgumentParser(prog='replacemarcchars',
                                     description='takes binary MARC records (e.g. originally stored in a JSON value) as input and replace some characters in it to be really binary MARC compatible.',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    optional_arguments = parser._action_groups.pop()

    optional_arguments.add_argument('-replace-method', type=str, choices=['decimal', 'unicode', 'hex'],
                                    help="method for character replacement",
                                    default="decimal", dest='replace_method')

    parser._action_groups.append(optional_arguments)

    args = parser.parse_args()

    replace_method = args.replace_method

    for line in sys.stdin:
        for i in range(0, 3):
            line = line.replace(REPLACE_METHODS.get(replace_method)[0][i], REPLACE_METHODS.get(replace_method)[1][i])

        sys.stdout.write(line)


if __name__ == "__main__":
    run()
