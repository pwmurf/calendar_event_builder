####################################
# NeonCRM --> GCal event automator
# 
# 
# v1.0 - two-day event parsing, duplication detection, logging
# v1.1 - neon_setup and refactor
#
####################################

import logging
from pathlib import Path
from cal_setup import get_calendar_service
from neon_setup import get_neon_service


# set up logging
log_file = Path('/var/log/gcal.log')
logging.basicConfig(filename=log_file, 
                    encoding='utf-8', 
                    format='%(asctime)s %(levelname)-8s %(message)s', 
                    level=logging.DEBUG, datefmt='%Y-%m-%d %H:%M:%S')

# calendar ID
cal_ID = ''

# main 
def main():

  # start log	
  logging.info("Executing script...")
  
  # call neon_setup
  dct = get_neon_service()

  # make a list to iterate over
  out = []
  for pair in dct["listEvents"]["searchResults"]["nameValuePairs"]:
   tmp = {}
   for p in pair["nameValuePair"]:
     tmp[p["name"]] = p["value"]
   out.append(tmp)
  
  # begin looping 
  for event in out:
    evid = (event["Event ID"])
    name = (event["Event Name"])
    cat = (event["Event Category Name"])
    sTime = (event["Event Start Time"])
    eTime = (event["Event End Time"])
    sDate = (event["Event Start Date"])
    eDate = (event["Event End Date"])
    
    # skip existing events based on log entries
    with open(log_file) as f:
      if evid in f.read():
        logging.info("Event already exists in Google Calendar!")
        continue
    
    # skip template events
    if cat != ("Workshops"):
      continue
    
    # parse multiday events 
    if sDate != eDate:
      newDate = eDate
      eDate = sDate      
      # create first date, second will be created in outer loop
      logging.info(evid)
      logging.info(name)
      logging.info(cat)
      logging.info(sTime)
      logging.info(eTime)
      logging.info(sDate)
      logging.info(eDate)

      start = (f"{sDate}T{sTime}")
      logging.info(start)
      end = (f"{eDate}T{eTime}")
      logging.info(end)
      
      # append dates for second day
      sDate = newDate
      eDate = newDate
      
      # call cal_setup
      service = get_calendar_service()
   
      event_result = service.events().insert(calendarId={cal_ID}),
         body={ 
           "summary": name, 
           "description": 'Created by event automation script',
           "start": {"dateTime": start, "timeZone": 'US/Pacific'}, 
           "end": {"dateTime": end, "timeZone": 'US/Pacific'},
          }
      ).execute()

      print("created event")
      print("id: ", event_result['id'])
      print("summary: ", event_result['summary'])
      print("starts at: ", event_result['start']['dateTime'])
      print("ends at: ", event_result['end']['dateTime'])
      print()
  
    logging.info(evid)
    logging.info(name)
    logging.info(cat)
    logging.info(sTime)
    logging.info(eTime)
    logging.info(sDate)
    logging.info(eDate)
    
    start = (f"{sDate}T{sTime}")
    logging.info(start)
    end = (f"{eDate}T{eTime}")
    logging.info(end)

    # call cal_setup
    service = get_calendar_service()

    event_result = service.events().insert(calendarId={cal_ID}),
       body={ 
         "summary": name, 
         "description": 'Created by event automation script',
         "start": {"dateTime": start, "timeZone": 'US/Pacific'}, 
         "end": {"dateTime": end, "timeZone": 'US/Pacific'},
        }
    ).execute()

    print("created event")
    print("id: ", event_result['id'])
    print("summary: ", event_result['summary'])
    print("starts at: ", event_result['start']['dateTime'])
    print("ends at: ", event_result['end']['dateTime'])
    print()
    
  logging.info("...complete!\n")

if __name__ == '__main__':
  main()
    
