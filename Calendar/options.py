import datetime
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import geopy

from .exceptions import (
    InvalidAttachementsError,
    InvalidEmailError,
    InvalidUrlError,
    LocationNotFoundError,
)
from .enums import (
    CalendarEventRepeat,
    CalendarEventImportance,
)


@dataclass(frozen=True)
class CalendarEventOptions:
    start: datetime.datetime
    end: datetime.datetime
    event_name: str
    all_day: bool = False
    repeat: CalendarEventRepeat = CalendarEventRepeat.NONE
    invitees_email: tuple[str] | None = None
    location: str | None = None
    notes: str | None = None
    url: str | None = None
    # Lazy load the attachements when they are required
    attachements: list[Path] | None = None

    def __post_init__(self):
        def is_email_valid(email: str):
            EMAIL_VALIDATION_REGEX = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}"
            return bool(re.fullmatch(EMAIL_VALIDATION_REGEX, email))

        def is_url_valid(url: str):
            URL_VALIDATION_REGEX = r"^https?:\/\/(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,63}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&\/=]*)$"
            return bool(re.fullmatch(URL_VALIDATION_REGEX, url))

        if (self.end - self.start) != abs(self.end - self.start):
            raise ValueError(
                f"The endtime must not be before the startime: ({self.start=}, {self.end=})"
            )
        if self.invitees_email and not all(map(is_email_valid, self.invitees_email)):
            # Filter only the invalid emails
            raise InvalidEmailError(
                list(
                    filter(
                        lambda mail: not is_email_valid(mail),
                        self.invitees_email,
                    ),
                )
            )
        if self.location:
            geolocator = geopy.Nominatim()
            found_location: Any | None = geolocator.geocode(self.location)
            if found_location is None:
                raise LocationNotFoundError(self.location)
        if self.url and not is_url_valid(self.url):
            raise InvalidUrlError(self.url)
        if self.attachements and not all(x.exists() for x in self.attachements):
            raise InvalidAttachementsError(
                list(
                    filter(
                        lambda attachement: not attachement.exists(),
                        self.attachements,
                    ),
                )
            )


@dataclass(frozen=True)
class CalendarReminderOptions:
    expire_time: datetime.datetime
    reminder_name: str
    repeat_frequency: CalendarEventRepeat = CalendarEventRepeat.NONE
    tags: tuple[str] | None = None
    flag: bool = False
    importance: CalendarEventImportance = CalendarEventImportance.NORMAL
    invitees_email: tuple[str] | None = None
    location: str | None = None
    notes: str | None = None
    url: str | None = None
    # Lazy load the attachements when they are required
    attachements: list[Path] | None = None

    def __post_init__(self):
        def is_email_valid(email: str):
            EMAIL_VALIDATION_REGEX = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}"
            return bool(re.fullmatch(EMAIL_VALIDATION_REGEX, email))

        def is_url_valid(url: str):
            URL_VALIDATION_REGEX = r"^https?:\/\/(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,63}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&\/=]*)$"
            return bool(re.fullmatch(URL_VALIDATION_REGEX, url))

        if self.invitees_email and not all(map(is_email_valid, self.invitees_email)):
            # Filter only the invalid emails
            raise InvalidEmailError(
                list(
                    filter(
                        lambda mail: not is_email_valid(mail),
                        self.invitees_email,
                    ),
                )
            )
        if self.location:
            geolocator = geopy.Nominatim()
            found_location: Any | None = geolocator.geocode(self.location)
            if found_location is None:
                raise LocationNotFoundError(self.location)
        if self.url and not is_url_valid(self.url):
            raise InvalidUrlError(self.url)
        if self.attachements and not all(x.exists() for x in self.attachements):
            raise InvalidAttachementsError(
                list(
                    filter(
                        lambda attachement: not attachement.exists(),
                        self.attachements,
                    ),
                )
            )
