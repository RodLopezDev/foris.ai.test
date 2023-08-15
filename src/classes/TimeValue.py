class TimeValue():
    def __init__(self, string_value: str):
        items = string_value.split(":")
        if len(items) != 2:
            raise Exception('Inconsistent Data')
        if not items[0].isdigit():
            raise Exception('Hours is not a number')
        if not items[1].isdigit():
            raise Exception('Minutes is not a number')

        hours, minutes = map(int, items)
        self.minutes = hours * 60 + minutes
