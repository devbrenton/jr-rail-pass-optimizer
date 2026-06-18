# Query needs to be in Japanese Characters (KANJI)
# TODO: Build web scraper that queries yahoo online transit, parses the data
# https://transit.yahoo.co.jp/search/result?from=%E6%9D%B1%E4%BA%AC&to=%E5%93%81%E5%B7%9D&ticket=ic&expkind=1
import requests
import re
import time
import random
import pandas as pd
from bs4 import BeautifulSoup
df = pd.read_csv("data/stations_cleaned.csv", encoding="utf-8-sig", comment='#')
station_lookup = df.set_index("station_name_rn")["station_name"].to_dict()
def process_string(s):
    transformed = s[5:s.find("円")]
    if transformed.find(",") != -1:
        transformed = transformed[0:transformed.find(",")]+transformed[transformed.find(",")+1:]
    
    return int(transformed)
def translate(s):
    s = s.upper()
    try:
        return station_lookup[s]
    except:
        raise ValueError(f"\033[91mStation name {s} is NOT in dataset, please check again\033[0m")
        
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
origin = ""
dest = ""

min_cost = []
max_cost = []
warnings = []
# Take user input
# TODO: move user input part to main.py
with open('input.txt', 'r', encoding="utf-8") as file:
    for line in file:
        origin_raw, dest_raw = map(str, line.split())
        origin = translate(origin_raw)
        dest = translate(dest_raw)
        print(origin, ' ', dest)
        time.sleep(random.uniform(1, 2))
        # Requesting for info from Yahoo Transit
        url = f"https://transit.yahoo.co.jp/search/result?from={origin}&to={dest}&ticket=normal&expkind=2&shin=1&ex=1&y=2026&m=06&d=19&hh=12&m1=5&m2=0"
        response = requests.get(url, headers=headers)

        if (response.status_code != 200):
            print("ERROR FAILED TO GET RESULT FROM YAHOO TRANSIT")
        else:
            print("SUCCESSFULLY GOT RESULT FROM YAHOO TRANSIT")

        soup = BeautifulSoup(response.text, "html.parser")
        route01 = soup.find("div", id="route01")

        # If route01 is non-existent, impossible to transit between the origin and destination
        if (route01 == None):
            print("Route is non-existent for trains on Yahoo Transit, please input another route")
            continue

        # Check if route01 is fully JR
        sections01 = route01.find_all("li", class_="transport")
        for i in sections01:
            flag = i.find(string=re.compile("ＪＲ"))
            flag2 = i.find(string=re.compile("徒歩"))
            #print(flag)
        
        print("DEBUG: ", flag) # DELETE LATER

        aux = []
        # route01 is fully JR, find fare
        if (flag != None) or (flag2 != None):
            for i in route01:
                i = route01.find("li", class_="fare")

                # Print fare
                aux.append(process_string(i.get_text(strip=True)))
                break

        # Check if route02 is fully JR
        route02 = soup.find("div", id="route02")
        if (route02 != None):
            sections02 = route02.find_all("li", class_="transport")
            for i in sections02:
                flag = i.find(string=re.compile("ＪＲ"))
                flag2 = i.find(string=re.compile("徒歩"))
            print("DEBUG: ", flag) # DELETE LATER

            # route02 is fully JR, find fare
            if (flag != None) or (flag2 != None):
                for i in route02:
                    i = route02.find("li", class_="fare")

                    aux.append(process_string(i.get_text(strip=True)))
                    break
        # Check if route03 is fully JR
        route03 = soup.find("div", id="route03")
        if (route03 != None):
            sections03 = route03.find_all("li", class_="transport")
            for i in sections03:
                flag = i.find(string=re.compile("ＪＲ"))
                flag2 = i.find(string=re.compile("徒歩"))
            
            print("DEBUG: ", flag) # DELETE LATER

            # route03 is fully JR, find fare
            if (flag != None) or (flag2 != None):
                for i in route03:
                    i = route03.find("li", class_="fare")

                    aux.append(process_string(i.get_text(strip=True)))
                    break
        mn = 2147483647
        mx = -mn
        if (len(aux)==0):
            temp = []
            temp.append(origin_raw)
            temp.append(dest_raw)
            warnings.append(temp)
        for i in aux:
            mn = min(mn, i)
            mx = max(mx, i)
        if (mn != 2147483647):
            min_cost.append(mn)
        if (mx != -2147483647):
            max_cost.append(mx)
        print(aux)
        aux.clear()
print("Minimum cost: ", min_cost)
print(sum(min_cost))
print("Maximum cost: ", max_cost)
print(sum(max_cost))
for i in warnings:
    print(f"\033[91mWARNING: {i[0].upper()} to {i[1].upper()} HAS NO RESULTS AND THUS IS NOT CALCULATED IN THE TOTAL")
    print("Reasons could include no valid routes, no JR coverage etc etc...")
    print(f"You can edit your input to fix the problem (Try putting a nearby station/major hub as your origin!)\033[0m")