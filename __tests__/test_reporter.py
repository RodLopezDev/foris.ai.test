import pytest
from typing import Dict

from src.reporter import PrintReport
from src.classes.Presence import Presence
from src.classes.StudentPresence import StudentPresence


class TestPrintReport:
    def test_should_print_report(self, capsys):
        state: Dict[str, StudentPresence] = {
            'Marcos': StudentPresence(),
            'Pedro': StudentPresence(),
        }

        report = """Marcos: 0 minutes
Pedro: 0 minutes"""

        PrintReport(state)
        captured = capsys.readouterr()
        printResult = captured.out.strip()
        assert printResult == report

    def test_should_print_report_with_data(self, capsys):
        presence1 = Presence('1', '10:00', '12:00', 'EXM')
        presence2 = Presence('1', '08:00', '15:00', 'EXM')
        presence3 = Presence('4', '14:00', '20:00', 'EXM')

        marcos_presence = StudentPresence()
        pedro_presence = StudentPresence()

        marcos_presence.add_presence(presence1)
        pedro_presence.add_presence(presence2)
        pedro_presence.add_presence(presence3)
        state: Dict[str, StudentPresence] = {
            'Marcos': marcos_presence,
            'Pedro': pedro_presence,
            'Lucas': StudentPresence(),
        }

        report = """Pedro: 780 minutes in 2 days
Marcos: 120 minutes in 1 days
Lucas: 0 minutes"""

        PrintReport(state)
        captured = capsys.readouterr()
        printResult = captured.out.strip()
        assert printResult == report
