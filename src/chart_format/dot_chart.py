"""Handle .CHART files"""

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


import chart
import note


def parse_chart_line(line: str):
    line = line.split()

    for i in range(len(line)):
        if line[i].isnumeric():
            line[i] = int(line[i])
        else:
            line[i] = line[i].strip('"')

    if type(line[0]) is int:  # Key is numerical
        if len(line) == 4:  # timestamp = key value
            return line[0], line[2].lower(), line[3]  # timestamp, key, value
        elif line[3] == 'section':  # Section name like [1234, '=', 'E', 'section', "Some", 'Section', 'Name']
            return line[0], line[2].lower(), (line[3], ' '.join(line[4:]))
        elif len(line) == 5:  # timestamp = key value value
            return line[0], line[2].lower(), (line[3], line[4])  # timestamp, key, (val1, val2)
        else:
            print("Cannot parse line:\n", line)

    else:  # Key is not numerical
        if type(line[2]) is int:  # Key = NUMBER
            return line[0].lower(), int(line[2])
        else:  # Key = "STRING" or Key = VALUE
            return line[0].lower(), line[2].replace('"', '')  # Remove any quotes


def process_external_chart(source_chart_contents: str):
    ascii_chart_contents = source_chart_contents.encode("ascii", errors="ignore").decode()  # ASCII only

    # Split chart contents into lines
    lines = ascii_chart_contents.splitlines()
    lines_lower = ascii_chart_contents.lower().splitlines()

    section_pos_song = None
    section_pos_synctrack = None
    section_pos_events = None
    section_pos_easysingle = None
    section_pos_easysinglebass = None
    section_pos_mediumsingle = None
    section_pos_mediumsinglebass = None
    section_pos_hardsingle = None
    section_pos_hardsinglebass = None
    section_pos_expertsingle = None
    section_pos_expertsinglebass = None

    # Process each line
    for i in range(len(lines)):
        # Strip (leading/trailing whitespace from) each line
        lines[i] = lines[i].strip()
        lines_lower[i] = lines_lower[i].strip()

        # Required sections
        section_pos_song = lines_lower.index('[song]')
        section_pos_synctrack = lines_lower.index('[synctrack]')
        section_pos_events = lines_lower.index('[events]')

        DIFFICULTY_AND_INSTRUMENT = 'ExpertSingle'  # TODO

        section_notes_name = '[' + DIFFICULTY_AND_INSTRUMENT.lower() + ']'

        if section_notes_name in lines_lower:
            section_pos_notes = lines_lower.index(section_notes_name)

        # if '[easysingle]' in lines_lower:
        #     section_pos_easysingle = lines_lower.index('[easysingle]')
        # if '[easysinglebass]' in lines_lower:
        #     section_pos_easysinglebass = lines_lower.index('[easysinglebass]')
        # if '[mediumsingle]' in lines_lower:
        #     section_pos_mediumsingle = lines_lower.index('[mediumsingle]')
        # if '[mediumsinglebass]' in lines_lower:
        #     section_pos_mediumsinglebass = lines_lower.index('[mediumsinglebass]')
        # if '[hardsingle]' in lines_lower:
        #     section_pos_hardsingle = lines_lower.index('[hardsingle]')
        # if '[hardsinglebass]' in lines_lower:
        #     section_pos_hardsinglebass = lines_lower.index('[hardsinglebass]')
        # if '[expertsingle]' in lines_lower:
        #     section_pos_expertsingle = lines_lower.index('[expertsingle]')
        # if '[expertsinglebass]' in lines_lower:
        #     section_pos_expertsinglebass = lines_lower.index('[expertsinglebass]')

    # print(section_pos_song,
    #       section_pos_synctrack,
    #       section_pos_events,
    #       section_pos_easysingle,
    #       section_pos_easysinglebass,
    #       section_pos_mediumsingle,
    #       section_pos_mediumsinglebass,
    #       section_pos_hardsingle,
    #       section_pos_hardsinglebass,
    #       section_pos_expertsingle,
    #       section_pos_expertsinglebass)

    ############################
    # Process the "Song" section
    ############################

    sec_start = section_pos_song
    sec_end = lines.index('}', sec_start + 1)  # Find the end of the section (first '}' after start)
    section = lines[sec_start + 2:sec_end]  # Isolate the section

    name = None
    offset = None
    resolution = None
    player2 = None
    difficulty = None
    previewstart = None
    previewend = None
    genre = None
    mediatype = None

    for i in range(len(section)):
        ln = section[i]

        key, val = parse_chart_line(ln)
        if key == 'name':
            name = val
        elif key == 'offset':
            offset = val
        elif key == 'resolution':
            resolution = val
        elif key == 'player2':
            player2 = val
        elif key == 'difficulty':
            difficulty = val
        elif key == 'previewstart':
            previewstart = val
        elif key == 'previewend':
            previewend = val
        elif key == 'genre':
            genre = val
        elif key == 'mediatype':
            mediatype = val

    # print(name,
    # offset,
    # resolution,
    # player2,
    # difficulty,
    # previewstart,
    # previewend,
    # genre,
    # mediatype)

    ############################
    # Process the "SyncTrack" section
    ############################

    sec_start = section_pos_synctrack
    sec_end = lines.index('}', sec_start + 1)  # Find the end of the section (first '}' after start)
    section = lines[sec_start + 2:sec_end]  # Isolate the section

    time_signature = None
    bpm = None

    for i in range(len(section)):
        ln = section[i]

        pos, key, val = parse_chart_line(ln)

        if key == 'ts':
            time_signature = val
        elif key == 'b':
            bpm = val / 1000

    # print(time_signature,
    #       bpm)

    ############################
    # Process the "Events" section
    ############################

    sec_start = section_pos_events
    sec_end = lines.index('}', sec_start + 1)  # Find the end of the section (first '}' after start)
    section = lines[sec_start + 2:sec_end]  # Isolate the section

    chart_sections = []

    for i in range(len(section)):
        ln = section[i]

        pos, key, val = parse_chart_line(ln)
        pos = 1000 * (pos / resolution) / (bpm / 60)

        if key == 'e' and val[0] == 'section':
            chart_sections.append((pos, val[1]))  # Add pos, name to our list of sections for use later

            # TODO get BPM

    chart_sections.sort()  # Sort them so they are ordered by position

    # print(chart_sections)

    ############################
    # Process the notes section
    ############################

    # section_pos_easysingle
    # section_pos_easysinglebass
    # section_pos_mediumsingle
    # section_pos_mediumsinglebass
    # section_pos_hardsingle
    # section_pos_hardsinglebass
    # section_pos_expertsingle
    # section_pos_expertsinglebass

    sec_start = section_pos_notes  # If you get an exception here, try fixing the notes section name (ExpertSingle, HardSingle, etc). Currently it's in DIFFICULTY_AND_INSTRUMENT. TODO
    sec_end = lines.index('}', sec_start + 1)  # Find the end of the section (first '}' after start)
    section = lines[sec_start + 2:sec_end]  # Isolate the section

    chart_notes = []

    for i in range(len(section)):
        ln = section[i]

        pos, key, val = parse_chart_line(ln)
        pos = 1000 * (pos / resolution) / (bpm / 60)

        if key == 'n':
            chart_notes.append((pos, val))

    chart_notes.sort()

    # print(chart_notes)  # Sort them so they are ordered by position

    ############################
    # Build an internal chart
    ############################

    times = []
    # time_lookup = {}

    for s in chart_sections:
        if s[0] not in times:
            times.append(s[0])
        # if s[0] not in time_lookup:
        #     time_lookup[s[0]] = []
        # time_lookup[s[0]].append(s)

    for c in chart_notes:
        if c[0] not in times:
            times.append(c[0])
        # if c[0] not in time_lookup:
        #     time_lookup[c[0]] = []
        # time_lookup[c[0]].append(c)

    times.sort()

    # print(time_lookup)

    internal_chart = chart.Chart(name, bpm)
    latest_section_number = 0

    for time in times:
        for s in range(len(chart_sections)):
            sec = chart_sections[s]
            if sec[0] == time:
                internal_chart.add_section(i, section_name=sec[1])
                latest_section_number = s
        for n in range(len(chart_notes)):
            nte = chart_notes[n]
            if nte[0] == time:
                internal_chart.add_note(latest_section_number, n, note.Note(nte[0], nte[0] + nte[1][1], nte[1][0]))

    #
    # for t in times:
    #
    #
    #
    #

    #
    # for i in range(len(chart_sections)):
    #     sec = chart_sections[i]
    #     internal_chart.add_section(i, sec[0], section_name=sec[1])  # TODO get BPM
    #
    # for i in range(len(chart_notes)):
    #     ext_note = chart_notes[i]
    #
    #     start = ext_note[0]  # TODO ms not ticks
    #     end = ext_note[0] + ext_note[1][1]
    #     fret = ext_note[1][0]
    #     n = note.Note(start, end, fret)
    #
    #     # internal_chart.add_note(n)
    #
    #
    # # current_position = 0
    # #
    # # for ext_note in chart_notes:
    # #     start = ext_note[0]  # TODO ms not ticks
    # #     end = ext_note[0] + ext_note[1][1]
    # #     fret = ext_note[1][0]
    # #     n = note.Note(start, end, fret)
    # #     print(n)

    return internal_chart


def export_external_chart():
    return None  # TODO
