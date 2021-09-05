import note
import chart


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
        elif len(line) == 5:   # timestamp = key value value
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

        # Optional sections
        if '[events]' in lines_lower:
            section_pos_events = lines_lower.index('[events]')
        if '[easysingle]' in lines_lower:
            section_pos_easysingle = lines_lower.index('[easysingle]')
        if '[easysinglebass]' in lines_lower:
            section_pos_easysinglebass = lines_lower.index('[easysinglebass]')
        if '[mediumsingle]' in lines_lower:
            section_pos_mediumsingle = lines_lower.index('[mediumsingle]')
        if '[mediumsinglebass]' in lines_lower:
            section_pos_mediumsinglebass = lines_lower.index('[mediumsinglebass]')
        if '[hardsingle]' in lines_lower:
            section_pos_hardsingle = lines_lower.index('[hardsingle]')
        if '[hardsinglebass]' in lines_lower:
            section_pos_hardsinglebass = lines_lower.index('[hardsinglebass]')
        if '[expertsingle]' in lines_lower:
            section_pos_expertsingle = lines_lower.index('[expertsingle]')
        if '[expertsinglebass]' in lines_lower:
            section_pos_expertsinglebass = lines_lower.index('[expertsinglebass]')

    print(section_pos_song,
          section_pos_synctrack,
          section_pos_events,
          section_pos_easysingle,
          section_pos_easysinglebass,
          section_pos_mediumsingle,
          section_pos_mediumsinglebass,
          section_pos_hardsingle,
          section_pos_hardsinglebass,
          section_pos_expertsingle,
          section_pos_expertsinglebass)

    ############################
    # Process the "Song" section
    ############################

    sec_start = section_pos_song
    sec_end = lines.index('}', sec_start+1)  # Find the end of the section (first '}' after start)
    section = lines[sec_start+2:sec_end]  # Isolate the section

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


    print(name,
    offset,
    resolution,
    player2,
    difficulty,
    previewstart,
    previewend,
    genre,
    mediatype)

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
            bpm = val

    print(time_signature,
          bpm)

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

        if key == 'e' and val[0] == 'section':
            chart_sections.append((pos, val[1]))  # Add pos, name to our list of sections for use later

            # TODO get BPM


    chart_sections.sort()  # Sort them so they are ordered by position

    print(chart_sections)


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

    NOTE_SECTION_POS = section_pos_expertsingle  # TODO option to change at runtime from available

    sec_start = NOTE_SECTION_POS
    sec_end = lines.index('}', sec_start + 1)  # Find the end of the section (first '}' after start)
    section = lines[sec_start + 2:sec_end]  # Isolate the section

    chart_notes = []

    for i in range(len(section)):
        ln = section[i]

        pos, key, val = parse_chart_line(ln)

        if key == 'n':
            chart_notes.append((pos, val))

    chart_notes.sort()

    print(chart_notes)  # Sort them so they are ordered by position

    ############################
    # Build an internal chart
    ############################

    internal_chart = chart.Chart(name, bpm)

    for i in range(len(chart_sections)):
        sec = chart_sections[i]
        internal_chart.add_section(i, sec[0], section_name=sec[1])  # TODO get BPM

    for i in range(len(chart_notes)):
        ext_note = chart_notes[i]

        start = ext_note[0]  # TODO ms not ticks
        end = ext_note[0] + ext_note[1][1]
        fret = ext_note[1][0]
        n = note.Note(start, end, fret)

        # internal_chart.add_note(n)


    # current_position = 0
    #
    # for ext_note in chart_notes:
    #     start = ext_note[0]  # TODO ms not ticks
    #     end = ext_note[0] + ext_note[1][1]
    #     fret = ext_note[1][0]
    #     n = note.Note(start, end, fret)
    #     print(n)


    return internal_chart


def export_external_chart():
    return None  # TODO