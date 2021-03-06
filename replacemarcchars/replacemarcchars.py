#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys
import argparse

REPLACE_METHODS = {
    'decimal': (('#29;', '#30;', '#31;'), ("\x1D", "\x1E", "\x1F")),
    'unicode': (('\u001d', '\u001e', '\u001f'), ("\x1D", "\x1E", "\x1F")),
    'hex': (('\x1D', '\x1E', '\x1F'), ("\x1D", "\x1E", "\x1F"))
}


def run():
    parser = argparse.ArgumentParser(prog='replacemarcchars',
                                     description='takes binary MARC records/lines (e.g. originally stored in a JSON value) as input and replace some characters in it to be really binary MARC compatible.',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    optional_arguments = parser._action_groups.pop()

    optional_arguments.add_argument('-replace-method', type=str, choices=['decimal', 'unicode', 'hex'],
                                    help="method for character replacement",
                                    default="decimal", dest='replace_method')

    parser._action_groups.append(optional_arguments)

    args = parser.parse_args()

    replace_method = args.replace_method
    replace_method_tuple = REPLACE_METHODS.get(replace_method)

    for line in sys.stdin:
        marc_record = line
        # remove line break
        lastchar = line[-1]
        oslinebreak = os.linesep
        if lastchar == oslinebreak:
            marc_record = line[0:-1]
        for i in range(0, 3):
            marc_record = marc_record.replace(replace_method_tuple[0][i], replace_method_tuple[1][i])

        sys.stdout.write(marc_record)


if __name__ == "__main__":
    run()
