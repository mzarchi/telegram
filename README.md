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
- [x] 1 : DateTime limit
- [x] 2 : TimeRange limit
- [x] 3 : View limit
- [x] 4 : Forward limit 
- [x] 5 : Mention limit
- [x] 6 : ID limit
- [x] 7 : Admins
- [ ] 12 : DateTime & TimeRange limit
- [x] 13 : DateTime & View limit
- [x] 14 : DateTime & Forward limit
- [x] 15 : DateTime & Mention limit
- [x] 16 : DateTime & ID limit
- [ ] 17 : DateTime & Admins
- [ ] 23 : TimeRange & View limit
- [ ] 24 : TimeRange & Forward limit
- [ ] 25 : TimeRange & Mention limit
- [ ] 26 : TimeRange & ID limit
- [ ] 27 : TimeRange & Admins limit
- [x] 34 : View & Forward limit
- [x] 35 : View & Mention limit
- [x] 36 : View & ID limit
- [ ] 37 : View & Admins limit
- [x] 45 : Forward & Mention limit
- [x] 46 : Forward & ID limit
- [ ] 47 : Forward & Admins limit
- [x] 56 : Mention & ID limit
- [x] 57 : Mention & Admins limit
- [ ] 67 : ID limit & Admins
- [ ] 123 : DateTime & TimeRange & View limit
- [ ] 124 : DateTime & TimeRange & Forward limit
- [ ] 125 : DateTime & TimeRange & Mention limit
- [ ] 126 : DateTime & TimeRange & ID limit
- [ ] 127 : DateTime & TimeRange & Admins limit
- [ ] 234 : TimeRange & Favorite & Forward limit
- [ ] 235 : TimeRange & Favorite & Mention limit
- [ ] 236 : TimeRange & Favorite & ID limit
- [ ] 237 : TimeRange & Favorite & Admins limit
- [ ] 345 : View & Forward & Mention limit
- [ ] 346 : View & Forward & ID limit
- [ ] 347 : View & Forward & Admins limit
- [ ] 1234 : DateTime & TimeRange & View & Forward limit
- [ ] 1235 : DateTime & TimeRange & View & Mention limit
- [ ] 1236 : DateTime & TimeRange & View & ID limit
- [ ] 1237 : DateTime & TimeRange & View & Admins limit
- [ ] 12345 : DateTime & TimeRange & View & Forward & Mention limit
- [ ] 12346 : DateTime & TimeRange & View & Forward & ID limit
- [ ] 12347 : DateTime & TimeRange & View & Forward & Admins limit
- [ ] 123456 : DateTime & TimeRange & View & Forward & Mention & ID limit
- [ ] 123457 : DateTime & TimeRange & View & Forward & Mention & Admins limit
- [ ] 1234567 : DateTime & TimeRange & View & Forward & Mention & ID & Admins limit


You can get the data you want in an edited form!
