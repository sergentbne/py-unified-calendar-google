from typing import override

from Calendar.commons import Calendar
import datetime


from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os
from pathlib import Path


class GoogleCalendar(Calendar):
    def __init__(self, credentials_file: Path) -> None:
        super().__init__("Google")
        self._creds: Credentials | None = None
        self._SCOPES = ["https://www.googleapis.com/auth/calendar.readwrite"]

    @override
    def authentificate(self):
        """authentificate with google oauth2"""
        creds: Credentials | None = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists("token.json"):
            creds = Credentials.from_authorized_user_file("token.json", self._SCOPES)

        # If there are no (valid) credentials available, let the user log in.

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    "credentials.json", self._SCOPES
                )
                creds = Credentials(flow.run_local_server(port=15560))
            assert creds is not None
            # Save the credentials for the next run
            with open("token.json", "w") as token:
                token.write(creds.to_json())
        try:
            service = build("calendar", "v3", credentials=creds)

            # Call the Calendar API
            now = datetime.datetime.now(tz=datetime.timezone.utc).isoformat()
            print("Getting the upcoming 10 events")
            events_result = (
                service.events()
                .list(
                    calendarId="primary",
                    timeMin=now,
                    singleEvents=True,
                    orderBy="startTime",
                )
                .execute()
            )
            events = events_result.get("items", [])

            if not events:
                print("No upcoming events found.")
                return

            # Prints the start and name of the next 10 events
            for event in events:
                start = event["start"].get("dateTime", event["start"].get("date"))
                print(start, event["summary"])

        except HttpError as error:
            print(f"An error occurred: {error}")
        return
