#!/usr/bin/python3

from telethon import TelegramClient
from config import config

client = TelegramClient('telethon', config.get('api_id'), config.get('api_hash'))
client.start()

messages = client.get_messages(config.get('channel_from'))

for message in messages:
    if 'Запорізька' in message.message:
        client.forward_messages(config.get('channel_to'), message)
