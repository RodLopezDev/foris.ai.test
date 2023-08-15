from typing import Dict
from functools import reduce


def time_to_minutes(time_str: str):
    hours, minutes = map(int, time_str.split(":"))
    return hours * 60 + minutes


def main():
    # 1. Get data
    content = """
        Student Marco
        Student David
        Student Fran
        Presence Marco 1 09:02 10:17 R100
        Presence Marco 3 10:58 12:05 R205
        Presence David 5 14:02 15:46 F505
    """
    lines = content.splitlines()

    globalState: Dict[str, list[int]] = {}

    # 2. Process data
    for line in lines:
        if not line.strip():
            continue
        items = line.strip().split(" ")
        action = items.pop(0)
        student = items.pop(0)

        if action == 'Student':
            globalState[student] = []
        elif action == 'Presence':
            base_minutes = time_to_minutes(items[1])
            end_minutes = time_to_minutes(items[2])
            minutes = end_minutes - base_minutes
            globalState[student].append(minutes)
        else:
            raise Exception('NOT_IMPLEMENTED')

    # 3. Visualize data result
    for name, presences in globalState.items():
        if not len(presences):
            print(f"{name}: 0 minutes")
        else:
            minutes = reduce(lambda x, y: x + y, presences, 0)
            print(f"{name}: {minutes} minutes in {len(presences)} days")


if __name__ == "__main__":
    main()
