
from pydoc import describe
import pymysql

schlocationName = input("請輸入縣市地區")

if schlocationName !='':
    db = pymysql.connect(host='127.0.0.1',user='root',password='',db='cwb')
    cursor = db.cursor()
    sql="select * from thirty_six_hour_weather_forecast where locationName  = '%s'"%(schlocationName)
    cursor.execute(sql)
    data0 = cursor.fetchall()
    # print(data0)
    for row in data0:
        print (row[3],row[4],row[5])
        print (row[17],row[18],row[19])
        print (row[42],row[43],row[44])

    db.close()
else:
    print("不可以是空的")
