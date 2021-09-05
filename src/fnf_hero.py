#!/usr/bin/env python3

import os, sys

import re

import chart_format.dot_chart
import chart_format.fnf_chart

if __name__ == "__main__":

    DOT_CHART_FILE = os.path.normpath(sys.path[0] + "/../test_files/test.chart")
    FNF_CHART_FILE = os.path.normpath(sys.path[0] + "/../test_files/test.json")

    fnf_chart = chart_format.fnf_chart.process_external_chart(open(FNF_CHART_FILE).read())

    dot_chart = chart_format.dot_chart.process_external_chart(open(DOT_CHART_FILE).read())


    #
    # c = chart.Chart("example", 60)
    #
    # c.add_section(0)
    # c.add_section(1, "a section name")
    #
    # c.add_note(0, 0, note.Note(0, 10, 0))
    # c.add_note(1, 0, note.Note(10, 20, 2))




    None

    # n = note.Note(0, 10, 0)

    # print(n)
