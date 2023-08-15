import pytest
from main import main


class TestMain:
    def test_validate_Single(self, capsys):
        content = """
            Student Marco
            Student David
            Student Fran
            Presence Marco 1 09:02 10:17 R100
            Presence Marco 3 10:58 12:05 R205
            Presence David 5 14:02 15:46 F505
        """
        result = """Marco: 142 minutes in 2 days
David: 104 minutes in 1 days
Fran: 0 minutes"""

        main(content=content)
        captured = capsys.readouterr()
        printResult = captured.out.strip()
        assert printResult == result.strip()

    def test_validate_WithError(self):
        content = """
            Student Marco
            Student David
            Student Fran
            RareCase Marco 1 09:02 10:17 R100
        """
        with pytest.raises(Exception, match='NOT_IMPLEMENTED'):
            main(content=content)
