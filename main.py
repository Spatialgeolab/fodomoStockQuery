from sendLine import sendNotifucationToLine
import requests
import pandas as pd
import time
import random
def queryGood(base_url, params, sid_values,keyword):
    current_params = params.copy()
    # 變更要查詢的分店
    current_params["sid"] = sid_values
    current_params['keyword']=keyword
    response = requests.get(base_url, params=current_params)
    return response

# 基本URL和查詢參數
base_url = "https://opennow.foodomo.com/app/wxapp.php"
params = {
    "i": 1,
    "m": "ht_wmps",
    "c": "entry",
    "do": "mobile",
    "lang": "zh-cn",
    "ctrl": "wmall",
    "ac": "store",
    "op": "goods",
    "ta": "list",
    "from": "vue",
    "u": "wap",
    "sid": 3560,
    "gid": 1065662,
    "keyword": "Dinotaeng",
    "page": 1,
    "psize": 20
}
# 這邊可以透過pandas先篩選要查詢的商店列表
df=pd.read_csv('./store_id.csv',)
# 我只篩選彰化、台中的分店
filtered_df = df[df['addr'].str.contains('台中|彰化')]
# print(filtered_df.iloc[0]['sid'])
# print(filtered_df.index)
flag=0
while flag==0:
    for i,row in filtered_df.iterrows():
        print(f'查詢 sid:{row["sid"]} ->{row["name"]}')
        time.sleep(random.uniform(0.5,1.5))
        res=queryGood(base_url,params,row['sid'],'Dinotaeng')
        if res.status_code != 200:
            print("Error: ", res.status_code)
            #sendNotifucationToLine(f"error : {res.status_code}")
            continue
        if len(res.json()['message']['message']['goods'])!=0:
            sendNotifucationToLine(f"{row['sid']} ->{row['name']} 發現:樂事 X Dinotaeng 歡樂分享組 \n 購買連結:https://opennow.foodomo.com/m/index.html#/?sid={row['sid']} \n  地址:{row['addr']}")
            # 可以透過flag控制是否切斷while loop
            # flag=1
            # break