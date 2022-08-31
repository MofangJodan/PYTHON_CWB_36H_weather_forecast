
from pydoc import describe
import pymysql
import matplotlib.pyplot as plt

schlocationName = input("請輸入縣市地區")

if schlocationName !='':
    db = pymysql.connect(host='127.0.0.1',user='root',password='',db='cwb')
    cursor = db.cursor()
    sql="select * from thirty_six_hour_weather_forecast where locationName  = '%s'"%(schlocationName)
    cursor.execute(sql)
    data0 = cursor.fetchall()
    # print(data0)
    for row in data0:
        # 溫度變化圖表
        data=[row[6],row[14],row[31],row[35],row[39],row[54],row[58],row[62]]
        plt.xlabel("Day")
        plt.ylabel("Celsius")
        plt.plot(data)
        plt.show()

    db.close()
else:
    print("不可以是空的")
