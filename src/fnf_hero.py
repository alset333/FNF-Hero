#!/usr/bin/env python3

"""FNF Hero. A utility to convert between .chart files for Clone Hero and .json files for Friday Night Funkin'.
"""

__copyright__ = 'Copyright 2021, Peter Maar'
__author__ = 'Peter Maar <PeterMaar@protonmail.com>'
__license__ = 'GNU Lesser General Public License Version 3'

# __version__ = '0.0.0'
# __date__ = 'D Month YYYY'
# __credits__ = None

#   This file is part of FNF Hero.
#
#   FNF Hero is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Lesser General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   FNF Hero is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Lesser General Public License for more details.
#
#   You should have received a copy of the GNU Lesser General Public License
#   along with FNF Hero.  If not, see <https://www.gnu.org/licenses/>.


import argparse
import os

import chart_format.dot_chart
import chart_format.fnf_chart

SWAP_MUSTHIT = True
CHART_FORMATS = ['dot_chart', 'fnf_chart']

# Default for CH -> FNF is mustHitSection true (shows more of the scene at start)
# When mustHitSection is true in FNF, the FNF frets look like [4567 0123]

# In .CHART:  0-4 is Green-Orange, 5 is a force flag, 6 is the Tap note flag, 7 is the Open note flag
# Source: https://www.reddit.com/r/GuitarHero/comments/5zfyad/question_about_the_format_of_chart_files/dezgqrb

FRET_MAPPING = {
    0: 0,
    1: 0,
    2: 1,
    3: 2,
    4: 3,
    5: None,
    6: None,
    7: 3
}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="FNF Hero.\
        A utility to convert between .chart files for Clone Hero and .json files for Friday Night Funkin'.")

    parser.add_argument('input_format', type=str, help='Input chart format')
    parser.add_argument('input_file', type=str, help='Input file to read')
    parser.add_argument('output_format', type=str, help='Output chart format')
    parser.add_argument('output_file', type=str, help='Output file to write')

    args = parser.parse_args()

    valid_args = True

    input_path = os.path.normpath(args.input_file)
    output_path = os.path.normpath(args.output_file)

    if args.input_format.lower() not in CHART_FORMATS:  # If the input format is unknown
        valid_args = False  # Note the arguments are invalid
        print("Invalid input format")  # Report the error

    if not os.path.isfile(input_path):  # If the file does not exist
        valid_args = False  # Note the arguments are invalid
        print("Invalid input file")  # Report the error

    if args.output_format.lower() not in CHART_FORMATS:  # If the output format is unknown
        valid_args = False  # Note the arguments are invalid
        print("Invalid output format")  # Report the error

    if os.path.exists(output_path):  # If the path already exists
        valid_args = False  # Note the arguments are invalid
        print("Output file already exists")  # Report the error

    if not valid_args:
        print("Exiting due to invalid arguments.")
        exit()

    input_file = open(input_path)
    input_contents = input_file.read()
    input_file.close()

    internal_chart = None
    output_contents = None

    if args.input_format.lower() == 'dot_chart':
        internal_chart = chart_format.dot_chart.process_external_chart(input_contents)
    elif args.output_format.lower() == 'fnf_chart':
        internal_chart = chart_format.fnf_chart.process_external_chart(input_contents)

    if internal_chart:
        if args.output_format.lower() == 'dot_chart':
            None  # TODO
        elif args.output_format.lower() == 'fnf_chart':
            internal_chart.remap_frets(FRET_MAPPING)
            internal_chart.name = "Tutorial"
            output_contents = chart_format.fnf_chart.export_chart(internal_chart, musthit_swap=SWAP_MUSTHIT)

    if output_contents:
        if os.path.exists(output_path):
            print("Error. Output path suddenly exists.")
            exit()
        else:
            output_file = open(output_path, 'w')
            output_file.write(output_contents)
            output_file.close()

    # exit()
    #
    # # FNF_CHART_FILE = os.path.normpath(sys.path[0] + "/../test_files/tutorial.json")
    # DOT_CHART_FILE = os.path.normpath(sys.path[0] + "/../test_files/s4.chart")
    #
    # # fnf_chart = chart_format.fnf_chart.process_external_chart(open(FNF_CHART_FILE).read())
    # dot_chart = chart_format.dot_chart.process_external_chart(open(DOT_CHART_FILE).read())
    #
    # # print(fnf_chart)
    # # print(dot_chart)
    #
    # # Because we leave mustHitSection as true (shows more of the scene) the FNF frets look like [4567 0123]
    #
    # # 0-4 is Green-Orange, 5 is a force flag, 6 is the Tap note flag, 7 is the Open note flag
    # # Source: https://www.reddit.com/r/GuitarHero/comments/5zfyad/question_about_the_format_of_chart_files/dezgqrb
    #
    # fret_mapping = {
    #     0: 0,
    #     1: 0,
    #     2: 1,
    #     3: 2,
    #     4: 3,
    #     5: 5,
    #     6: 6
    # }
    # dot_chart.remap_frets(fret_mapping)
    #
    # dot_chart.name = "Tutorial"
    #
    # fnf_export = chart_format.fnf_chart.export_chart(dot_chart)
    #
    # print(fnf_export)
    #
    # None
    #
    # # n = note.Note(0, 10, 0)
    #
    # # print(n)
