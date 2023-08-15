import pytest
from src.classes.Presence import Presence
from src.classes.StudentPresence import StudentPresence


class TestStudentPresence:
    def test_validate_Value(self):
        place = 'EXM'
        total1 = 60 * 4
        presence1 = Presence('1', '09:00', '13:00', place)
        assert presence1.minutes == total1

        total2 = 60 * 7
        presence2 = Presence('1', '11:00', '18:00', place)
        assert presence2.minutes == total2

        presences = StudentPresence()
        presences.add_presence(presence1)
        presences.add_presence(presence2)
        assert presences.total() == 2
        assert presences.totalMinutes() == total1 + total2
