def get_free_seats():
    import requests

    url = "https://app.testcenter.kz/ent/student/app/api/v1/app/season/items/26/app-type/items/15/test-org/items/1052/test-period/items?student-test-id=0"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ru-RU,ru;q=0.7",
        "Authorization": "Bearer eyJhbGciOiJSUzI1NiJ9.eyJpaW5IYXNoIjoiODIzQTBGNDFCQzlERUQ0NUY1NUJGREM0NEM0NkExQkUiLCJ1c2VyUm9sZUlkIjoxLCJ1c2VySWQiOjE2NzQzNzl9.jWnOlnLY2t6BV9KjN-EnPThzSAdpNUsUcOOVuI2F6THAF95tYoqXHXhD3iMlGk6z_ynLBxG4LjDteMCEFb8sXo46ay2JD-dhEmCRgJMmPikwLzuzaqHAS8XokQI9Lk8ERAjTh0jqXjSVSSPZWSC4Bn16wFVIylsggmCT6MBUmCBCXPfxkRvcdS5XHiy6MXDUtj3sTNmKJ_ExYNlivcV60aBky6TqHvnNZupFf9qAhZV0Z_h9Sm7lXHSm0gOPNi6U966OH_LRbGdz7XN6e80ziDbUkI8Me1BUdloBN-k8Ub76pPl8XeMie2E_QS97G3ya2nMVdH_Em-1u3iWlXAu1eQ",
        "Connection": "keep-alive",
        "Host": "app.testcenter.kz",
        "Referer": "https://app.testcenter.kz/profile/applications/2/seasons/26/VTG?appTypeId=15",
        "Sec-Ch-Ua": '"Not_A Brand";v="8", "Chromium";v="120", "Brave";v="120"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Gpc": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        res = ''
        for i in data['items']:
            formatted_message = (
                f"📅 *Дата тестирования:* {i['testDate']}\n"
                f"⏰ *Время Входа:* {i['enterTime']}\n"
                f"🚀 *Время Начала:* {i['startTime']}\n"
                f"🆔 *ID Тестирования:* {i['id']}\n"
                f"🆓 *Свободных мест:* {i['freePlaceCount']}\n"
            )

            res+=formatted_message+"\n"
        print(res)
    else:
        print(f"Request failed with status code: {response.status_code}")
    

get_free_seats()