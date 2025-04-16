# config.py

from telethon import TelegramClient
from telethon.tl.types import InputPeerChannel
import os

# Hardcoded Telegram deal channels (ID + access_hash)
channel_info_list = [
    {'id': 1563971114, 'access_hash': -8631643076697037864},
    {'id': 1422047391, 'access_hash': 731058964822613751},
    {'id': 1358642095, 'access_hash': 6250756390186018524},
    {'id': 2125169945, 'access_hash': -313052371522893206},
    {'id': 1216327422, 'access_hash': 3737021600897267789},
    {'id': 1493719413, 'access_hash': 866565995579559335},
    {'id': 2291280551, 'access_hash': -5607206976301071189}
]

def get_client():
    return TelegramClient(
        'appwrite_session',
        int(os.environ['API_ID']),
        os.environ['API_HASH']
    )

def get_channels():
    return [InputPeerChannel(ch['id'], ch['access_hash']) for ch in channel_info_list]
