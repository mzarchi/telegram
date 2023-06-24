<p>
<img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/mzarchi/telegram">
<img alt="GitHub contributors" src="https://img.shields.io/github/contributors/mzarchi/telegram">
</p>

## Telegram content analysis

**_Steps:_**

1. Go to [Telegram Apps](https://my.telegram.org/auth?to=apps) to get **_api_id_** and **_api_hash_**

2. Clone repo by `git clone https://github.com/mzarchi/telegram.git`

3. Install lib by `pip install -r requirements.txt`

4. Copy `.env.example` to `.env` and put your **_api_id_** and **_api_hash_** with `cp .env.example .env`

   > <sub>At this step, you must have **api_id** and **api_hash**</sub>

5. Login to your **Telegram** account by `/login/main.py` and save **automatically** your session in `/sessions`

6. Open `/channel/analysis.ipynb` and run first cell

## Supported params in `/channel/analysis.ipynb`

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

According to the following `match_case` :


- [x] 0 : No limit<br>
- [x] 1 : <b>DateTime</b> limit
- [x] 2 : <b>TimeRange</b> limit
- [x] 3 : <b>View</b> limit
- [x] 4 : <b>Forward</b> limit 
- [x] 5 : <b>Mention</b> limit
- [x] 6 : <b>ID</b> limit
- [x] 7 : <b>Admins</b>
- [ ] 12 : <b>DateTime</b> & <b>TimeRange</b> limit
- [x] 13 : <b>DateTime</b> & <b>View</b> limit
- [x] 14 : <b>DateTime</b> & <b>Forward</b> limit
- [x] 15 : <b>DateTime</b> & <b>Mention</b> limit
- [x] 16 : <b>DateTime</b> & <b>ID</b> limit
- [ ] 17 : <b>DateTime</b> & <b>Admins</b>
- [ ] 23 : <b>TimeRange</b> & <b>View</b> limit
- [ ] 24 : <b>TimeRange</b> & <b>Forward</b> limit
- [ ] 25 : <b>TimeRange</b> & <b>Mention</b> limit
- [ ] 26 : <b>TimeRange</b> & <b>ID</b> limit
- [ ] 27 : <b>TimeRange</b> & <b>Admins</b> limit
- [x] 34 : <b>View</b> & <b>Forward</b> limit
- [x] 35 : <b>View</b> & <b>Mention</b> limit
- [x] 36 : <b>View</b> & <b>ID</b> limit
- [ ] 37 : <b>View</b> & <b>Admins</b> limit
- [x] 45 : <b>Forward</b> & <b>Mention</b> limit
- [x] 46 : <b>Forward</b> & <b>ID</b> limit
- [ ] 47 : <b>Forward</b> & <b>Admins</b> limit
- [x] 56 : <b>Mention</b> & <b>ID</b> limit
- [x] 57 : <b>Mention</b> & <b>Admins</b> limit
- [ ] 67 : <b>ID</b> limit & <b>Admins</b>
- [ ] 123 : <b>DateTime</b> & <b>TimeRange</b> & <b>View</b> limit
- [ ] 124 : <b>DateTime</b> & <b>TimeRange</b> & <b>Forward</b> limit
- [ ] 125 : <b>DateTime</b> & <b>TimeRange</b> & <b>Mention</b> limit
- [ ] 126 : <b>DateTime</b> & <b>TimeRange</b> & <b>ID</b> limit
- [ ] 127 : <b>DateTime</b> & <b>TimeRange</b> & <b>Admins</b> limit
- [ ] 234 : <b>TimeRange</b> & Favorite & <b>Forward</b> limit
- [ ] 235 : <b>TimeRange</b> & Favorite & <b>Mention</b> limit
- [ ] 236 : <b>TimeRange</b> & Favorite & <b>ID</b> limit
- [ ] 237 : <b>TimeRange</b> & Favorite & <b>Admins</b> limit
- [ ] 345 : <b>View</b> & <b>Forward</b> & <b>Mention</b> limit
- [ ] 346 : <b>View</b> & <b>Forward</b> & <b>ID</b> limit
- [ ] 347 : <b>View</b> & <b>Forward</b> & <b>Admins</b> limit
- [ ] 1234 : <b>DateTime</b> & <b>TimeRange</b> & <b>View</b> & <b>Forward</b> limit
- [ ] 1235 : <b>DateTime</b> & <b>TimeRange</b> & <b>View</b> & <b>Mention</b> limit
- [ ] 1236 : <b>DateTime</b> & <b>TimeRange</b> & <b>View</b> & <b>ID</b> limit
- [ ] 1237 : <b>DateTime</b> & <b>TimeRange</b> & <b>View</b> & <b>Admins</b> limit
- [ ] 12345 : <b>DateTime</b> & <b>TimeRange</b> & <b>View</b> & <b>Forward</b> & <b>Mention</b> limit
- [ ] 12346 : <b>DateTime</b> & <b>TimeRange</b> & <b>View</b> & <b>Forward</b> & <b>ID</b> limit
- [ ] 12347 : <b>DateTime</b> & <b>TimeRange</b> & <b>View</b> & <b>Forward</b> & <b>Admins</b> limit
- [ ] 123456 : <b>DateTime</b> & <b>TimeRange</b> & <b>View</b> & <b>Forward</b> & <b>Mention</b> & <b>ID</b> limit
- [ ] 123457 : <b>DateTime</b> & <b>TimeRange</b> & <b>View</b> & <b>Forward</b> & <b>Mention</b> & <b>Admins</b> limit
- [ ] 1234567 : <b>DateTime</b> & <b>TimeRange</b> & <b>View</b> & <b>Forward</b> & <b>Mention</b> & <b>ID</b> & <b>Admins</b> limit


You can get the data you want in an edited form!
