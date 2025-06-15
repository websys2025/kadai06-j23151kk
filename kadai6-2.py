import requests

APP_ID = "611ce910ee186743e6be8d9b00d5ccb8ea4eae19"
API_URL = "https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"

params = {
    "appId": APP_ID,
    "statsDataId": "0000020201",
    "cdArea": "13000",
    "cdCat01": "A1101",
    "lang": "J"
}

response = requests.get(API_URL, params=params)
data = response.json()

try:
    values = data['GET_STATS_DATA']['STATISTICAL_DATA']['DATA_INF']['VALUE']
    for item in values[:10]:
        print(item)
except KeyError:
    print("データ取得エラー: 'STATISTICAL_DATA' が存在しません。")

