"""Handle notes"""

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
