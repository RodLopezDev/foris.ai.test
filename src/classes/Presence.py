from src.classes.TimeValue import TimeValue


class Presence():
    def __init__(self, day: str, init: str, end: str, place: str):
        self.day = day
        self.place = place
        self.init = init
        self.end = end
        self.minutes = TimeValue(end).minutes - TimeValue(init).minutes
