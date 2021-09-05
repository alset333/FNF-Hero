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


import os
import sys

import chart_format.dot_chart
import chart_format.fnf_chart

if __name__ == "__main__":
    DOT_CHART_FILE = os.path.normpath(sys.path[0] + "/../test_files/ttfaf.chart")
    FNF_CHART_FILE = os.path.normpath(sys.path[0] + "/../test_files/tutorial.json")

    fnf_chart = chart_format.fnf_chart.process_external_chart(open(FNF_CHART_FILE).read())

    dot_chart = chart_format.dot_chart.process_external_chart(open(DOT_CHART_FILE).read())

    print(fnf_chart)
    print(dot_chart)

    fnf_export = chart_format.fnf_chart.export_chart(dot_chart)

    print(fnf_export)

    None

    # n = note.Note(0, 10, 0)

    # print(n)
