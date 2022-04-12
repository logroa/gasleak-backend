import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re

def solve(s):                                             
    return re.sub(r'(\d)(st|nd|rd|th)', r'\1', s)

def get_data_oilprice():
    prices_url = "https://oilprice.com/oil-price-charts/"
    soup = BeautifulSoup(requests.get(prices_url).content, 'html.parser')
    results = soup.find("tbody", class_="row_holder").find_all("tr")[:3]
    prices = [datetime.today()]
    for result in results:
        prices.append(result.find_all("td")[2].text)
    
    counts_url = "https://oilprice.com/rig-count"
    soup = BeautifulSoup(requests.get(counts_url).content, 'html.parser')
    results = soup.find("div", class_="info_table_holder").find("div", class_="info_table").find("div", class_="info_table_row")
    counts = []
    for result in results.find_all("div"):
        counts.append(result.text.strip())
    counts[0] = datetime.strptime(solve(counts[0]), '%d %b %Y')
    return prices, counts

if __name__ == '__main__':
    prices, counts = get_data_oilprice()
    print(prices)
    print(counts)