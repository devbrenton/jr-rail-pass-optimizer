import pandas as pd
df = pd.read_csv("data/3!stations.csv")
to_drop = [
    "station_name_k",
    "station_name_r",
    "station_name_zh",
    "station_name_ko",
    "station_number1",
    "station_number2",
    "station_number3",
    "station_number4",
    "three_letter_code",
    "pref_cd",
    "post",
    "address",
    "open_ymd",
    "close_ymd",
    "e_status",
    "e_sort"
]
df = df.drop(columns = to_drop)
df.to_csv('stations_cleaned.csv', index=False)