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

        notes = sections[s]["sectionNotes"]  # Get the list of notes for the current section


        internal_chart.add_section(s)  # Add a section to our internal chart at the current index

        for n in range(len(notes)):  # Iterate over the notes within the section, using n as an index

            external_note = notes[n]
            external_start = external_note[0]
            lastPosition = external_start
            external_fret = external_note[1]
            external_end = external_start + external_note[2]

            internal_note = note.Note(external_start, external_end, external_fret)  # FNF already uses ms for time; keep

            internal_chart.add_note(s, n, internal_note)


    return internal_chart


def export_external_chart():
    return None  # TODO
