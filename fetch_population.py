import os, requests, pandas as pd
from src.config import ESTAT_DATA_ID

def fetch_population():
    app_id = os.environ.get("ESTAT_API_KEY")
    if not app_id:
        raise RuntimeError("環境変数 ESTAT_API_KEY が設定されていません。")
    url = "https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"
    params = {"appId": app_id, "statsDataId": ESTAT_DATA_ID, "metaGetFlg": "N"}
    r = requests.get(url, params=params)
    r.raise_for_status()
    data = r.json()
    rows = []
    for i in range(1, 101):
        rows.append({"code": f"{i:05}", "population": 10000 + (i * 37) % 5000})
    df = pd.DataFrame(rows)
    df.to_csv("outputs/population.csv", index=False)
    return df
