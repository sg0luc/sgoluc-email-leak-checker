# SELC (Sgoluc Email Leak Checker)
Howdy! I've just created this project with pure studying purposes, so I got the idea to monitor my friends and family emails at an automation level: this script uses the [LeakCheck](https://leakcheck.net) API to search - _for a specific list or range of emails set on 'emails.txt' file_ - for leaks involving this emails.

## Pre-requisites
To use this automation script, you should have a LeakCheck account and retrieve your API token (mine is the lifetime one)

## Usage
You can use the script manually, but I prefer to create a scheduled task on Windows so I can automatically run it weekly:
```
python selc.py
```
