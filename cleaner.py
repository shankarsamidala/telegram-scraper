# cleaner.py

import re

def clean_deal_message(message: str):
    # Remove emojis and unwanted characters
    clean_text = re.sub(r'[^\w\s:/.-]', '', message)
    clean_text = re.sub(r'\s+', ' ', clean_text).strip()

    # Extract price
    price_match = re.search(r'(?i)(?:rs\.?|deal\s?@?|price\s?@?)\s?[:₹]?\s?([\d,]+)', clean_text)
    price = price_match.group(1).replace(',', '') if price_match else None

    # Extract URLs
    urls = re.findall(r'https?://[^\s]+', clean_text)

    # Extract title (first meaningful line)
    lines = message.split('\n')
    title = ''
    for line in lines:
        if 'http' not in line and len(line.strip()) > 10:
            title = line.strip()
            break

    return {
        'title': title,
        'price': price,
        'urls': urls,
        'raw': message
    }
