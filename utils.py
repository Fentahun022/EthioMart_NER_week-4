# utils.py

import re

def clean_text(text):
    """
    Cleans and normalizes raw text from Telegram posts.
    
    This function performs the following actions:
    1. Removes all URLs and Telegram links (e.g., http, www, t.me).
    2. Strips user mentions (@username) and hashtags (#tag).
    3. Removes a list of common decorative emojis and special characters.
    4. Replaces multiple newlines and whitespace characters with a single space.
    
    Args:
        text (str): The raw input string from a Telegram post.

    Returns:
        str: The cleaned and normalized string.
    """
    if not isinstance(text, str):
        return ""
    # 1. Remove URLs and Telegram links
    text = re.sub(r'http\S+|www\S+|t\.me/\S+', '', text, flags=re.MULTILINE)
    # 2. Remove user mentions and hashtags
    text = re.sub(r'@\w+|#\w+', '', text)
    # 3. Remove specific decorative characters
    text = re.sub(r'[💥📌💵✅👉📍📞☎️👇✨✔®©™❤🔥]', '', text)
    # 4. Standardize whitespace
    text = re.sub(r'[\n\r\s]+', ' ', text).strip()
    return text