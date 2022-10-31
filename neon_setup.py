#####
#
# Get next month's events from NeonCRM
#
#####

import calendar
import time
import datetime
import json
import requests

apiKey = ''
orgid = ''

def get_neon_service():
  # get session ID for API 
  response = requests.get(f"https://api.neoncrm.com/neonws/services/api/common/login?login.apiKey={apiKey}&login.orgid={orgid}").json()
  token = response['loginResponse']['userSessionId']

  #  get dates for events query, stating with today
  first_day = time.strftime('%Y-%m-%d')
  
  # grab day for next month 
  next_day = int(time.strftime('%d'))

  # year and month to pass to calendar
  year = int(time.strftime('%Y'))
  month = int(time.strftime('%m'))
  month = month + 1
  
  # calendar to get first day of next month
  limit = calendar.monthrange(year, month)
  last = datetime.date(year, month, next_day)
  last_day = last.strftime('%Y-%m-%d')    

  # get events list for target month
  url = f"https://api.neoncrm.com/neonws/services/api/event/listEvents?responseType=json&userSessionId={token}&outputfields.idnamepair.name=Event%20ID&outputfields.idnamepair.name=Event%20ID&outputfields.idnamepair.name=Event%20Name&outputfields.idnamepair.name=Event%20Category%20Name&outputfields.idnamepair.name=Event%20Start%20Date&outputfields.idnamepair.name=Event%20Start%20Time&outputfields.idnamepair.name=Event%20End%20Date&outputfields.idnamepair.name=Event%20End%20Time&searches.search.key=Event%20Start%20Date&searches.search.searchOperator=GREATER_THAN&searches.search.value={first_day}&searches.search.key=Event%20End%20Date&searches.search.searchOperator=LESS_THAN&searches.search.value={last_day}"
  dct = requests.get(url).json()
  return dct
  
  