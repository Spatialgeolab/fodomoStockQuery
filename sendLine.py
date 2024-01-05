import requests
def sendNotifucationToLine(message):

    url = 'https://notify-api.line.me/api/notify'
    token = ['輸入自己的Line Notify token']
    data = {
        'message':message     # 設定要發送的訊息
    }
    for i in token:
        headers = {
            'Authorization': 'Bearer ' + i    # 設定權杖
        }
        data = requests.post(url, headers=headers, data=data)   # 使用 POST 方法

if __name__ == '__main__':
    sendNotifucationToLine('Hello Line Notify')