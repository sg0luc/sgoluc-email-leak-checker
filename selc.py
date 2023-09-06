"""
Sgoluc Email Leak Checker
Author: Lucas "Sg0luc" Silveira
Created: 2023-09-03
Enjoy! <3
"""
import sys
import json
import requests
from pprint import pprint
from sendMessage import sendmessage

# Raw URL: https://leakcheck.io/api?key=YOUR_KEY&check=example@example.com&type=email
# Usage: python selc.py email

api_file = open('/Users/lucas/Documents/Projects/Keys/leakcheck_token.txt', 'r') # Store your LeakCheck token into this file and read it
api_key = api_file.read().strip()

emails_file = open('/Users/lucas/Documents/Projects/Keys/emails.txt', 'r') # Store your email list into this file
emails_list = emails_file.readlines()

sent_messages_file = '/Users/lucas/Documents/Projects/Keys/sent_messages.json' # Store already sent messages into 'sent_messages.json' file, to avoid realerting
sent_messages = {}

# Try to load 'sent_messages.json' file
try: 
    with open(sent_messages_file, 'r') as file:
        sent_messages = json.load(file)
except (FileNotFoundError, json.decoder.JSONDecodeError):
    pass

# Search for each email in 'emails.txt' file
for e in emails_list:
    print('Results for '+e)
    try:
        request = requests.get('https://leakcheck.io/api?key=' + api_key + '&type=email&check=' + e)
        response = json.loads(request.text)

        # Create initial message variable for each email and leak
        for i in response['result']:
            message = '🚨 Sgoluc Leak Check - Novo Vazamento Identificado 🚨' + '\n🔐 Credencial: ' + i['line'] + '\n'

            # Verify if 'sources' exists and is not empty
            if 'sources' in i and i['sources']:
                sources_message = '🔍 Fonte(s): ' + ', '.join(i['sources']) + '\n'
                message += sources_message

            message += '🔥 Último vazamento: ' + i['last_breach']

            # Create keys with email, source and last breach date to input into json file
            keys = (e.strip(), ', '.join(i['sources']), i['last_breach'])

            # Convert tuple into string to use it as key
            keys_str = str(keys)

            # Verify if message is already sent
            if keys_str not in sent_messages:
                # Send message to Telegram
                sendmessage(message)
                # Print message to screen
                #print(message)
                sent_messages[keys_str] = message
        sleep(5)
    except Exception as e:
        print('Request not sent. Reason:', e, '\n')

# Save sent messages into sent_messages.json file
with open(sent_messages_file, 'w') as savesentmessages:
    json.dump(sent_messages, savesentmessages)

