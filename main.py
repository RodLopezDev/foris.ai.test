from typing import Dict, Callable

from src.input import getInputData
from src.events import map_of_events
from src.reporter import PrintReport
from src.classes.StudentPresence import StudentPresence


def main(
    *,
    getContent: Callable[[], str] = getInputData,
    reporter: Callable[[Dict[str, StudentPresence]], None] = PrintReport
):
    # 1. Get data
    content = getContent()
    lines = content.splitlines()

    errors = []
    globalState: Dict[str, StudentPresence] = {}

    # 2. Process data
    for line in lines:
        if not line.strip():
            continue
        items = line.strip().split(" ")
        action = items.pop(0)

        if not map_of_events.get(action):
            raise Exception('NOT_IMPLEMENTED')

        try:
            map_of_events.get(action)(globalState, items)
        except:
            errors.append(line)

    # 3. Visualize data result
    reporter(globalState)


if __name__ == "__main__":
    main()
