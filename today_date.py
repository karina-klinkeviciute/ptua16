import datetime
from unittest.mock import Mock


def is_weekday():
    today = datetime.datetime.today()
    # .weekday() returns an integer: 0 is Monday, 6 is Sunday
    return 0 <= today.weekday() < 5

tuesday = datetime.datetime(year=2019, month=1, day=1)
saturday = datetime.datetime(year=2019, month=1, day=5)

datetime = Mock()

datetime.datetime.today.return_value = tuesday

print(is_weekday())

datetime.datetime.today.return_value = saturday

print(is_weekday())