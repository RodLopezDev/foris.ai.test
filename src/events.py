from typing import Callable, Dict

from src.classes.Presence import Presence
from src.classes.StudentPresence import StudentPresence


def add_student_event(state: Dict[str, StudentPresence], items: list[str]):
    student = items.pop(0)
    state[student] = StudentPresence()


def add_presence_event(state: Dict[str, StudentPresence], items: list[str]):
    student = items.pop(0)
    day = items[0]
    init = items[1]
    end = items[2]
    place = items[3]

    if state.get(student):
        presence = Presence(day, init, end, place)
        state.get(student).add_presence(presence)


map_of_events: Dict[str, Callable[[Dict[str, StudentPresence], list[str]], None]] = {
    'Student': add_student_event,
    'Presence': add_presence_event,
}
