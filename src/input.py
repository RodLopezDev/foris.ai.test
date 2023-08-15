import sys
from typing import Callable
from abc import ABC, abstractmethod


class AbstractStrategy(ABC):
    name: str
    @abstractmethod
    def Validate() -> bool: pass

    @abstractmethod
    def execute() -> str: pass


class StrategyReadIn(AbstractStrategy):
    name = 'ReadInFile'

    def Validate(self) -> bool:
        return not sys.stdin.isatty()

    def execute(self) -> str:
        try:
            content = sys.stdin.read()
            return content
        except Exception as e:
            print(f"An error occurred: {e}")
            return ""


class StrategyArgument(AbstractStrategy):
    name = 'ArgumentFile'

    def Validate(self) -> bool:
        return len(sys.argv) == 2

    def execute(self) -> str:
        input_file_name = sys.argv[1]
        try:
            with open(input_file_name, 'r') as input_file:
                return input_file.read()
        except FileNotFoundError:
            print(f"File '{input_file_name}' not found.")
            return ""
        except Exception as e:
            print(f"An error occurred: {e}")
            return ""


def StrategyManagerFactory(strategies: list[AbstractStrategy]) -> Callable[[], str]:
    def getData():
        for strategy in strategies:
            if strategy.Validate():
                print(f"Get data from {strategy.name} strategy")
                content = strategy.execute()
                if not content:
                    raise Exception(f'CONTENT_NOT_FOUND::{strategy.name}')
                return content
        raise Exception('STRATEGY_NOT_FOUND')
    return getData


getInputData = StrategyManagerFactory([StrategyArgument(), StrategyReadIn()])


def getMockData():
    return """
        Student Marco
        Student David
        Student Fran
        Presence Marco 1 09:02 10:17 R100
        Presence Marco 3 10:58 12:05 R205
        Presence David 5 14:02 15:46 F505
    """
