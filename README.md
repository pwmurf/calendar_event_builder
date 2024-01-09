# NeonCRM --> GCal

NeonCRM is a popular non-profit platform that does not have a native Google Calendar integration. So this app does it for you!

This tool leverages Google service account credentials to access its API without authenticating via your browser so the script can be automated from a Linux/Unix device, and could also be slightly modified to be run by Task Manager on Windows. 

Note that events in NeonCRM must belong to the same category and multiday parsing is limited to two calendar days. 

More about setting up service account credentials: https://cloud.google.com/iam/docs/service-account-creds

This tool is using v1 of Neon's API: https://developer.neoncrm.com/api/

Be sure to add your Neon API credentials to **neon_setup.py** and the path to your service account credentials in **cal_setup.py**. The token will be stored in the working directory. 

Then you can run the updater script from the CLI:

`python3 update_gcal.py`

