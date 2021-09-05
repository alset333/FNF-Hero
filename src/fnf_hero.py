#!/usr/bin/env python3

import os, sys

import re

import chart_format.dot_chart
import chart_format.fnf_chart

if __name__ == "__main__":

    DOT_CHART_FILE = os.path.normpath(sys.path[0] + "/../test_files/notes.chart")
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
