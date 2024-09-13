from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pytz

app = FastAPI()

origins = [
    "http://localhost:8899",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "n77"}

@app.get("/food")
def food(name: str):
    # 시간을 구함
    # 음식 이름과 시간을 csv 로 저장 -> /code/data/food.csv
    # DB 저장
    print("==============" + name )

    from datetime import datetime
    import pytz
    timezone = pytz.timezone('Asia/Seoul')
    korea_time = datetime.now(timezone)
    formatted_time = korea_time.strftime('%Y-%m-%d %H:%M:%S')

    import pymysql
    db = pymysql.connect(host = '172.18.0.1',
                     port = 13306,
                     user = 'food',
                     passwd = '1234',
                     db = 'fooddb',
                     charset = 'utf8')
    cursor = db.cursor(pymysql.cursors.DictCursor)

    sql = "INSERT INTO foodhistory(username, foodname, dt) VALUES(%s,%s,%s)"
    cursor.execute(sql, ('n77', name, formatted_time))
    db.commit()

    return {"food": name, "time": formatted_time}
