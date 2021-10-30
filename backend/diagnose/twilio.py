# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


def send_msg(tousr,body):
    account_sid = 'SK7408a1a9c65e8f94ac82d0f0eef4075e'
    auth_token = 'e1fadb1c019c793c4068c2c401f94d52'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body=body,
            messaging_service_sid='MG9752274e9e519418a7406176694466fa',
            to=tousr
        )

    print(message.sid)
