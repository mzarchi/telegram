from telethon.sync import TelegramClient
import telethon
import sys
sys.path.append('../GitHub')
import config.appconfig as ac

phone = input("Insert Your Phone: ")
name = phone
client = TelegramClient(
    f'../sessions/{name.replace("+", "")}', ac.api_id, ac.api_hash)
client.connect()
client.send_code_request(phone, force_sms=False)
value = input("Insert Login Code: ")
try:
    client.sign_in(phone, code=value)
except telethon.errors.SessionPasswordNeededError:
    password = input("Insert Your 2-Step Code: ")
    client.sign_in(password=password)
print("Successfully Connect!\nSession created at sessions dir")
