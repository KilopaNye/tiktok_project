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


#-----pyplot block-----
def get_log(set_limit, post_id=False):
    con = cnxpool.get_connection()
    cursor = con.cursor(dictionary=True)
    try:
        if post_id:
            cursor.execute(
                "SELECT * FROM follow WHERE post_id=%s limit 20 OFFSET %s",(post_id, set_limit,)
            )
        else:
            cursor.execute(
                "SELECT * FROM follow"
            )
        source = cursor.fetchall()
        if source:
            return source
        else:
            return False

    except Exception as err:
        print("get_log: ",err)
        return False
    finally:
        cursor.close()
        con.close()


def get_total_log(set_limit):
    con = cnxpool.get_connection()
    cursor = con.cursor(dictionary=True)
    try:
        cursor.execute(
            "SELECT SUM(likes) AS likes, SUM(comments) AS comments, SUM(favorites) AS favorites, SUM(shares) AS shares, hourly_timestamp, COUNT(*) AS post_count FROM follow WHERE post_id != '7330219946762439941' AND hourly_timestamp < '2024-02-04 21:00:00' GROUP BY hourly_timestamp limit 25 OFFSET %s",(set_limit,)
        )
        source = cursor.fetchall()
        if source:
            return source
        else:
            return False

    except Exception as err:
        print("get_total_log: ",err)
        return False
    finally:
        cursor.close()
        con.close()

def get_all_log():
    con = cnxpool.get_connection()
    cursor = con.cursor(dictionary=True)
    try:
        cursor.execute(
            "SELECT SUM(likes) AS likes, SUM(comments) AS comments, SUM(favorites) AS favorites, SUM(shares) AS shares, hourly_timestamp, COUNT(*) AS post_count FROM follow WHERE post_id != '7330219946762439941' AND hourly_timestamp < '2024-02-04 21:00:00' GROUP BY hourly_timestamp"
        )
        source = cursor.fetchall()
        if source:
            return source
        else:
            return False

    except Exception as err:
        print("get_all_log: ",err)
        return False
    finally:
        cursor.close()
        con.close()

def get_post_count():
    con = cnxpool.get_connection()
    cursor = con.cursor(dictionary=True)
    try:
        cursor.execute(
            "SELECT COUNT(*) AS post_count, hourly_timestamp FROM follow WHERE hourly_timestamp < '2024-02-04 21:00:00' AND post_id != '7330219946762439941' GROUP BY hourly_timestamp"
        )
        source = cursor.fetchall()
        if source:
            return source
        else:
            return False

    except Exception as err:
        print("get_post_count: ",err)
        return False
    finally:
        cursor.close()
        con.close()