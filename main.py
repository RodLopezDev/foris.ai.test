from functools import reduce
from typing import Dict, Callable

from src.classes.TimeValue import TimeValue


def getInputData():
    return """
        Student Marco
        Student David
        Student Fran
        Presence Marco 1 09:02 10:17 R100
        Presence Marco 3 10:58 12:05 R205
        Presence David 5 14:02 15:46 F505
    """


def add_student_event(state: Dict[str, list[int]], items: list[str]):
    student = items.pop(0)
    state[student] = []


def add_presence_event(state: Dict[str, list[int]], items: list[str]):
    student = items.pop(0)
    base_minutes = TimeValue(items[1])
    end_minutes = TimeValue(items[2])
    minutes = end_minutes.minutes - base_minutes.minutes
    state[student].append(minutes)


map_of_events: Dict[str, Callable[[Dict[str, list[int]], list[str]], None]] = {
    'Student': add_student_event,
    'Presence': add_presence_event,
}


def main(
    *,
    content: str = getInputData()
):
    # 1. Get data
    lines = content.splitlines()

    globalState: Dict[str, list[int]] = {}

    # 2. Process data
    for line in lines:
        if not line.strip():
            continue
        items = line.strip().split(" ")
        action = items.pop(0)

        if not map_of_events.get(action):
            raise Exception('NOT_IMPLEMENTED')

        map_of_events.get(action)(globalState, items)

    # 3. Visualize data result
    for name, presences in globalState.items():
        if not len(presences):
            print(f"{name}: 0 minutes")
        else:
            minutes = reduce(lambda x, y: x + y, presences, 0)
            print(f"{name}: {minutes} minutes in {len(presences)} days")


if __name__ == "__main__":
    main()
