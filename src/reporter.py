from typing import Dict
from src.classes.StudentPresence import StudentPresence


def PrintReport(state: Dict[str, StudentPresence]):
    sorted_data = sorted(
        state.items(), key=lambda item: item[1].totalMinutes(), reverse=True)
    for name, presences in sorted_data:
        if not presences.total():
            print(f"{name}: 0 minutes")
            continue
        print(f"{name}: {presences.totalMinutes()} minutes in {presences.total()} days")
