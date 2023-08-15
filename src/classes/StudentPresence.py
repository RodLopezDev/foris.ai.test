from functools import reduce
from src.classes.Presence import Presence


class StudentPresence():
    def __init__(self):
        self.presences: list[Presence] = []

    def add_presence(self, presence: Presence):
        self.presences.append(presence)

    def total(self):
        return len(self.presences)

    def totalMinutes(self):
        return reduce(lambda x, y: x + y.minutes, self.presences, 0)
