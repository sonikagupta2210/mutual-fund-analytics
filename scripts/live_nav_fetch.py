import requests
import pandas as pd

schemes = {
    "sbi_bluechip": 119552,
    "icici_bluechip": 120504,
    "nippon_largecap": 118633,
    "axis_bluechip": 119093,
    "kotak_bluechip": 120841
}

for name, code in schemes.items():

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed for {name}")
        continue

    data = response.json()

    print(f"\nFetching {name}")
    print(data["meta"]["scheme_name"])

    df = pd.DataFrame(data["data"])

    df.to_csv(
        f"data/raw/{name}_live_nav.csv",
        index=False
    )

    print(f"Saved {len(df)} records")