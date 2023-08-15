import pytest
from typing import Dict

from src.events import map_of_events
from src.classes.StudentPresence import StudentPresence


class TestEvents:
    def test_should_be_run_Student_case(self):
        case = 'Student'
        row = ['TestName']

        state: Dict[str, StudentPresence] = {}

        map_of_events.get(case)(state, row)

        assert state.get('TestName') != None
        assert state.get('TestNameCustom') == None

    def test_should_be_run_Presence_case(self):
        case = 'Presence'
        row = ['Marcos', '1', '10:30', '12:00', 'EXM']

        state: Dict[str, StudentPresence] = {'Marcos': StudentPresence()}

        map_of_events.get(case)(state, row)

        assert state.get('Marcos') != None
        assert state.get('Marcos').total() == 1
        assert state.get('Marcos').totalMinutes() == 90

        row2 = ['Marcos', '2', '14:25', '20:00', 'EXM']

        map_of_events.get(case)(state, row2)

        assert state.get('Marcos') != None
        assert state.get('Marcos').total() == 2
        assert state.get('Marcos').totalMinutes() == 90 + 335

    def test_should_be_run_Presence_case_with_error(self):
        case = 'Student'
        row = []

        state: Dict[str, StudentPresence] = {}

        with pytest.raises(Exception, match='Inconsistent data'):
            map_of_events.get(case)(state, row)

    def test_should_be_run_Presence_case_with_error(self):
        case = 'Presence'
        row = ['Marcos']

        state: Dict[str, StudentPresence] = {'Marcos': StudentPresence()}

        with pytest.raises(Exception, match='Inconsistent data'):
            map_of_events.get(case)(state, row)

    def test_should_be_run_Presence_case_corner_case(self):
        case = 'Presence'
        row = ['Marcos', '1', '10:30', '12:00', 'EXM']

        state: Dict[str, StudentPresence] = {}

        map_of_events.get(case)(state, row)

        assert state.get('Marcos') == None
