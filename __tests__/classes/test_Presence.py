import pytest
from src.classes.Presence import Presence


class TestPresence:
    def test_validate_Value(self):
        day = '1'
        init = '10:00'
        end = '12:00'
        place = 'EXM'
        presence = Presence(day, init, end, place)
        assert presence.minutes == 120

    def test_validate_Value_Case2(self):
        day = '1'
        init = '09:01'
        end = '12:13'
        place = 'EXM'
        presence = Presence(day, init, end, place)
        assert presence.minutes == 192

    def test_validate_Value_Exceptions(self):
        day = ''
        init = ''
        end = ''
        place = ''
        with pytest.raises(Exception, match='Inconsistent Data'):
            Presence(day, init, end, place)
        with pytest.raises(BaseException, match='Inconsistent Data'):
            Presence(day, 'pruebas', 'asas', place)
        with pytest.raises(BaseException, match='Inconsistent Data'):
            Presence(day, '10:00', 'asas', place)
