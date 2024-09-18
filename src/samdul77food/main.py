from typing import Union
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import pytz
from PIL import Image
import uuid
import os

app = FastAPI()

origins = [
    "http://localhost:8899",
    "https://samdul77food.web.app",
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

@app.post("/photo")
async def upload_photo(file: UploadFile):
    UPLOAD_DIR = "./photo"  # 이미지를 저장할 서버 경로
    
    content = await file.read()
    filename = f"{str(uuid.uuid4())}.jpg"  # uuid로 유니크한 파일명으로 변경
    with open(os.path.join(UPLOAD_DIR, filename), "wb") as fp:
        fp.write(content)  # 서버 로컬 스토리지에 이미지 저장 (쓰기)

    return {"filename": filename}