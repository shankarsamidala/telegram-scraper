# index.py

import os
import asyncio
from telethon import TelegramClient
from config import get_channels, get_client
from cleaner import clean_deal_message

async def fetch_and_clean():
    client = get_client()
    await client.start(os.environ['PHONE_NUMBER'])

    deals = []
    for peer in get_channels():
        try:
            messages = await client.get_messages(peer, limit=10)
            for msg in messages:
                if msg.raw_text:
                    data = clean_deal_message(msg.raw_text)
                    deals.append(data)
                    print(data)  # For now, just log
        except Exception as e:
            print(f"Error fetching from {peer.channel_id}: {e}")

    await client.disconnect()

# Appwrite handler
def main(req, res):
    asyncio.run(fetch_and_clean())
    return res.json({"status": "Deals fetched and cleaned."})
