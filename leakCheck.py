"""
Sgoluc LeakCheck Script
Only works with linked IPs!
"""

import sys
import json
import requests
from pprint import pprint
from sendMessage import sendmessage

# Raw URL: https://leakcheck.net/api?key=YOUR_KEY&check=example@example.com&type=email
# Usage: python leakCheck.py [TYPE] [SEARCH]

api_file = open('C:\\Users\\lucas\\OneDrive\\Documents\\Projects\\Keys\\leakcheck_apikey.txt', 'r')
api_key = api_file.read()

search_type = sys.argv[1]
check = sys.argv[2]

try:
    request = requests.get('https://leakcheck.net/api?key=' + api_key + '&check=' + check + '&type=' + search_type)
    response = json.loads(request.text)
    for i in response['result']:
        pprint(i)
        sendmessage(i)
except Exception as e:
    print('Request not sent. Reason:', e)