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
        section_name, section_bpm, section_notes, musthit = self.get_section(section_number)  # Get the section name and notes
        section_notes.insert(note_number, note_object)  # Insert the inputted note object at the inputted note position

        return len(section_notes)  # Return the number of notes in this section

    def get_note(self, section_number, note_number):
        return self.get_section(section_number)[2][note_number]  # Get the section, select the note, return it

    def get_bpm(self, section_number=None):
        return self.bpm

    def get_name(self):
        return self.name

    def get_must_hit_section(self, section_number):
        return self.get_section(section_number)[3]