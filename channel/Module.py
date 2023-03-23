from datetime import datetime
import time
import json
import sys


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
    def convert_timestamp(cls, ts, rs=True):
        # Convert timestamp to datetime
        dt = cls.fromtimestamp(ts)
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

    @classmethod
    def points(cls, timestamp):
        # Convert timestamp to point
        dt = cls.fromtimestamp(timestamp)
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


class File:
    @classmethod
    def write(cls, username, data):
        txt = json.dumps(data)
        f = open(f"ChannelData/{username}.json", "a")
        f.write(txt)
        f.close()

    @classmethod
    def read(cls, username):
        f = open(f"ChannelData/{username}.json", "r")
        return json.loads(f.read())


class Config:
    id = 0
    hash = ''

    def __init__(self):
        sys.path.append(sys.path[0].replace('/channel', '/config'))
        import appconfig as ac
        self.id = ac.api_id
        self.hash = ac.api_hash
