import mysql.connector
from dotenv import *
import os
load_dotenv()



def connect_to_pool():
    cnxpool = mysql.connector.pooling.MySQLConnectionPool(
    user=os.getenv("user"),
    password=os.getenv("password"),
    host=os.getenv("host"),
    database="tiktok",
    pool_name="tikpool",
    pool_size=2,
    )
    return cnxpool