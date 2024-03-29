"""
Simple Telegram SendMessage Function
:)
"""
import requests

def sendmessage(message):
    tokenfile = open('/Users/lucas/Documents/Projects/Keys/telegram_token.txt', 'r')
    token = tokenfile.read().strip()
    method = 'sendMessage'
    try:
        requests.post(
            url='https://api.telegram.org/bot{0}/{1}?'.format(token, method),
            data={'chat_id': '-960809758', 'text': message}
        ).json()
        print("Message sent.")
    except Exception as e:
        print("Message not sent. Reason: ", e)

    return message
