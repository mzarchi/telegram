from telethon.sync import TelegramClient
import telethon

phone = input("Insert Your Phone: ")
name = phone
client = TelegramClient(
    f'../sessions/{name.replace("+", "")}', 'api_id', 'api_hash')
client.connect()
client.send_code_request(phone, force_sms=False)
value = input("Insert Login Code: ")
try:
    client.sign_in(phone, code=value)
except telethon.errors.SessionPasswordNeededError:
    password = input("Insert Your 2-Step Code: ")
    client.sign_in(password=password)
print("Successfully Connect!")
