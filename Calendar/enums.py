from enum import Enum


class CalendarEventImportance(Enum):
    NORMAL = 1
    IMPORTANT = 2
    VERY_IMPORTANT = 3
    URGENT = 4


class CalendarEventRepeat(Enum):
    NONE = 1
    DAILY = 2
    WEEKLY = 3
    MONTHLY = 4
    YEARLY = 5
