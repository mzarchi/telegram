# Telegram Analysis

***Steps:***
1. Go to [Telegram Apps](https://my.telegram.org/auth?to=apps) to get **_api_id_** and **_api_hash_**

2. Install **Telethon** by ```pip install Telethon


3. Use ```git clone https://github.com/mzarchi/telegram.git```

4. Rename ```/config/appconfig_ignore.py``` to ```/config/appconfig.py``` and put your **_api_id_** and **_api_hash_**
    > <sub>At this step, you must have **api_id** and **api_hash**</sub>

5. Login to your **Telegram** account by `` `/login/main.py` ` ` and save your **automatically** your session in ` ``/sessions

6. Open ```/channel/analysis.ipynb``` and run first cell

## Supported params in ```/channel/analysis.ipynb```
The most important cell in this notebook is this:
```
match_case = 6  # Important param
dics = md.get_vfm_data(
    data, match_case,
    min_id=0, max_id=1000,
    min_view=0, max_view=0,
    min_forward=0, max_forward=0,
    min_mention=0, max_mention=0,
    datetime_start=md.ts("2010-01-18 00:00"), datetime_end=md.ts("2010-01-18 00:00"),
)

``` 
According to the following ```match_case```:
```
| 0 : No limit
| 1 : DateTime limit
| 3 : View limit
| 4 : Forward limit
| 5 : Mention limit
| 6 : ID limit
| 13 : DateTime & View limit
| 14 : DateTime & Forward limit
| 15 : DateTime & Mention limit
| 34 : View & Forward limit
| 35 : View & Mention limit
| 45 : Forward & Mention limit
```
You can get the data you want in an edited form!
<p align="center">
<img src="./assets/images/plot-1.jpg" width="500" height="500">
</p>

* [x] Check if data set is exist
    - [x] if exist sort, if not get data
* [x] Get Data
* [x] Save Data
* [x] Draw scatter graph
* [ ] Draw monthly graph
