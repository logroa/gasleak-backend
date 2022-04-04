import requests
from bs4 import BeautifulSoup

def get_data_oilprice():
    url = "https://oilprice.com/oil-price-charts/"
    soup = BeautifulSoup(requests.get(url).content, 'html.parser')
    results = soup.find("tbody", class_="row_holder").find_all("tr")[:3]
    prices = []
    for result in results:
        prices.append(result.find_all("td")[2].text)
    return prices

if __name__ == '__main__':
    print(get_data_oilprice())