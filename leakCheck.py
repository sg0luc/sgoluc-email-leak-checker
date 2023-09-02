"""
Sgoluc LeakCheck Test Script
Only works with linked IPs!
"""

import sys
import json
import requests
from pprint import pprint
from sendMessage import sendmessage

# Raw URL: https://leakcheck.io/api?key=YOUR_KEY&check=example@example.com&type=email
# Usage: python leakCheckTest.py [TYPE]

api_file = open('C:\\Users\\lucas\\OneDrive\\Documents\\Projects\\Keys\\leakcheck_token.txt', 'r')
api_key = api_file.read()

emails_file = open('C:\\Users\\lucas\\OneDrive\\Documents\\Projects\\Keys\\emails.txt', 'r')
emails_list = emails_file.readlines()

search_type = sys.argv[1]

for e in emails_list:
    try:
        request = requests.get('https://leakcheck.io/api?key=' + api_key + '&type=' + search_type + '&check=' + e)
        response = json.loads(request.text)
        print('Results for', e, ':')
        for i in response['result']:
            pprint(i)
    except Exception as e:
        print('Request not sent. Reason: ', e)
