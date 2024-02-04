from flask import *
from time import *
import json
import urllib.request as req
from model.query_make import *

flag = 259200
while flag>0:
    flag-=3600
    time_now = get_time()
    url="https://www.tiktok.com/api/post/item_list/?WebIdLastTime=1706512299&aid=1988&app_language=zh-Hant-TW&app_name=tiktok_web&browser_language=zh-TW&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F120.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&count=35&coverFormat=2&cursor=0&device_id=7329414412724749842&device_platform=web_pc&focus_state=true&from_page=user&history_len=8&is_fullscreen=false&is_page_visible=true&language=zh-Hant-TW&os=windows&priority_region=&referer=https%3A%2F%2Fwww.google.com%2F&region=TW&root_referer=https%3A%2F%2Fwww.google.com%2F&screen_height=1080&screen_width=1920&secUid=MS4wLjABAAAAJIomeXV1JCW4_bS7h6mx4Ftf4pM9eYpW30KW1f3834SvpVXO0vHfuwBUGSWjE0PY&tz_name=Etc%2FGMT-8&verifyFp=verify_lryldi3z_msamPoV7_BQKp_4QpO_8qnj_REgXvrggfLe0&webcast_language=zh-Hant-TW&msToken=ebRGQgvlcrLkN6gbEsv-4k-xKs83InZgA-wzYTAi34CCB5nX1IaUvLwCl2cgjw2S_CPhzG6mfnpwbX_w0YG8A0A08XsS_E_l2QOi2kA68EVvd-bbIEiH2-qG8bKVlcik7e4ZrlwrGCJjrrU=&X-Bogus=DFSzswVOcktANy5ntE/bt09WcBne&_signature=_02B4Z6wo00001r3x8.AAAIDCvfHz8GmpKHK98fdAAMrX86"
    
    request = req.Request(url, headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    result=json.loads(data)

    for i in range(0,len(result["itemList"])):
        if result["itemList"][i]["createTime"] > 1706699830:
            stats = result["itemList"][i]["stats"]
            post_name = result["itemList"][i]["desc"]
            post_id = result["itemList"][i]["id"]
            data = {
                "post_id":post_id,
                "post_name":post_name,
                "likes":stats["diggCount"],
                "comments":stats["commentCount"],
                "favorites":stats["collectCount"],
                "shares":stats["shareCount"],
                "hourly_timestamp":time_now
            }
            res = data_log(data)
            if res:
                print("資料建立成功",time_now)
            else:
                print("意外的錯誤",time_now)
        else:
            break
    sleep(3600)


