from model.rds_pool import *
from datetime import datetime

cnxpool = connect_to_pool()

def data_log(data):
    con = cnxpool.get_connection()
    cursor = con.cursor(dictionary=True)
    try:
        cursor.execute(
            "INSERT INTO follow(post_id, post_name, likes, comments, favorites, shares, hourly_timestamp) VALUES(%s, %s, %s, %s, %s, %s, %s)",
            (data["post_id"], data["post_name"], data["likes"], data["comments"], data["favorites"], data["shares"], data["hourly_timestamp"]),
        )
        con.commit()
        return True
    except Exception as err:
        print("data_log: ",err)
        return False
    finally:
        cursor.close()
        con.close()

from datetime import datetime
import pytz

def get_time():
    # 取得當前時間
    current_time_utc = datetime.utcnow()
    taipei_timezone = pytz.timezone('Asia/Taipei')
    
    # 將 UTC 時間轉換為台北時區
    current_time_taipei = current_time_utc.replace(tzinfo=pytz.utc).astimezone(taipei_timezone)
    
    # 格式化為指定的字符串
    formatted_time = current_time_taipei.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_time