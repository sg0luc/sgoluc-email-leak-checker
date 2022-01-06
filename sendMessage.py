"""
Sgoluc Simple Telegram
SendMessage Function
:)
"""

import requests

def sendmessage(message):
    tokenfile = open('C:\\Users\\lucas\\OneDrive\\Documents\\Projects\\Keys\\telegram_token.txt', 'r')
    token = tokenfile.read()
    method = 'sendMessage'
    print(token)
    try:
        requests.post(
            url='https://api.telegram.org/bot{0}/{1}'.format(token, method),
            data={'chat_id': '[CHANNEL_ID]', 'text': message}
        ).json()
        print("Message sent.")
    except Exception as e:
        print("Message not sent. Reason:", e)

    return message
