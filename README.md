# NeonCRM --> GCal

This tool leverages Google service account credentials to access its API without authenticating via your browser so the script can be automated from a Linux/Unix device. Note that events in NeonCRM must belong to the same category and multiday parsing is limited to two calendar days. 

Be sure to add your Neon API credentials to **neon_setup.py** and the path to your service account credentials in **cal_setup.py**.

Then you can run the updater script from the CLI:

`python3 update_gcal.py`

