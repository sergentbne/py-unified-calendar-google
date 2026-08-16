from abc import ABC, abstractmethod

from .options import CalendarEventOptions, CalendarReminderOptions


class Calendar(ABC):
    def __init__(self, source: str | None = None) -> None:
        self._source: str | None = source
        self._events: list[CalendarEvent] = []
        self._is_authentificated: bool = False

    @abstractmethod
    def authentificate(self):
        pass

    def is_authentificated(self):
        return self._is_authentificated

    @abstractmethod
    def sync_calendar(self):
        pass

    # TODO
    # the rest


class CalendarEvent:
    def __init__(self, options: CalendarEventOptions) -> None:
        self.options: CalendarEventOptions = options


class CalendarReminder:
    def __init__(self, options: CalendarReminderOptions) -> None:
        self.options: CalendarReminderOptions = options
