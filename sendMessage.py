"""
Sgoluc Simple Telegram
SendMessage Function
:)
"""

import requests

def sendmessage(message):
    token = '[YOUR_BOT_TOKEN]'
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

sendmessage('[YOUR_MESSAGE]')
