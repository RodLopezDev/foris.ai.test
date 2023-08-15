import pytest
from main import main
from src.input import getMockData


class TestMain:
    def test_validate_Single(self, capsys):
        result = """Marco: 142 minutes in 2 days
David: 104 minutes in 1 days
Fran: 0 minutes"""

        main(getContent=getMockData)
        captured = capsys.readouterr()
        printResult = captured.out.strip()
        assert printResult == result.strip()

    def test_validate_WithError(self):
        def getContent(): return """
            Student Marco
            Student David
            Student Fran
            RareCase Marco 1 09:02 10:17 R100
        """
        with pytest.raises(Exception, match='NOT_IMPLEMENTED'):
            main(getContent=getContent)

    def test_validate_CornerCase(self):
        def getContent(): return """
            Student Marco
            Student David
            Presence Marco 1 X X R100
        """
        main(getContent=getContent)