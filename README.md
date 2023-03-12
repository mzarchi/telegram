# Telegram Analysis

***Steps:***
1. Go to [Telegram Apps](https://my.telegram.org/auth?to=apps) to get **_api_id_** and **_api_hash_**

2. Install **Telethon** by ```pip install Telethon

```

3. Use ```git clone https://github.com/mzarchi/telegram.git```

4. Rename ```/config/appconfig_ignore.py``` to ```/config/appconfig.py``` and put your **_api_id_** and **_api_hash_**
    > <sub>At this step, you must have **api_id** and **api_hash**</sub>

5. Login to your **Telegram** account by `` `/login/main.py` ` ` and save your **automatically** your session in ` ``/sessions

```

6. Open ```/channel/analysis.ipynb``` and run first cell

## Supported params in ```/channel/analysis.ipynb```

| 0 : No limit<br>
| 1 : DateTime limit<br>
| 3 : View limit<br>
| 4 : Forward limit<br>
| 5 : Mention limit<br>
| 6 : ID limit<br>
| 13 : DateTime & View limit<br>
| 14 : DateTime & Forward limit<br>
| 15 : DateTime & Mention limit<br>
| 34 : View & Forward limit<br>
| 35 : View & Mention limit<br>
| 45 : Forward & Mention limit<br>

<p align="center">
<img src="./assets/images/plot-1.jpg" width="500" height="500">
</p>

* [x] Check if data set is exist
    - [x] if exist sort, if not get data
* [x] Get Data
* [x] Save Data
* [x] Draw scatter graph
* [ ] Draw monthly graph
