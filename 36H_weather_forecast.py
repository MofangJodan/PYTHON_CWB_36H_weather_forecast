# ※ URL：https://opendata.cwb.gov.tw/api/v1/rest/datastore/{dataid}?Authorization={apikey}&format={format}                
# {dataid} 為資料編號 (參照：資料清單)  ex.F-C0032-001                
# {apikey} 為會員帳號對應之授權碼  ex.CWB-1234ABCD-78EF-GH90-12XY-IJKL12345678
# {format} 為回傳資料格式  ex.XML、JSON(預設)                
# ※ 範例：https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-1234ABCD-78EF-GH90-12XY-IJKL12345678&format=JSON
# 三十六小時天氣預報

import json, requests 
import pymysql

source_url = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=" # 政府資料開放平臺
source_url1="CWB-1234ABCD-78EF-GH90-12XY-IJKL12345678" # 氣象局

source_url0 = "&format=JSON" # 氣象局 JSON
SS1 = source_url+source_url1
SS2 = SS1+source_url0

url = requests.get(SS2)
text = url.json()

for AA  in range(0,22):
    locationName = (text["records"]["location"][AA]["locationName"])
    hwf01 = (text["records"]["location"][AA]["weatherElement"][0]["elementName"])    
    hwf02 = (text["records"]["location"][AA]["weatherElement"][0]["time"][0]["startTime"])
    hwf03 = (text["records"]["location"][AA]["weatherElement"][0]["time"][0]["endTime"])
    hwf04 = (text["records"]["location"][AA]["weatherElement"][0]["time"][0]["parameter"]["parameterName"])
    hwf05 = (text["records"]["location"][AA]["weatherElement"][0]["time"][0]["parameter"]["parameterValue"])
    hwf06 = (text["records"]["location"][AA]["weatherElement"][0]["time"][1]["startTime"])
    hwf07 = (text["records"]["location"][AA]["weatherElement"][0]["time"][1]["endTime"])
    hwf08 = (text["records"]["location"][AA]["weatherElement"][0]["time"][1]["parameter"]["parameterName"])
    hwf09 = (text["records"]["location"][AA]["weatherElement"][0]["time"][1]["parameter"]["parameterValue"])
    hwf10 = (text["records"]["location"][AA]["weatherElement"][0]["time"][2]["startTime"])
    hwf11 = (text["records"]["location"][AA]["weatherElement"][0]["time"][2]["endTime"])
    hwf12 = (text["records"]["location"][AA]["weatherElement"][0]["time"][2]["parameter"]["parameterName"])
    hwf13 = (text["records"]["location"][AA]["weatherElement"][0]["time"][2]["parameter"]["parameterValue"])
    hwf14 = (text["records"]["location"][AA]["weatherElement"][1]["elementName"])    
    hwf15 = (text["records"]["location"][AA]["weatherElement"][1]["time"][0]["startTime"])
    hwf16 = (text["records"]["location"][AA]["weatherElement"][1]["time"][0]["endTime"])
    hwf17 = (text["records"]["location"][AA]["weatherElement"][1]["time"][0]["parameter"]["parameterName"])
    hwf18 = (text["records"]["location"][AA]["weatherElement"][1]["time"][0]["parameter"]["parameterUnit"])        
    hwf19 = (text["records"]["location"][AA]["weatherElement"][1]["time"][1]["startTime"])
    hwf20 = (text["records"]["location"][AA]["weatherElement"][1]["time"][1]["endTime"])
    hwf21 = (text["records"]["location"][AA]["weatherElement"][1]["time"][1]["parameter"]["parameterName"])
    hwf22 = (text["records"]["location"][AA]["weatherElement"][1]["time"][1]["parameter"]["parameterUnit"])
    hwf23 = (text["records"]["location"][AA]["weatherElement"][1]["time"][2]["startTime"])
    hwf24 = (text["records"]["location"][AA]["weatherElement"][1]["time"][2]["endTime"])
    hwf25 = (text["records"]["location"][AA]["weatherElement"][1]["time"][2]["parameter"]["parameterName"])
    hwf26 = (text["records"]["location"][AA]["weatherElement"][1]["time"][2]["parameter"]["parameterUnit"])
    hwf27 = (text["records"]["location"][AA]["weatherElement"][2]["elementName"])
    hwf28 = (text["records"]["location"][AA]["weatherElement"][2]["time"][0]["startTime"])
    hwf29 = (text["records"]["location"][AA]["weatherElement"][2]["time"][0]["endTime"])
    hwf30 = (text["records"]["location"][AA]["weatherElement"][2]["time"][0]["parameter"]["parameterName"])
    hwf31 = (text["records"]["location"][AA]["weatherElement"][2]["time"][0]["parameter"]["parameterUnit"])
    hwf32 = (text["records"]["location"][AA]["weatherElement"][2]["time"][1]["startTime"])
    hwf33 = (text["records"]["location"][AA]["weatherElement"][2]["time"][1]["endTime"])
    hwf34 = (text["records"]["location"][AA]["weatherElement"][2]["time"][1]["parameter"]["parameterName"])
    hwf35 = (text["records"]["location"][AA]["weatherElement"][2]["time"][1]["parameter"]["parameterUnit"])
    hwf36 = (text["records"]["location"][AA]["weatherElement"][2]["time"][2]["startTime"])
    hwf37 = (text["records"]["location"][AA]["weatherElement"][2]["time"][2]["endTime"])
    hwf38 = (text["records"]["location"][AA]["weatherElement"][2]["time"][2]["parameter"]["parameterName"])
    hwf39 = (text["records"]["location"][AA]["weatherElement"][2]["time"][2]["parameter"]["parameterUnit"])
    hwf40 = (text["records"]["location"][AA]["weatherElement"][3]["elementName"])
    hwf41 = (text["records"]["location"][AA]["weatherElement"][3]["time"][0]["startTime"])
    hwf42 = (text["records"]["location"][AA]["weatherElement"][3]["time"][0]["endTime"])
    hwf43 = (text["records"]["location"][AA]["weatherElement"][3]["time"][0]["parameter"]["parameterName"])
    hwf44 = (text["records"]["location"][AA]["weatherElement"][3]["time"][1]["startTime"])
    hwf45 = (text["records"]["location"][AA]["weatherElement"][3]["time"][1]["endTime"])
    hwf46 = (text["records"]["location"][AA]["weatherElement"][3]["time"][1]["parameter"]["parameterName"])
    hwf47 = (text["records"]["location"][AA]["weatherElement"][3]["time"][2]["startTime"])
    hwf48 = (text["records"]["location"][AA]["weatherElement"][3]["time"][2]["endTime"])
    hwf49 = (text["records"]["location"][AA]["weatherElement"][3]["time"][2]["parameter"]["parameterName"])
    hwf50 = (text["records"]["location"][AA]["weatherElement"][4]["elementName"])
    hwf51 = (text["records"]["location"][AA]["weatherElement"][4]["time"][0]["startTime"])
    hwf52 = (text["records"]["location"][AA]["weatherElement"][4]["time"][0]["endTime"])
    hwf53 = (text["records"]["location"][AA]["weatherElement"][4]["time"][0]["parameter"]["parameterName"])
    hwf54 = (text["records"]["location"][AA]["weatherElement"][4]["time"][0]["parameter"]["parameterUnit"])
    hwf55 = (text["records"]["location"][AA]["weatherElement"][4]["time"][1]["startTime"])
    hwf56 = (text["records"]["location"][AA]["weatherElement"][4]["time"][1]["endTime"])
    hwf57 = (text["records"]["location"][AA]["weatherElement"][4]["time"][1]["parameter"]["parameterName"])
    hwf58 = (text["records"]["location"][AA]["weatherElement"][4]["time"][1]["parameter"]["parameterUnit"])    
    hwf59 = (text["records"]["location"][AA]["weatherElement"][4]["time"][2]["startTime"])
    hwf60 = (text["records"]["location"][AA]["weatherElement"][4]["time"][2]["endTime"])
    hwf61 = (text["records"]["location"][AA]["weatherElement"][4]["time"][2]["parameter"]["parameterName"])
    hwf62 = (text["records"]["location"][AA]["weatherElement"][4]["time"][2]["parameter"]["parameterUnit"])

    data={
    "locationName":locationName,
    "36hwf01":hwf01,
    "36hwf02":hwf02,
    "36hwf03":hwf03,
    "36hwf04":hwf04,
    "36hwf05":hwf05,
    "36hwf06":hwf06,
    "36hwf07":hwf07,
    "36hwf08":hwf08,
    "36hwf09":hwf09,
    "36hwf10":hwf10,
    "36hwf11":hwf11,
    "36hwf12":hwf12,
    "36hwf13":hwf13,
    "36hwf14":hwf14,
    "36hwf15":hwf15,
    "36hwf16":hwf16,
    "36hwf17":hwf17,
    "36hwf18":hwf18,
    "36hwf19":hwf19,
    "36hwf20":hwf20,
    "36hwf21":hwf21,
    "36hwf22":hwf22,
    "36hwf23":hwf23,
    "36hwf24":hwf24,
    "36hwf25":hwf25,
    "36hwf26":hwf26,
    "36hwf27":hwf27,
    "36hwf28":hwf28,
    "36hwf29":hwf29,
    "36hwf30":hwf30,
    "36hwf31":hwf31,
    "36hwf32":hwf32,
    "36hwf33":hwf33,
    "36hwf34":hwf34,
    "36hwf35":hwf35,
    "36hwf36":hwf36,
    "36hwf37":hwf37,
    "36hwf38":hwf38,
    "36hwf39":hwf39,
    "36hwf40":hwf40,
    "36hwf41":hwf41,
    "36hwf42":hwf42,
    "36hwf43":hwf43,
    "36hwf44":hwf44,
    "36hwf45":hwf45,
    "36hwf46":hwf46,
    "36hwf47":hwf47,
    "36hwf48":hwf48,
    "36hwf49":hwf49,
    "36hwf50":hwf50,
    "36hwf51":hwf51,
    "36hwf52":hwf52,
    "36hwf53":hwf53,
    "36hwf54":hwf54,
    "36hwf55":hwf55,
    "36hwf56":hwf56,
    "36hwf57":hwf57,
    "36hwf58":hwf58,
    "36hwf59":hwf59,
    "36hwf60":hwf60,
    "36hwf61":hwf61,
    "36hwf62":hwf62,
    }
    db = pymysql.connect(host='127.0.0.1',user='root',password='',db='cwb')
    cursor = db.cursor()
    sql = "INSERT INTO thirty_six_hour_weather_forecast (locationName,36hwf01,36hwf02,36hwf03,36hwf04,36hwf05,36hwf06,36hwf07,36hwf08,36hwf09,36hwf10,36hwf11,36hwf12,36hwf13,36hwf14,36hwf15,36hwf16,36hwf17,36hwf18,36hwf19,36hwf20,36hwf21,36hwf22,36hwf23,36hwf24,36hwf25,36hwf26,36hwf27,36hwf28,36hwf29,36hwf30,36hwf31,36hwf32,36hwf33,36hwf34,36hwf35,36hwf36,36hwf37,36hwf38,36hwf39,36hwf40,36hwf41,36hwf42,36hwf43,36hwf44,36hwf45,36hwf46,36hwf47,36hwf48,36hwf49,36hwf50,36hwf51,36hwf52,36hwf53,36hwf54,36hwf55,36hwf56,36hwf57,36hwf58,36hwf59,36hwf60,36hwf61,36hwf62) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}','{13}','{14}','{15}','{16}','{17}','{18}','{19}','{20}','{21}','{22}','{23}','{24}','{25}','{26}','{27}','{28}','{29}','{30}','{31}','{32}','{33}','{34}','{35}','{36}','{37}','{38}','{39}','{40}','{41}','{42}','{43}','{44}','{45}','{46}','{47}','{48}','{49}','{50}','{51}','{52}','{53}','{54}','{55}','{56}','{57}','{58}','{59}','{60}','{61}','{62}')"
    sql = sql.format(data['locationName'],data['36hwf01'],data['36hwf02'],data['36hwf03'],data['36hwf04'],data['36hwf05'],data['36hwf06'],data['36hwf07'],data['36hwf08'],data['36hwf09'],data['36hwf10'],data['36hwf11'],data['36hwf12'],data['36hwf13'],data['36hwf14'],data['36hwf15'],data['36hwf16'],data['36hwf17'],data['36hwf18'],data['36hwf19'],data['36hwf20'],data['36hwf21'],data['36hwf22'],data['36hwf23'],data['36hwf24'],data['36hwf25'],data['36hwf26'],data['36hwf27'],data['36hwf28'],data['36hwf29'],data['36hwf30'],data['36hwf31'],data['36hwf32'],data['36hwf33'],data['36hwf34'],data['36hwf35'],data['36hwf36'],data['36hwf37'],data['36hwf38'],data['36hwf39'],data['36hwf40'],data['36hwf41'],data['36hwf42'],data['36hwf43'],data['36hwf44'],data['36hwf45'],data['36hwf46'],data['36hwf47'],data['36hwf48'],data['36hwf49'],data['36hwf50'],data['36hwf51'],data['36hwf52'],data['36hwf53'],data['36hwf54'],data['36hwf55'],data['36hwf56'],data['36hwf57'],data['36hwf58'],data['36hwf59'],data['36hwf60'],data['36hwf61'],data['36hwf62'])

    try:
        cursor.execute(sql)
        db.commit()
        print("新增資料成功")
    except:
        db.rollback()
        print("新增失敗")
    db.close()
