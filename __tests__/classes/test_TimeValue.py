import sys
import pytest
from src.classes.TimeValue import TimeValue


class TestProcessor:
    def test_validate_Value_0(self):
        time_value = TimeValue('00:00')
        assert time_value.minutes == 0

    def test_validate_Value_Custom(self):
        time_value = TimeValue('02:13')
        assert time_value.minutes == 60 * 2 + 13

    def test_validate_Value_Exceptions(self):
        with pytest.raises(Exception):
            TimeValue('a:1')
        with pytest.raises(Exception):
            TimeValue('12:sxo')
        with pytest.raises(Exception):
            TimeValue('13345sxo')
        with pytest.raises(Exception):
            TimeValue('')
