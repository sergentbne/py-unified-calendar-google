import pytest

from Calendar.enums import CalendarEventImportance, CalendarEventRepeat


def test_importance_members_order():
    assert list(CalendarEventImportance) == [
        CalendarEventImportance.NORMAL,
        CalendarEventImportance.IMPORTANT,
        CalendarEventImportance.VERY_IMPORTANT,
        CalendarEventImportance.URGENT,
    ]


def test_importance_values():
    assert CalendarEventImportance.NORMAL.value == 1
    assert CalendarEventImportance.IMPORTANT.value == 2
    assert CalendarEventImportance.VERY_IMPORTANT.value == 3
    assert CalendarEventImportance.URGENT.value == 4


def test_repeat_members_order():
    assert list(CalendarEventRepeat) == [
        CalendarEventRepeat.NONE,
        CalendarEventRepeat.DAILY,
        CalendarEventRepeat.WEEKLY,
        CalendarEventRepeat.MONTHLY,
        CalendarEventRepeat.YEARLY,
    ]


def test_repeat_values():
    assert CalendarEventRepeat.NONE.value == 1
    assert CalendarEventRepeat.DAILY.value == 2
    assert CalendarEventRepeat.WEEKLY.value == 3
    assert CalendarEventRepeat.MONTHLY.value == 4
    assert CalendarEventRepeat.YEARLY.value == 5