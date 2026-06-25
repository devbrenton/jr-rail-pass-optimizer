import pandas as pd

def get_lookup_table():
    df = pd.read_csv("data/stations_cleaned.csv", encoding="utf-8-sig", comment='#')
    station_lookup = df.set_index("station_name_rn")["station_name"].to_dict()
    return station_lookup

def translate(s, station_lookup):
    s = s.upper()
    try:
        return station_lookup[s]
    except:
        raise ValueError(f"\033[91mStation name {s} is NOT in dataset, please check again\033[0m")