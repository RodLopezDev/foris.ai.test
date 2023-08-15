import sys
import pytest
import unittest
from unittest.mock import patch

from src.input import StrategyReadIn, StrategyArgument, getInputData


class TestStrategyReadIn(unittest.TestCase):
    def test_validate_StrategyReadIn(self):
        with patch('sys.stdin.isatty', return_value=False):
            strategy = StrategyReadIn()
            self.assertTrue(strategy.Validate())
            assert strategy.Validate() == True

    def test_execute_StrategyReadIn(self):
        input_content = "Test content\nSecond line\n"
        expected_output = input_content

        with patch('sys.stdin.read', return_value=input_content):
            strategy = StrategyReadIn()
            output = strategy.execute()
            self.assertEqual(output, expected_output)
            assert output == expected_output

    def test_execute_error_StrategyReadIn(self):
        with patch('sys.stdin.read', side_effect=Exception("Test error")):
            strategy = StrategyReadIn()
            output = strategy.execute()
            self.assertEqual(output, "")
            assert output == ""

    def test_validate_StrategyArgument(self):
        with patch.object(sys, 'argv', ['program_name', 'input_file.txt']):
            strategy = StrategyArgument()
            self.assertTrue(strategy.Validate())
            assert strategy.Validate() == True

    def test_execute_StrategyArgument(self):
        input_file_content = "Test content\nSecond line\n"
        input_file_name = 'input_file.txt'

        with patch('builtins.open', unittest.mock.mock_open(read_data=input_file_content)):
            with patch.object(sys, 'argv', ['program_name', input_file_name]):
                strategy = StrategyArgument()
                output = strategy.execute()
                self.assertEqual(output, input_file_content)

    def test_execute_file_not_found_StrategyArgument(self):
        input_file_name = 'nonexistent_file.txt'

        with patch('builtins.open', side_effect=FileNotFoundError):
            with patch.object(sys, 'argv', ['program_name', input_file_name]):
                strategy = StrategyArgument()
                output = strategy.execute()
                self.assertEqual(output, "")

    def test_execute_error_StrategyArgument(self):
        input_file_name = 'input_file.txt'

        with patch('builtins.open', side_effect=Exception("Test error")):
            with patch.object(sys, 'argv', ['program_name', input_file_name]):
                strategy = StrategyArgument()
                output = strategy.execute()
                self.assertEqual(output, "")

    def test_manager_first_strategy(self):
        input_content = "Test content\nSecond line\n"
        with patch('sys.stdin.isatty', return_value=False):
            with patch('sys.stdin.read', return_value=input_content):
                content = getInputData()
                assert content == input_content

    def test_manager_first_strategy_with_error(self):
        input_content = ""
        with patch('sys.stdin.isatty', return_value=False):
            with patch('sys.stdin.read', return_value=input_content):
                with pytest.raises(Exception, match='CONTENT_NOT_FOUND::ReadInFile'):
                    getInputData()

    def test_manager_second_strategy(self):
        input_file_content = "Test content\nSecond line\n"
        input_file_name = 'input_file.txt'

        with patch('builtins.open', unittest.mock.mock_open(read_data=input_file_content)):
            with patch.object(sys, 'argv', ['program_name', input_file_name]):
                content = getInputData()
                assert content == input_file_content

    def test_manager_second_strategy_with_error(self):
        input_file_content = ""
        input_file_name = 'input_file.txt'

        with patch('builtins.open', unittest.mock.mock_open(read_data=input_file_content)):
            with patch.object(sys, 'argv', ['program_name', input_file_name]):
                with pytest.raises(Exception, match='CONTENT_NOT_FOUND::ArgumentFile'):
                    getInputData()

    def test_manager_none_strategy_with_error(self):
        with patch('sys.stdin.isatty', return_value=True):
            with pytest.raises(Exception, match='STRATEGY_NOT_FOUND'):
                getInputData()
