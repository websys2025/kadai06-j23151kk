import requests

APP_ID = "611ce910ee186743e6be8d9b00d5ccb8ea4eae19"
API_URL  = "https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"

params = {
    "appId": APP_ID,
    "statsDataId":"0000020201",
    "cdArea":"12101,12102,12103,12104,12105,12106",
    "cdCat01": "A1101",  # 総人口
    "metaGetFlg":"Y",
    "cntGetFlg":"N",
    "explanationGetFlg":"Y",
    "annotationGetFlg":"Y",
    "sectionHeaderFlg":"1",
    "replaceSpChars":"0",
    "lang": "J"
}

response = requests.get(API_URL, params=params)
data = response.json()

try:
    values = data['GET_STATS_DATA']['STATISTICAL_DATA']['DATA_INF']['VALUE']
    class_objs = data['GET_STATS_DATA']['STATISTICAL_DATA']['CLASS_INF']['CLASS_OBJ']

    area_dict = {}
    for obj in class_objs:
        if obj['@id'] == 'area':
            for area in obj['CLASS']:
                area_dict[area['@code']] = area['@name']

    print("地域別人口データ:")
    for item in values:
        area_code = item['@area']
        year_raw = item['@time']
        year = year_raw[:4]  # 例: "1980100000" → "1980"
        value = item['$']
        area_name = area_dict.get(area_code, area_code)
        formatted_value = f"{value}人" if value != "-" else "データなし"
        print(f"{year}年 - {area_name}: {formatted_value}")

except KeyError as e:
    print("データ取得または整形中にエラーが発生しました:", e)
