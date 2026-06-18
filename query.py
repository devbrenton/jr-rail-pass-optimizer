# Query needs to be in Japanese Characters (KANJI)
# TODO: Build web scraper that queries yahoo online transit, parses the data
# https://transit.yahoo.co.jp/search/result?from=%E6%9D%B1%E4%BA%AC&to=%E5%93%81%E5%B7%9D&ticket=ic&expkind=1
import requests
from bs4 import BeautifulSoup
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
origin = str(input("Enter Origin"))
dest = str(input("Enter Destination"))
url = f"https://transit.yahoo.co.jp/search/result?from={origin}&to={dest}&ticket=normal&expkind=2&shin=1&ex=1&y=2026&m=06&d=19&hh=12&m1=5&m2=0"
response = requests.get(url, headers=headers)

if (response.status_code != 200):
    print("ERROR FAILED TO GET RESULT FROM YAHOO TRANSIT")
else:
    print("SUCCESSFULLY GOT RESULT FROM YAHOO TRANSIT")
soup = BeautifulSoup(response.text, "html.parser")
ar = soup.find_all("li", class_="fare")
for i in ar:
    print(i.get_text(strip=True))