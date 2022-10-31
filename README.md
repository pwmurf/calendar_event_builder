# NeonCRM --> GCal

## This tool leverages Google service account credentials to access its API without authenticating via browser so it script can be run from a Linux/Unix automation server.

Be sure to add these credentials to **neon_setup.py**

`apiKey = ''
 orgid = ''` 

And the path to your service account credentials in **cal_setup.py**

`CREDENTIALS_FILE = 'path/to/service_creds.json'`

Then you can run the updater script from the CLI

`python3 update_gcal.py`

Note that events in NeonCRM must belong to the same category and multiday parsing is limited to two calendar days. 