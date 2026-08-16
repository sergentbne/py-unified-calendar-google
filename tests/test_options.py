import datetime
from pathlib import Path

import pytest

from Calendar.enums import CalendarEventImportance, CalendarEventRepeat
from Calendar.exceptions import InvalidAttachementsError, InvalidEmailError, InvalidUrlError
from Calendar.options import CalendarEventOptions, CalendarReminderOptions

DUMMY_ATTACHMENT = Path(__file__).parent / "data" / "attachments" / "dummy.txt"


def dt():
    return datetime.datetime(2026, 1, 1, 9, 0)


def test_event_options_minimal():
    start = dt()
    opts = CalendarEventOptions(start=start, end=start + datetime.timedelta(hours=1), event_name="Meeting")
    assert opts.event_name == "Meeting"
    assert opts.all_day is False
    assert opts.repeat == CalendarEventRepeat.NONE
    assert opts.invitees_email is None


def test_event_options_end_before_start_raises():
    start = dt()
    end = start - datetime.timedelta(hours=1)
    with pytest.raises(ValueError):
        CalendarEventOptions(start=start, end=end, event_name="Meeting")


def test_event_options_invalid_email_raises():
    start = dt()
    with pytest.raises(InvalidEmailError):
        CalendarEventOptions(
            start=start,
            end=start + datetime.timedelta(hours=1),
            event_name="Meeting",
            invitees_email=("valid@example.com", "not-an-email"),
        )


def test_event_options_invalid_url_raises():
    start = dt()
    with pytest.raises(InvalidUrlError):
        CalendarEventOptions(
            start=start,
            end=start + datetime.timedelta(hours=1),
            event_name="Meeting",
            url="not a url",
        )


def test_reminder_options_minimal():
    expire = dt()
    opts = CalendarReminderOptions(expire_time=expire, reminder_name="Reminder")
    assert opts.reminder_name == "Reminder"
    assert opts.importance == CalendarEventImportance.NORMAL
    assert opts.flag is False


def test_reminder_options_invalid_email_raises():
    expire = dt()
    with pytest.raises(InvalidEmailError):
        CalendarReminderOptions(
            expire_time=expire,
            reminder_name="Reminder",
            invitees_email=("bad",),
        )


def test_event_options_valid_attachments(tmp_path):
    attachment = tmp_path / "present.txt"
    attachment.touch()
    start = dt()
    opts = CalendarEventOptions(
        start=start,
        end=start + datetime.timedelta(hours=1),
        event_name="Meeting",
        attachements=[attachment],
    )
    assert opts.attachements == [attachment]


def test_event_options_missing_attachment_raises(tmp_path):
    start = dt()
    present = tmp_path / "present.txt"
    present.touch()
    missing = tmp_path / "missing.txt"
    with pytest.raises(InvalidAttachementsError) as exc:
        CalendarEventOptions(
            start=start,
            end=start + datetime.timedelta(hours=1),
            event_name="Meeting",
            attachements=[present, missing],
        )
    assert exc.value.invalid_attachements == [missing]


def test_event_options_dummy_attachment_ok():
    start = dt()
    opts = CalendarEventOptions(
        start=start,
        end=start + datetime.timedelta(hours=1),
        event_name="Meeting",
        attachements=[DUMMY_ATTACHMENT],
    )
    assert opts.attachements == [DUMMY_ATTACHMENT]


def test_reminder_options_missing_attachment_raises(tmp_path):
    expire = dt()
    missing = tmp_path / "missing.txt"
    with pytest.raises(InvalidAttachementsError):
        CalendarReminderOptions(
            expire_time=expire,
            reminder_name="Reminder",
            attachements=[missing],
        )