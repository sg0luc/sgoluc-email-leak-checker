"""
Sgoluc LeakCheck Script
Only works with linked IPs!
"""

import sys
import json
import requests
from pprint import pprint

# Raw URL: https://leakcheck.net/api?key=YOUR_KEY&check=example@example.com&type=email
# Usage: python leakCheck.py [TYPE] [SEARCH]

api_file = open('leakcheck_api.txt', 'r')
api_key = api_file.read()

search_type = sys.argv[1]
check = sys.argv[2]

try:
    request = requests.get('https://leakcheck.net/api?key=' + api_key + '&check=' + check + '&type=' + search_type)
    response_json = json.loads(request.text)
    response = response_json['result']
    pprint(response)

except Exception as e:
    print('Request not sent. Reason:', e)