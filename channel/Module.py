import os
import sys
import csv
import time
import pandas as pd

from os.path import exists
from datetime import datetime
from colorama import Fore, Style


class Time:
    @classmethod
    def timestamp(cls, dt, pattern):
        # Convert datetime to timestamp
        return int(time.mktime(datetime.strptime(dt, pattern).timetuple()))

    @classmethod
    def fromtimestamp(cls, timestamp):
        # Get timestamp and set datetime obj
        return datetime.fromtimestamp(timestamp)

    @classmethod
    def sleep(cls, second):
        time.sleep(second)

    @classmethod
    def time(cls):
        return time.time()

    @classmethod
    def points(cls, dt):
        # Convert timestamp to point
        # dt = [2023, 03, 25, 14, 37, 50]
        xy = int(dt[0]) - 2013
        match int(dt[2]):
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

        ym = int(dt[1]) - 1
        day = int(dt[2])
        if day >= 1 and day <= 6:
            ym += 0.18
        elif day > 6 and day <= 12:
            ym += 0.34
        elif day > 12 and day <= 18:
            ym += 0.50
        elif day > 18 and day <= 24:
            ym += 0.66
        elif day > 24 and day <= 31:
            ym += 0.82

        return xy, ym

    @classmethod
    def dtnow(cls):
        return datetime.now()

    @classmethod
    def dtlist(cls, dtobj):
        datetime_list = []
        datetime_list.append(dtobj.strftime("%Y-%m-%d"))
        datetime_list.append(dtobj.strftime("%H:%M:%S"))
        return datetime_list

    @classmethod
    def reformat_time(cls, first_time, second_time):
        # Convert 20:08:54 to 200854
        ft = first_time.replace(":", "")
        st = second_time.replace(":", "")
        return int(ft), int(st)


class File:
    @classmethod
    def write(cls, username, field_name, data):
        with open(f'ChannelData/{username}.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=field_name)
            writer.writeheader()
            writer.writerows(data)

        #txt = json.dumps(data)
        #f = open(f"ChannelData/{username}.json", "a")
        # f.write(txt)
        # f.close()

    @classmethod
    def read(cls, username):
        return pd.read_csv(f'ChannelData/{username}')

    @classmethod
    def show(cls):
        path = 'ChannelData/'
        dirs = os.listdir(path)
        if ".ipynb_checkpoints" in dirs:
            dirs.remove(".ipynb_checkpoints")

        dirs = sorted(dirs, key=str.casefold)
        for i, d in enumerate(dirs):
            if d != ".ipynb_checkpoints.json":
                size = os.path.getsize(path + d) / 1024
                if size > 100:
                    size = size / 1024
                    fv = "MB"
                else:
                    fv = "kB"

            data = File.read(d)
            start_date = data['date'].iloc[0]
            end_date = data['date'].iloc[-1]
            dates = f"[from:{Fore.CYAN + Style.BRIGHT}{start_date}{Style.RESET_ALL}, to:{Fore.CYAN + Style.BRIGHT}{end_date}{Style.RESET_ALL}]"
            channel_name = f"{Fore.RED + Style.BRIGHT}{d.replace('.json','')}{Style.RESET_ALL}"
            post_counts = '{:,}'.format(len(data)) + ' posts,'
            value = '{:,}'.format(round(size, 2)) + f" {fv} )"
            print("{}:{} {:<40s} ( {:<15s} {:<10s} ".format(
                cls.__setnum(i+1), dates, channel_name, post_counts, value))
            time.sleep(0.2)

    @classmethod
    def get(cls, name):
        file_exists = exists(f"ChannelData/{name}.csv")
        if file_exists is True:
            data = File.read(f"{name}.csv")
            example_csv = data[["date", "time", "unixtime", "id", "view"]]
            head1 = example_csv.head()
            tail1 = example_csv.tail()
            frames = [head1, tail1]
            print(pd.concat(frames))
            return data
        else:
            print("App does not have any json file!")
            print("Use below cell to get channel data ..")

    def __setnum(number):
        if number >= 1 and number < 10:
            return f"00{number}"
        elif number >= 10 and number < 100:
            return f"0{number}"
        elif number >= 100:
            return f"{number}"


class Config:
    def __init__(self):
        sys.path.append(sys.path[0].replace('/channel', '/config'))
        import appconfig as ac
        self.id = ac.api_id
        self.hash = ac.api_hash
        self.zone = ac.timezone
