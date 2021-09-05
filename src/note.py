class Note:
    start_time = 0  # Note start time in ms
    end_time = 0  # Note end time in ms
    fret = 0  # Color/position of the note. Starts at zero (leftmost) and increases rightwards.

    def __init__(self, start_time, end_time, fret):
        self.start_time = start_time
        self.end_time = end_time
        self.fret = fret

    def get_start_time(self):
        return self.start_time

    def __str__(self):
        return "Start: " + str(self.start_time) + "\t" \
               + "End: " + str(self.end_time) + "\t" \
               + "Fret: " + str(self.fret)
