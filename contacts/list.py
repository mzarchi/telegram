from telethon.sync import TelegramClient
from telethon import functions
import sys
sys.path.append('../GitHub')
import config.appconfig as ac

with TelegramClient('../sessions/my', ac.api_id, ac.api_hash) as client:
    result = client(functions.contacts.GetContactsRequest(hash=0))
    for i, user in enumerate(result.users):
        txt = f"{i+1}, Id: {user.id}, Mutual: {user.mutual_contact}, Number: {user.phone}, Name: {user.first_name} {user.last_name}"
        print(txt)
