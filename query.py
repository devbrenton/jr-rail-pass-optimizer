# Query needs to be in Japanese Characters (KANJI)
# TODO: Build web scraper that queries yahoo online transit, parses the data
# https://transit.yahoo.co.jp/search/result?from=%E6%9D%B1%E4%BA%AC&to=%E5%93%81%E5%B7%9D&ticket=ic&expkind=1
import requests
import re
from bs4 import BeautifulSoup
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
origin = ""
dest = ""

# Take user input
while (origin != "-1") and (dest != "-1"):
    origin = str(input("Enter Origin "))
    dest = str(input("Enter Destination "))

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
    if (len(route01) == 0):
        print("Route is non-existent for trains on Yahoo Transit, please input another route")
        continue

    # Check if route01 is fully JR
    sections01 = route01.find_all("li", class_="transport")
    for i in sections01:
        flag = i.find(string=re.compile("ＪＲ"))
        #print(flag)
    
    print("DEBUG: ", flag) # DELETE LATER

    # route01 is fully JR, find fare
    if (flag != None):
        for i in route01:
            i = route01.find("li", class_="fare")

            # Print fare
            print(i.get_text(strip=True))
            break

    # Check if route02 is fully JR
    route02 = soup.find("div", id="route02")
    sections02 = route02.find_all("li", class_="transport")
    for i in sections02:
        flag = i.find(string=re.compile("ＪＲ"))

    print("DEBUG: ", flag) # DELETE LATER

    # route02 is fully JR, find fare
    if (flag != None):
        for i in route02:
            i = route02.find("li", class_="fare")

            # Print fare
            print(i.get_text(strip=True))
            break
    # Check if route03 is fully JR
    route03 = soup.find("div", id="route03")
    sections03 = route03.find_all("li", class_="transport")
    for i in sections03:
        flag = i.find(string=re.compile("ＪＲ"))
    
    print("DEBUG: ", flag) # DELETE LATER

    # route03 is fully JR, find fare
    if (flag != None):
        for i in route03:
            i = route03.find("li", class_="fare")

            # Print fare
            print(i.get_text(strip=True))
            break  
