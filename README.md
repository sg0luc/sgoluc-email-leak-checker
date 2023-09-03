# SELC (Sgoluc Email Leak Checker)
Howdy! I've just created this project with pure studying purposes, so I got the idea to monitor my friends and family emails at an automation level: this script uses the [LeakCheck](https://leakcheck.net) API to search - _for a specific list or range of emails set on 'emails.txt' file_ - for leaks involving this emails.

## Pre-requisites
- A LeakCheck account and retrieve your API token - _mine is the lifetime one_
- A Telegram Bot in a group and set up at the sendMessage.py file - _if you don't want to use the Telegram Bot feature, you have to comment the line #58 and uncomment the line #60 on selc.py file_

## Usage
You can use the script manually, but I prefer to create a scheduled task on Windows so I can automatically run it weekly:
```
python selc.py
```
