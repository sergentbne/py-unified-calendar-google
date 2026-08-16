from pathlib import Path

import pytest

from Calendar.exceptions import (
    InvalidAttachementsError,
    InvalidEmailError,
    InvalidUrlError,
    LocationNotFoundError,
)


@pytest.mark.parametrize(
    "emails,expected",
    [
        (["a@b.com"], "One or more provided email is invalid: a@b.com"),
        (
            ["a@b.com", "bad"],
            "One or more provided email is invalid: a@b.com, bad",
        ),
    ],
)
def test_invalid_email_error(emails, expected):
    err = InvalidEmailError(emails)
    assert str(err) == expected
    assert err.invalid_emails == emails


def test_location_not_found_error():
    err = LocationNotFoundError("Paris XX")
    assert str(err) == "The requested location has not been found: Paris XX has not been found"
    assert err.location == "Paris XX"


def test_invalid_url_error():
    err = InvalidUrlError("not a url")
    assert str(err) == "The inputed email is invalid: not a url is invalid"
    assert err.url == "not a url"


def test_invalid_attachements_error():
    paths = [Path("a.txt"), Path("b.txt")]
    err = InvalidAttachementsError(paths)
    assert str(err) == "One or more than one attachement(s) is invalid: a.txt, b.txt"
    assert err.invalid_attachements == paths