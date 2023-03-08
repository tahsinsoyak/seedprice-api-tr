import pandas as pd
from bs4 import BeautifulSoup
import requests
import random


def _scrape_data():
    urunismi = []
    urunfiyat = []

    file1 = open('user-agents.txt', 'r')
    Lines = file1.readlines()
    

    for page in range(1,12):
        random_user_agent = random.choice(Lines)
        header = {
                'User-Agent': random_user_agent.strip()
            }
        next_page = requests.get(f"https://www.fidedeposu.com/kategori/ucuz-organik-tohum-fiyatlari?stoktakiler=1&tp={page}",headers=header)
        print(next_page.url)
        html_content = next_page.content
        soup = BeautifulSoup(html_content, 'html.parser')
        container = soup.find('div',{"class" : 'showcase-container'} )
        for urun in container.find_all('div',{"class" : 'showcase-inner'}):
                a = urun.find('div',{"class" : 'showcase-price-new'})
                urunfiyat.append(a.text.strip())
                b = urun.find('div',{"class" : 'showcase-title'})
                urunismi.append(b.text.strip())

    df = pd.DataFrame({'urunismi': urunismi,
                       'urunfiyat': urunfiyat
                       })
    return df


def _kaydet():
    dataframe = pd.DataFrame()
    dataframe = _scrape_data()
    result = dataframe.to_json(orient="records")
    with open(f"tohumfiyatlari.json", "w") as file:
        file.write(result)
        file.close()

if __name__ == "__main__":
    _kaydet()
