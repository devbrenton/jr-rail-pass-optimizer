from bs4 import BeautifulSoup
import re
from utils import fare_stoi
def get_route(soup, route_id):
    route = soup.find("div", id=route_id)
    return route
def check_jr(route):
    sections = route.find_all("li", class_="transport")
    for i in sections:
        flag = i.find(string=re.compile("ＪＲ"))
        flag2 = i.find(string=re.compile("徒歩"))
        if (flag == None) and (flag2 == None):
            break
    print("DEBUG: ", flag)
    if (flag == None) and (flag2 == None):
        return False
    else:
        return True
def find_fare(route):
    fare = 0 
    for i in route:
        i = route.find("li", class_="fare")
        fare = fare_stoi(i.get_text(strip=True))
        break
    return fare

