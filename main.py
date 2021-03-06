#!/usr/bin/python3

from telethon import TelegramClient
from raven import Client
from raven.transport.http import HTTPTransport
from config import config
import os
import json


rv_client = Client(config.get('raven_url'), transport=HTTPTransport)

try:
    curwd = os.path.dirname(os.path.realpath(__file__))
    client = TelegramClient(
        os.path.abspath(curwd + '/telethon.session'),
        config.get('api_id'),
        config.get('api_hash')
    )
    client.start()

    sent_ids = json.load(open(curwd + '/sent.json', 'r'))

    msg_from = client.get_messages(config.get('channel_from'))
    msg_to = client.get_messages(config.get('channel_from'))

    for message in msg_from:
        search = config.get('search')
        found = False
        if type(search) == list:
            for term in search:
                found = found or term in message.message
        else:
            found = search in message.message

        if found:
            if message.id not in sent_ids:
                sent_ids.append(message.id)
                client.forward_messages(config.get('channel_to'), message)

    json.dump(sent_ids, open(curwd + '/sent.json', 'w'))
except Exception:
    rv_client.captureException()
