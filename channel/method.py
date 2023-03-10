from telethon.sync import TelegramClient
from colorama import Fore, Style
from datetime import datetime
from os.path import exists
from time import sleep
import time
import json
import os

import sys
sys.path.append('../config')
import appconfig as ac


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
    return int(time.mktime(datetime.strptime(dati, "%Y-%m-%d %H:%M").timetuple()))


def hm(hmvalue):
    return int(time.mktime(datetime.strptime(hmvalue, "%H:%M").timetuple()))


def cttdt(ts, rs=True):
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

    if rs:
        return "{}.{}.{}".format(dt.year, month, day)
    else:
        return "{}{}{}".format(dt.year, month, day)


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


def convert_ts_to_point(timestamp):
    dt = datetime.fromtimestamp(timestamp)
    xy = dt.year - 2013
    match dt.day:
        case 1 | 7 | 13 | 19 | 25:
            xy += 0.16
        case 2 | 8 | 14 | 20 | 26:
            xy += 0.29
        case 3 | 9 | 15 | 21 | 27:
            xy += 0.46
        case 4 | 10 | 16 | 22 | 28:
            xy += 0.59
        case 5 | 11 | 17 | 23 | 29:
            xy += 0.72
        case 6 | 12 | 18 | 24 | 30 | 31:
            xy += 0.85

    ym = dt.month - 1
    if dt.day >= 1 and dt.day <= 6:
        ym += 0.18
    elif dt.day > 6 and dt.day <= 12:
        ym += 0.34
    elif dt.day > 12 and dt.day <= 18:
        ym += 0.50
    elif dt.day > 18 and dt.day <= 24:
        ym += 0.66
    elif dt.day > 24 and dt.day <= 31:
        ym += 0.82

    return xy, ym


def scatter_handel(data):
    sd = {}
    ds = []
    distance_ts = []
    xp = {
        'g1': [],
        'g2': [],
        'g3': [],
        'g4': []
    }

    yp = {
        'g1': [],
        'g2': [],
        'g3': [],
        'g4': []
    }

    for p in data:
        dt = datetime.fromtimestamp(p['s'])
        dname = cttdt(p['s'])
        if dname in sd:
            sd[dname] += 1
        else:
            sd[dname] = 1

    today = convert_ts_to_point(int(time.time()))
    unit_value = max(sd.values()) / 3
    uv2 = unit_value * 2
    uv3 = unit_value * 3

    try:
        for i, p in enumerate(data):
            distance_ts.append(data[i+1]['s'] - data[i]['s'])
            xy, ym = convert_ts_to_point(p['s'])
            dname = cttdt(p['s'])
            dsv = cttdt(p['s'], False)
            if not dsv in ds:
                ds.append(dsv)
                if sd[dname] >= 1 and sd[dname] < uv2:
                    xp['g3'].append(xy)
                    yp['g3'].append(ym)
                elif sd[dname] >= uv2 and sd[dname] < uv3:
                    xp['g2'].append(xy)
                    yp['g2'].append(ym)
                elif sd[dname] >= uv3:
                    xp['g1'].append(xy)
                    yp['g1'].append(ym)

    except:
        pass

    return xp, yp, today, distance_ts


def show_day_distance(distance, day_count):
    distance.sort(reverse=True)
    print("Big distance from two post (day):")
    for i, d in enumerate(distance):
        if (i + 1) > day_count:
            break
        print("{} days".format(int(d / 86400)))


def get_vfm_data(data, match_code, **p):
    """
        | 0 : No limit *
        | 1 : DateTime limit *
        | 2 : TimeRange limit
        | 3 : View limit *
        | 4 : Forward limit *
        | 5 : Mention limit *
        | 6 : ID limit *
        | 7 : is Forward
        | 12 : DateTime & TimeRange limit
        | 13 : DateTime & View limit *
        | 14 : DateTime & Forward limit *
        | 15 : DateTime & Mention limit *
        | 23 : TimeRange & View limit
        | 24 : TimeRange & Forward limit
        | 25 : TimeRange & Mention limit
        | 34 : View & Forward limit *
        | 35 : View & Mention limit *
        | 45 : Forward & Mention limit *
        | 123 : DateTime & TimeRange & View limit
        | 124 : DateTime & TimeRange & Forward limit
        | 125 : DateTime & TimeRange & Mention limit
        | 234 : TimeRange & Favorite & Forward limit
        | 235 : TimeRange & Favorite & Mention limit
        | 345 : View & Forward & Mention limit
        | 1234 : DateTime & TimeRange & View & Forward limit
        | 1235 : DateTime & TimeRange & View & Mention limit
        | 12345 : DateTime & TimeRange & View & Forward & Mention limit
    """

    counter = 1
    result_dict = {
        'cont': [],
        'view': [],
        'forw': [],
        'repl': [],
        'view_dict': {},
        'forw_dict': {},
        'repl_dict': {},
    }

    for post in data:
        append_gate = False
        match match_code:
            case 0:  # No limit
                if (post['w'] == 0):
                    append_gate = True

            case 1:  # DateTime limit
                if (post['w'] == 0):
                    if (post['s'] <= p['datetime_end'] and post['s'] > p['datetime_start']):
                        append_gate = True

            case 3:  # View limit
                if (post['w'] == 0):
                    if (post['v'] <= p['max_view'] and post['v'] > p['min_view']):
                        append_gate = True

            case 4:  # Forward limit
                if (post['w'] == 0):
                    if (post['f'] <= p['max_forward'] and post['f'] > p['min_forward']):
                        append_gate = True

            case 5:  # Mention limit
                if (post['w'] == 0):
                    if (post['m'] <= p['max_mention'] and post['m'] > p['min_mention']):
                        append_gate = True

            case 6:  # ID limit
                if (post['w'] == 0):
                    if (post['i'] <= p['max_id'] and post['i'] > p['min_id']):
                        append_gate = True

            case 13:  # DateTime and View limit
                if (post['w'] == 0):
                    if (post['s'] <= p['datetime_end'] and post['s'] > p['datetime_start'] and
                            post['v'] <= p['max_view'] and post['v'] > p['min_view']):
                        append_gate = True

            case 14:  # DateTime and Forward limit
                if (post['w'] == 0):
                    if (post['s'] <= p['datetime_end'] and post['s'] > p['datetime_start'] and
                            post['f'] <= p['max_forward'] and post['f'] > p['min_forward']):
                        append_gate = True

            case 15:  # DateTime and Mention limit
                if (post['w'] == 0):
                    if (post['s'] <= p['datetime_end'] and post['s'] > p['datetime_start'] and
                            post['m'] <= p['max_mention'] and post['m'] > p['min_mention']):
                        append_gate = True

            case 34:  # View and Forward limit
                if (post['w'] == 0):
                    if (post['v'] <= p['max_view'] and post['v'] > p['min_view'] and
                            post['f'] <= p['max_forward'] and post['f'] > p['min_forward']):
                        append_gate = True

            case 35:  # View and Mention limit
                if (post['w'] == 0):
                    if (post['v'] <= p['max_view'] and post['v'] > p['min_view'] and
                            post['m'] <= p['max_mention'] and post['m'] > p['min_mention']):
                        append_gate = True

            case 45:  # View and Forward limit
                if (post['w'] == 0):
                    if (post['f'] <= p['max_forward'] and post['f'] > p['min_forward'] and
                            post['m'] <= p['max_mention'] and post['m'] > p['min_mention']):
                        append_gate = True

        if append_gate:
            result_dict['cont'].append(counter)
            result_dict['view'].append(post['v'])
            result_dict['forw'].append(post['f'])
            result_dict['repl'].append(post['m'])
            result_dict['view_dict'].update({post['i']: post['v']})
            result_dict['forw_dict'].update({post['i']: post['f']})
            result_dict['repl_dict'].update({post['i']: post['m']})

        counter += 1
    return result_dict


def drv(data):
    view_rate = 1
    forw_rate = 4
    ment_rate = 2

    day_dict = {}
    rte_dict = {}
    viw_dict = {}
    for i in range(0, 96):
        day_dict.update({i: 0})
        rte_dict.update({i: 0})
        viw_dict.update({i: []})

    for p in data:
        day_position = p['s'] % 86400
        day_andis = 0
        if day_position % 900 == 0:
            day_andis = day_position // 900
        else:
            day_andis = (day_position // 900) + 1

        if day_andis == 96:
            day_andis = 0

        day_dict[day_andis] += 1
        rte_dict[day_andis] += ((p['v'] * view_rate) +
                                (p['f'] * forw_rate) + (p['m'] * ment_rate)) / 1000
        viw_dict[day_andis].append(p['v'])
    
    return day_dict, rte_dict, viw_dict
