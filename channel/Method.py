from telethon.sync import TelegramClient
from Module import Time, File, Config
from pytz import timezone


async def get(username, count):
    data = []
    cf = Config()
    async with TelegramClient('../sessions/my', cf.id, cf.hash) as client:
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

                    td = item.date.astimezone(timezone(cf.zone))
                    post_detais = {
                        'id': item.id,
                        'view': item.views,
                        'forward': item.forwards,
                        'mention': replies,
                        'datetime': Time.dtlist(td),
                        'unixtime': int(item.date.timestamp()),
                        'is_forward': frw
                    }

                    data.append(post_detais)
                except:
                    print("Error")
                    pass

    data.reverse()
    print(f"\nData size: {len(data)}")
    Time.sleep(1)
    File.write(username, data)
    return data


async def get_src(username, count):
    data = []
    cf = Config()
    async with TelegramClient('../sessions/my', cf.id, cf.hash) as client:
        print("Start streaming ...")
        for item in await client.get_messages(username, limit=count):
            data.append(item)

    return data


def scatter_handel(data):
    sd = {}
    ds = []
    distance_ts = []
    xp = {'g1': [], 'g2': [], 'g3': [], 'g4': []}
    yp = {'g1': [], 'g2': [], 'g3': [], 'g4': []}

    for p in data:
        dname = f"{p['datetime'][0]}.{p['datetime'][1]}.{p['datetime'][2]}"
        if dname in sd:
            sd[dname] += 1
        else:
            sd[dname] = 1

    today = Time.points(Time.dtlist(Time.dtnow()))
    unit_value = max(sd.values()) / 3
    uv2 = unit_value * 2
    uv3 = unit_value * 3

    try:
        for i, p in enumerate(data):
            distance_ts.append(data[i+1]['unixtime'] - data[i]['unixtime'])
            xy, ym = Time.points(p['datetime'])
            dname = f"{p['datetime'][0]}.{p['datetime'][1]}.{p['datetime'][2]}"
            dsv = f"{p['datetime'][0]}{p['datetime'][1]}{p['datetime'][2]}"
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


def pdistance(distance, day_count):
    # Show post time distanced from before post
    distance.sort(reverse=True)
    print("Big distance from two post (day):")
    for i, d in enumerate(distance):
        if (i + 1) > day_count:
            break
        print("{} days".format(int(d / 86400)))


def cdata(data, match_code, **p):
    """
    0 : No limit *
    1 : DateTime limit *
    2 : TimeRange limit *
    3 : View limit *
    4 : Forward limit *
    5 : Mention limit *
    6 : ID limit *
    12 : DateTime & TimeRange limit
    13 : DateTime & View limit *
    14 : DateTime & Forward limit *
    15 : DateTime & Mention limit *
    16 : DateTime & ID limit *
    23 : TimeRange & View limit
    24 : TimeRange & Forward limit
    25 : TimeRange & Mention limit
    34 : View & Forward limit *
    35 : View & Mention limit *
    36 : View & ID limit *
    45 : Forward & Mention limit *
    46 : Forward & ID limit *
    56 : Mention & ID limit *
    123 : DateTime & TimeRange & View limit
    124 : DateTime & TimeRange & Forward limit
    125 : DateTime & TimeRange & Mention limit
    234 : TimeRange & Favorite & Forward limit
    235 : TimeRange & Favorite & Mention limit
    345 : View & Forward & Mention limit
    1234 : DateTime & TimeRange & View & Forward limit
    1235 : DateTime & TimeRange & View & Mention limit
    12345 : DateTime & TimeRange & View & Forward & Mention limit
    """

    counter = 1
    newdata = []
    result_dict = {
        'cont': [], 'view': [], 'forw': [], 'repl': [],
        'view_dict': {}, 'forw_dict': {}, 'repl_dict': {}
    }

    for post in data:
        append_gate = False
        match match_code:
            case 0:  # No limit
                if (post['is_forward'] == 0):
                    append_gate = True

            case 1:  # DateTime limit
                if (post['is_forward'] == 0):
                    if (post['unixtime'] <= p['stop_datetime'] and post['unixtime'] > p['start_datetime']):
                        append_gate = True

            case 2:  # TimeRange limit
                if (post['is_forward'] == 0):
                    start_time, stop_time = Time.reformat_time(
                        p['start_time'], p['stop_time'])
                    pt = post['datetime']
                    post_time = int(f"{pt[3]}{pt[4]}{pt[5]}")
                    if (post_time >= start_time and post_time <= stop_time):
                        append_gate = True

            case 3:  # View limit
                if (post['is_forward'] == 0):
                    if (post['view'] <= p['max_view'] and post['view'] > p['min_view']):
                        append_gate = True

            case 4:  # Forward limit
                if (post['is_forward'] == 0):
                    if (post['forward'] <= p['max_forward'] and post['forward'] > p['min_forward']):
                        append_gate = True

            case 5:  # Mention limit
                if (post['is_forward'] == 0):
                    if (post['mention'] <= p['max_mention'] and post['mention'] > p['min_mention']):
                        append_gate = True

            case 6:  # ID limit
                if (post['is_forward'] == 0):
                    if (post['id'] <= p['max_id'] and post['id'] > p['min_id']):
                        append_gate = True

            case 13:  # DateTime and View limit
                if (post['is_forward'] == 0):
                    if (post['unixtime'] <= p['stop_datetime'] and post['unixtime'] > p['start_datetime'] and
                            post['view'] <= p['max_view'] and post['view'] > p['min_view']):
                        append_gate = True

            case 14:  # DateTime and Forward limit
                if (post['is_forward'] == 0):
                    if (post['unixtime'] <= p['stop_datetime'] and post['unixtime'] > p['start_datetime'] and
                            post['forward'] <= p['max_forward'] and post['forward'] > p['min_forward']):
                        append_gate = True

            case 15:  # DateTime and Mention limit
                if (post['is_forward'] == 0):
                    if (post['unixtime'] <= p['stop_datetime'] and post['unixtime'] > p['start_datetime'] and
                            post['mention'] <= p['max_mention'] and post['mention'] > p['min_mention']):
                        append_gate = True

            case 16:  # DateTime and ID limit
                if (post['is_forward'] == 0):
                    if (post['unixtime'] <= p['stop_datetime'] and post['unixtime'] > p['start_datetime'] and
                            post['id'] <= p['max_id'] and post['id'] > p['min_id']):
                        append_gate = True

            case 34:  # View and Forward limit
                if (post['is_forward'] == 0):
                    if (post['view'] <= p['max_view'] and post['view'] > p['min_view'] and
                            post['forward'] <= p['max_forward'] and post['forward'] > p['min_forward']):
                        append_gate = True

            case 35:  # View and Mention limit
                if (post['is_forward'] == 0):
                    if (post['view'] <= p['max_view'] and post['view'] > p['min_view'] and
                            post['mention'] <= p['max_mention'] and post['mention'] > p['min_mention']):
                        append_gate = True

            case 36:  # View and ID limit
                if (post['is_forward'] == 0):
                    if (post['view'] <= p['max_view'] and post['view'] > p['min_view'] and
                            post['id'] <= p['max_id'] and post['id'] > p['min_id']):
                        append_gate = True

            case 45:  # Forward and Mention limit
                if (post['is_forward'] == 0):
                    if (post['forward'] <= p['max_forward'] and post['forward'] > p['min_forward'] and
                            post['mention'] <= p['max_mention'] and post['mention'] > p['min_mention']):
                        append_gate = True

            case 46:  # Forward and ID limit
                if (post['is_forward'] == 0):
                    if (post['forward'] <= p['max_forward'] and post['forward'] > p['min_forward'] and
                            post['id'] <= p['max_id'] and post['id'] > p['min_id']):
                        append_gate = True

            case 56:  # Mention and ID limit
                if (post['is_forward'] == 0):
                    if (post['mention'] <= p['max_mention'] and post['mention'] > p['min_mention'] and
                            post['id'] <= p['max_id'] and post['id'] > p['min_id']):
                        append_gate = True

        if append_gate:
            newdata.append(post)
            result_dict['cont'].append(counter)
            result_dict['view'].append(post['view'])
            result_dict['forw'].append(post['forward'])
            result_dict['repl'].append(post['mention'])
            result_dict['view_dict'].update({post['id']: post['view']})
            result_dict['forw_dict'].update({post['id']: post['forward']})
            result_dict['repl_dict'].update({post['id']: post['mention']})

        counter += 1
    return newdata, result_dict


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
        day_position = p['unixtime'] % 86400
        day_andis = 0
        if day_position % 900 == 0:
            day_andis = day_position // 900
        else:
            day_andis = (day_position // 900) + 1

        if day_andis == 96:
            day_andis = 0

        day_dict[day_andis] += 1
        rte_dict[day_andis] += ((p['view'] * view_rate) +
                                (p['forward'] * forw_rate) + (p['mention'] * ment_rate)) / 1000
        viw_dict[day_andis].append(p['view'])

    return day_dict, rte_dict, viw_dict
