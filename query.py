import requests
import sys
def yahoo_query(origin, dest):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    url = f"https://transit.yahoo.co.jp/search/result?from={origin}&to={dest}&ticket=normal&expkind=2&shin=1&ex=1&y=2026&m=06&d=19&hh=12&m1=5&m2=0"
    response = requests.get(url, headers=headers)
    if (response.status_code != 200):
        print("ERROR FAILED TO GET RESULT FROM YAHOO TRANSIT")
        sys.exit()
    else:
        print("SUCCESSFULLY GOT RESULT FROM YAHOO TRANSIT")
    return response
