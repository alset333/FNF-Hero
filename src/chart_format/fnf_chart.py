import json

import chart
import note


def process_external_chart(source_chart_contents: str):
    external_chart = json.loads(source_chart_contents)  # Load the json str into a dictionary we can easily manipulate

    # Get some key values from the chart
    song_node = external_chart["song"]
    sections = song_node["notes"]
    chart_name = song_node["song"]
    chart_bpm = song_node["bpm"]

    # Create a chart using our internal format
    internal_chart = chart.Chart(chart_name, chart_bpm)

    for s in range(len(sections)):  # Iterate over the sections, using s as an index

        musthit = sections[s]['mustHitSection']
        notes = sections[s]["sectionNotes"]  # Get the list of notes for the current section

        internal_chart.add_section(s, musthit=musthit)  # Add a section to our internal chart at the current index

        for n in range(len(notes)):  # Iterate over the notes within the section, using n as an index

            external_note = notes[n]
            external_start = external_note[0]
            lastPosition = external_start
            external_fret = external_note[1]
            external_end = external_start + external_note[2]

            internal_note = note.Note(external_start, external_end, external_fret)  # FNF already uses ms for time; keep

            internal_chart.add_note(s, n, internal_note)

    return internal_chart


def export_chart(internal_chart: chart):
    # Start with a template dictionary
    external_chart = {'song': {
        'bpm': internal_chart.get_bpm(),
        'needsVoices': False,
        'notes': [],
        'player1': 'bf',
        'player2': 'gf',
        'sections': internal_chart.get_section_count(),
        'song': internal_chart.get_name(),
        'speed': 1  # TODO What is this?
    }
    }

    for s in range(internal_chart.get_section_count()):
        section = internal_chart.get_section(s)
        section_notes = []
        for nt in section[2]:
            if nt:
                section_notes.append([nt.start_time, nt.fret, nt.end_time-nt.start_time])

        if section[2]:
            section_bpm = section[1]
            change_bpm = True
        else:
            section_bpm = internal_chart.get_bpm()
            change_bpm = False

        external_chart['song']['notes'].append({
            # 'altAnim': False,
            # 'bpm': section_bpm,
            # 'changeBPM': change_bpm,
            'lengthInSteps': 16,  # TODO
            'mustHitSection': internal_chart.get_must_hit_section(s),  # TODO
            'sectionNotes': section_notes,
            'typeOfSection': 0  # TODO

        })

    export_chart_contents = json.dumps(external_chart)  # Export the dictionary as a json str

    return export_chart_contents
