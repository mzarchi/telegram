# Telegram Analysis

***Steps:***
1. Go to [Telegram Apps](https://my.telegram.org/auth?to=apps) to get **_api_id_** and **_api_hash_**

2. Clone repo by ```git clone https://github.com/mzarchi/telegram.git```

3. Install lib by ```pip install -r requirements.txt```

4. Rename ```/config/appconfig_ignore.py``` to ```/config/appconfig.py``` and put your **_api_id_** and **_api_hash_**
    > <sub>At this step, you must have **api_id** and **api_hash**</sub>

5. Login to your **Telegram** account by ```/login/main.py``` and save **automatically** your session in ```/sessions```

6. Open ```/channel/analysis.ipynb``` and run first cell

## Supported params in ```/channel/analysis.ipynb```
The most important cell in this notebook is this:

```
match_case = 0  # Important param
dics = cdata(
    data, match_case,
    min_id=0, max_id=1000,
    min_view=0, max_view=0,
    min_forward=0, max_forward=0,
    min_mention=0, max_mention=0,
    start_time='15:00:00', stop_time='21:00:00',
    start_datetime=tm.timestamp('2010-01-18 00:00', '%Y-%m-%d %H:%M'),
    stop_datetime=tm.timestamp('2010-01-18 00:00', '%Y-%m-%d %H:%M')
)
```

According to the following ```match_case```:
```
0 : No limit *
1 : DateTime limit *
2 : TimeRange limit *
3 : View limit *
4 : Forward limit *
5 : Mention limit *
6 : ID limit *
13 : DateTime & View limit *
14 : DateTime & Forward limit *
15 : DateTime & Mention limit *
16 : DateTime & ID limit *
34 : View & Forward limit *
35 : View & Mention limit *
36 : View & ID limit *
45 : Forward & Mention limit *
46 : Forward & ID limit *
56 : Mention & ID limit *
```
You can get the data you want in an edited form!