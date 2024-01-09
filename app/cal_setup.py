#####
#
# This script has been reworked from https://github.com/karenapp/google-calendar-python-api
# to use service account authentication and avoid browser redirect for automation
#
#####

import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.oauth2 import service_account
from oauth2client.service_account import ServiceAccountCredentials


# Download JSON credentials from https://console.cloud.google.com/apis/ and update path
CREDENTIALS_FILE = 'path/to/service_creds.json'


def get_calendar_service():
   creds = None
   # The file token.pickle stores the user's access and refresh tokens, and is
   # created automatically when the authorization flow completes for the first
   # time.
   if os.path.exists('token.pickle'):
       with open('token.pickle', 'rb') as token:
           creds = pickle.load(token)
   # If there are no (valid) credentials available, let the user log in.
   if not creds or not creds.valid:
       if creds and creds.expired and creds.refresh_token:
           creds.refresh(Request())
       else:
           creds = service_account.Credentials.from_service_account_file(
               CREDENTIALS_FILE)  

       # Save the credentials for the next run
       with open('token.pickle', 'wb') as token:
           pickle.dump(creds, token)

   service = build('calendar', 'v3', credentials=creds)
   return service
   
