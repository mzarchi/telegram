from telethon.sync import TelegramClient
from colorama import Fore, Style
from datetime import datetime
from os.path import exists
from time import sleep
import appconfig as ac
import time
import json
import os


def fe(name):
    file_exists = exists(f"ChannelData/{name}.json")
    if file_exists is True:
        data = rjf(name)
        start_post = cttdt(data[0]['s'])
        end_post = cttdt(data[-1]['s'])
        dates = f"[from:{Fore.CYAN + Style.BRIGHT}{start_post}{Style.RESET_ALL}, to:{Fore.CYAN + Style.BRIGHT}{end_post}{Style.RESET_ALL}]"
        channel_name = f"{Fore.RED + Style.BRIGHT}{name}{Style.RESET_ALL}"
        post_counts = '{:,}'.format(len(data)) + ' posts'
        print("{} {} ({})".format(dates, channel_name, post_counts))
        return rjf(name)
    else:
        print("App does not have any json file!")
        print("Use below cell to get channel data ..")


async def get_data(username, count):
    data = []
    async with TelegramClient('../sessions/my', ac.api_id, ac.api_hash) as client:
        print("Start streaming ...")
        for item in await client.get_messages(username, limit=count):
            if item.views is not None:
                frw = 0
                try:
                    try:
                        replies = item.replies.replies
                    except:
                        replies = 0

                    if (item.fwd_from != None):
                        frw = 1

                    post_detais = {
                        'i': item.id,
                        's': int(item.date.timestamp()),
                        'v': item.views,
                        'f': item.forwards,
                        'm': replies,
                        'w': frw,
                    }

                    data.append(post_detais)
                except:
                    print("Error")
                    pass

    data.reverse()
    print(f"\nData size: {len(data)}")
    time.sleep(1)
    wjf(username, data)
    return data


def wjf(username, data):
    txt = json.dumps(data)
    f = open(f"ChannelData/{username}.json", "a")
    f.write(txt)
    f.close()


def rjf(username):
    f = open(f"ChannelData/{username}.json", "r")
    return json.loads(f.read())


def ts(dati):
    return int(time.mktime(datetime.datetime.strptime(dati, "%Y-%m-%d %H:%M").timetuple()))


def hm(hmvalue):
    return int(time.mktime(datetime.datetime.strptime(hmvalue, "%H:%M").timetuple()))


def cttdt(ts):
    dt = datetime.fromtimestamp(ts)
    month = ""
    if dt.month < 10:
        month = f"0{dt.month}"
    else:
        month = dt.month

    day = ""
    if dt.day < 10:
        day = f"0{dt.day}"
    else:
        day = dt.day
    return "{}.{}.{}".format(dt.year, month, day)


def ShowChannelList():
    fv = ""
    path = 'ChannelData/'
    dirs = os.listdir(path)
    for i, d in enumerate(dirs):
        size = os.path.getsize(path + d) / 1024
        if size > 100:
            size = size / 1024
            fv = "MB"
        else:
            fv = "kB"

        data = rjf(d.replace('.json', ''))
        start_post = cttdt(data[0]['s'])
        end_post = cttdt(data[-1]['s'])
        dates = f"[from:{Fore.CYAN + Style.BRIGHT}{start_post}{Style.RESET_ALL}, to:{Fore.CYAN + Style.BRIGHT}{end_post}{Style.RESET_ALL}]"
        channel_name = f"{Fore.RED + Style.BRIGHT}{d.replace('.json','')}{Style.RESET_ALL}"
        post_counts = '{:,}'.format(len(data)) + ' posts,'
        value = '{:,}'.format(round(size, 2)) + f" {fv} )"
        print("{}:{} {:<40s} ( {:<15s} {:<10s} ".format(
            i+1, dates, channel_name, post_counts, value))
        sleep(0.3)
