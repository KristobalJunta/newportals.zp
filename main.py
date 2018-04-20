#!/usr/bin/python3

from telethon import TelegramClient
from config import config

client = TelegramClient('telethon', config.get('api_id'), config.get('api_hash'))
client.start()

msg_from = client.get_messages(config.get('channel_from'))
msg_to = client.get_messages(config.get('channel_from'))

for message in msg_from:
    if 'Запорізька' in message.message:
        if message not in msg_to:
            client.forward_messages(config.get('channel_to'), message)
