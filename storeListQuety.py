import requests

def send_request_with_different_sid(base_url, params, sid_values):
    for sid in sid_values:
        current_params = params.copy()
        current_params["sid"] = sid
        response = requests.get(base_url, params=current_params)
        yield response

# 基本URL和參數
base_url = "https://opennow.foodomo.com/app/wxapp.php"
params = {
    "i": 1,
    "m": "ht_wmps",
    "c": "entry",
    "do": "mobile",
    "lang": "zh-cn",
    "ctrl": "wmall",
    "from": "vue",
    "u": "wap",
    "ac": "store",
    "op": "index",
    "ta": "index",
    "sid": 2,  # 初始sid值
    "is_house": ""
}

# 您希望替換的sid值列表
sid_values = range(7000,8000)

# 開啟檔案並寫入
with open('storeList.csv', 'a', encoding='utf-8') as f:
    f.write('sid,name,addr\n')
    for response in send_request_with_different_sid(base_url, params, sid_values):
        if response.status_code == 200:
            data = response.json()
            try:
                store = data['message']['message']['store']
                print(f"{store['id']},{store['title']},{store['address']}")
                f.write(f"{store['id']},{store['title']},{store['address']}\n")
                f.flush()
            except KeyError:
                print("Invalid response format or missing data.")
        else:
            print(f"Failed to fetch data for SID {response.request.params['sid']}")