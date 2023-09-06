# Anchor migration script 
In WNT 3.0 anchors are automatically deducted from locations/is_approved/diagnostics_role, 
but that method is inaccurate. In WNT 4.0 there is specific flag 'is_anchor' in node metadata. 
This tool has two python scripts, first to fetch anchor data from 3.0 to JSON file, 
which can then be manually changed if needed, and then updated with second script to 4.0 backend.

## Usage
Precondition to run export script is to have 3.0 backend with enough uptime, so rtsituation has every node in memory. 
Precondition to run import script is to have data.json with exported data.

### To export data to JSON file
Set desired configurations to settings.yml (or pass argument `--settings file_name`). Repository has [example.yml](example_settings.yml)

```python
make pkg_requirements
.env/bin/python3 anchordataexporter.py
```

Now you have data.json. Change manually if necessary

### To import JSON data to 4.0 backend
Set desired configurations to settings.yml (or pass argument `--settings file_name`). Repository has [example.yml](example_settings.yml)

```python
make pkg_requirements
.env/bin/python3 anchordataimporter.py
```

## Exit Codes
Script returns exit code every time it is run. Defined in [here](exitcode.py). 

More exact definitions:

0. Success
1. Undefined exception - See logfile for more information
2. Login failed - Login to your backend authentication service failed, check credentials
3. Set anchor failed - Setting data to 4.0 backend failed, see logfile for more information
4. Rtsituation login failed - Login to your backend rtsituation service failed, check credentials
5. Initial data failure - Receiving data from 3.0 backend failed before all data was received, see logfile for more information
6. Data missing - While exporting: no anchors received and data.json is empty. While importing: data.json file not found for importing
7. Unprocessed data - Some data not sent to 4.0 backend, see logfile for more information
8. Websocket error - Websocket connection had some error, see logfile for more information
9. Receive data timeout - No new initial data received between timeout period from 3.0 backend even that all data was not yet received.


