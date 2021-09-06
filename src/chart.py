"""Handle charts"""

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


class Chart:
    name = ""
    bpm = 0
    data = []

    def __init__(self, name: str, bpm: int):
        self.name = name
        self.bpm = bpm
        self.data = []  # Important to re-init empty value each time

    def __str__(self):

        notes = ""

        for s in range(self.get_section_count()):
            sec = self.get_section(s)
            for note in sec[2]:
                notes = notes + str(note) + "\n"

        return "Name: " + str(self.name) + "\n" \
               + "BPM: " + str(self.bpm) + "\n" \
               + "Sections: " + str(self.get_section_count()) + "\n" \
               + "Notes: " + str(notes)

    def add_section(self, section_number, section_bpm=None, section_name=None, musthit=True):
        section_notes = []  # Start with an empty list (no notes in the section)
        # Represent section as a tuple of name-string, bpm, and note-list
        section = section_name, section_bpm, section_notes, musthit

        # if section_number:
        self.data.insert(section_number, section)  # Store the section at the index in our data list
        # else:
        #     self.data.append(section)   # Store the section, adding it to the end of our data list

        return self.get_section_count()

    def get_section(self, section_number):
        return self.data[section_number]  # Return the section at the numbered position

    def get_section_count(self):
        return len(self.data)  # Return the number of sections

    def add_note(self, section_number, note_number, note_object):
        section_name, section_bpm, section_notes, _ = self.get_section(section_number)  # Get the section name and notes
        section_notes.insert(note_number, note_object)  # Insert the inputted note object at the inputted note position

        return len(section_notes)  # Return the number of notes in this section

    def get_note(self, section_number, note_number):
        return self.get_section(section_number)[2][note_number]  # Get the section, select the note, return it

    def replace_note(self, section_number, note_number, new_note_object):
        section_name, section_bpm, section_notes, _ = self.get_section(section_number)  # Get the section name and notes
        section_notes[note_number] = new_note_object  # Replace the note at the inputted position

        return len(section_notes)  # Return the number of notes in this section

    def get_bpm(self, section_number=None):
        return self.bpm

    def get_name(self):
        return self.name

    def get_must_hit_section(self, section_number):
        return self.get_section(section_number)[3]

    def remap_frets(self, new_mapping: dict):
        for s in range(self.get_section_count()):
            sec = self.get_section(s)
            for n in range(len(sec[2])):
                nte = self.get_note(s, n)
                nte.fret = new_mapping[nte.fret]
                self.replace_note(s, n, nte)

