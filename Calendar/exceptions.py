from pathlib import Path
from typing import final


@final
class InvalidEmailError(Exception):
    def __init__(self, invalid_emails: list[str]):
        super().__init__(
            f"One or more provided email is invalid: {', '.join(invalid_emails)}"
        )
        self.invalid_emails = invalid_emails


@final
class LocationNotFoundError(Exception):
    def __init__(
        self,
        location: str,
    ):
        super().__init__(
            f"The requested location has not been found: {location} has not been found"
        )
        self.location = location


@final
class InvalidUrlError(Exception):
    def __init__(
        self,
        url: str,
    ):
        super().__init__(f"The inputed email is invalid: {url} is invalid")
        self.url = url


@final
class InvalidAttachementsError(Exception):
    def __init__(
        self,
        invalid_attachements: list[Path],
    ):
        super().__init__(
            f"One or more than one attachement(s) is invalid: {', '.join(map(lambda x: str(x), invalid_attachements))}"
        )
        self.invalid_attachements = invalid_attachements
