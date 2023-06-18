from telethon.sync import TelegramClient
from Module import Time, File, Config
from pytz import timezone


async def get(username, count):
    data = []
    cf = Config()
    async with TelegramClient('../sessions/test', cf.id, cf.hash) as client:
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

                    post_author = "NoAuthor"
                    if hasattr(item, "post_author"):
                        post_author = item.post_author

                    td = item.date.astimezone(timezone(cf.zone))
                    datetime_list = Time.dtlist(td)
                    post_detais = {
                        'id': item.id,
                        'is_forward': frw,
                        'view': item.views,
                        'mention': replies,
                        'author': post_author,
                        'forward': item.forwards,
                        'date': datetime_list[0],
                        'time': datetime_list[1],
                        'unixtime': int(item.date.timestamp()),
                    }

                    data.append(post_detais)
                except:
                    print("Error")
                    pass

    data.reverse()
    print(f"\nData size: {len(data)}")
    field_name = [
        'date',
        'time',
        'unixtime',
        'id',
        'is_forward',
        'mention',
        'view',
        'forward',
        'author',
    ]
    File.write(username, field_name, data)
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
    xp = {'g1': [], 'g2': [], 'g3': [], 'g4': []}
    yp = {'g1': [], 'g2': [], 'g3': [], 'g4': []}

    for p in data:
        dname = p['date'].replace("-", ".")
        if dname in sd:
            sd[dname] += 1
        else:
            sd[dname] = 1
    dt = Time.dtlist(Time.dtnow())
    today = Time.points(dt[0].split("-"))
    unit_value = max(sd.values()) / 3
    uv2 = unit_value * 2
    uv3 = unit_value * 3

    try:
        for p in data:
            xy, ym = Time.points(p['date'].split("-"))
            dname = p['date'].replace("-", ".")
            dsv = p['date'].replace("-", "")
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

    return xp, yp, today


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
    7 : Admins *
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
    67 : ID limit & Admins *
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

    for post in data.iterrows():
        pid = post[1]['id']
        pview = post[1]['view']
        ptime = post[1]['time']
        pdate = post[1]['date']
        author = post[1]['author']
        pmention = post[1]['mention']
        pforward = post[1]['forward']
        punixtime = post[1]['unixtime']
        pis_forward = post[1]['is_forward']
        append_gate = False

        match match_code:
            case 0:  # No limit
                append_gate = True

            case 1:  # DateTime limit
                if (pis_forward == 0):
                    if (punixtime <= p['stop_datetime'] and punixtime > p['start_datetime']):
                        append_gate = True

            case 2:  # TimeRange limit
                if (pis_forward == 0):
                    start_time, stop_time = Time.reformat_time(
                        p['start_time'], p['stop_time'])
                    post_time = int(ptime.replace(":", ""))
                    if (post_time >= start_time and post_time <= stop_time):
                        append_gate = True

            case 3:  # View limit
                if (pis_forward == 0):
                    if (pview <= p['max_view'] and pview > p['min_view']):
                        append_gate = True

            case 4:  # Forward limit
                if (pis_forward == 0):
                    if (pforward <= p['max_forward'] and pforward > p['min_forward']):
                        append_gate = True

            case 5:  # Mention limit
                if (pis_forward == 0):
                    if (pmention <= p['max_mention'] and pmention > p['min_mention']):
                        append_gate = True

            case 6:  # ID limit
                if (pis_forward == 0):
                    if (pid <= p['max_id'] and pid > p['min_id']):
                        append_gate = True

            case 7:  # Admins
                if (pis_forward == 0):
                    if author in p['admins']:
                        append_gate = True

            case 13:  # DateTime and View limit
                if (pis_forward == 0):
                    if (punixtime <= p['stop_datetime'] and punixtime > p['start_datetime'] and
                            pview <= p['max_view'] and pview > p['min_view']):
                        append_gate = True

            case 14:  # DateTime and Forward limit
                if (pis_forward == 0):
                    if (punixtime <= p['stop_datetime'] and punixtime > p['start_datetime'] and
                            pforward <= p['max_forward'] and pforward > p['min_forward']):
                        append_gate = True

            case 15:  # DateTime and Mention limit
                if (pis_forward == 0):
                    if (punixtime <= p['stop_datetime'] and punixtime > p['start_datetime'] and
                            pmention <= p['max_mention'] and pmention > p['min_mention']):
                        append_gate = True

            case 16:  # DateTime and ID limit
                if (pis_forward == 0):
                    if (punixtime <= p['stop_datetime'] and punixtime > p['start_datetime'] and
                            pid <= p['max_id'] and pid > p['min_id']):
                        append_gate = True

            case 34:  # View and Forward limit
                if (pis_forward == 0):
                    if (pview <= p['max_view'] and pview > p['min_view'] and
                            pforward <= p['max_forward'] and pforward > p['min_forward']):
                        append_gate = True

            case 35:  # View and Mention limit
                if (pis_forward == 0):
                    if (pview <= p['max_view'] and pview > p['min_view'] and
                            pmention <= p['max_mention'] and pmention > p['min_mention']):
                        append_gate = True

            case 36:  # View and ID limit
                if (pis_forward == 0):
                    if (pview <= p['max_view'] and pview > p['min_view'] and
                            pid <= p['max_id'] and pid > p['min_id']):
                        append_gate = True

            case 45:  # Forward and Mention limit
                if (pis_forward == 0):
                    if (pforward <= p['max_forward'] and pforward > p['min_forward'] and
                            pmention <= p['max_mention'] and pmention > p['min_mention']):
                        append_gate = True

            case 46:  # Forward and ID limit
                if (pis_forward == 0):
                    if (pforward <= p['max_forward'] and pforward > p['min_forward'] and
                            pid <= p['max_id'] and pid > p['min_id']):
                        append_gate = True

            case 56:  # Mention and ID limit
                if (pis_forward == 0):
                    if (pmention <= p['max_mention'] and pmention > p['min_mention'] and
                            pid <= p['max_id'] and pid > p['min_id']):
                        append_gate = True

            case 67:  # ID limit & Admins
                if (pid <= p['max_id'] and pid > p['min_id'] and author in p['admins']):
                    append_gate = True

        if append_gate:
            newdata.append(post[1])
            result_dict['cont'].append(counter)
            result_dict['view'].append(pview)
            result_dict['forw'].append(pforward)
            result_dict['repl'].append(pmention)
            result_dict['view_dict'].update({pid: pview})
            result_dict['forw_dict'].update({pid: pforward})
            result_dict['repl_dict'].update({pid: pmention})

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
