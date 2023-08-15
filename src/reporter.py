from typing import Dict
from src.classes.StudentPresence import StudentPresence


def PrintReport(state: Dict[str, StudentPresence]):
    for name, presences in state.items():
        if not presences.total():
            print(f"{name}: 0 minutes")
            continue
        print(f"{name}: {presences.totalMinutes()} minutes in {presences.total()} days")
