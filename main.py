import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

w211 = []

for x in range(1,8):
    url = 'https://mobil.mitula.co.id/searchC/sortir-0/q-mercedes-benz-w211/halaman-'
    r = requests.get(url+str(x))
    soup = BeautifulSoup(r.text, 'html.parser')
    cars = soup.find_all('a', {'class': 'lis_ting_AdContainer'})
    for car in cars:
        name = car.find('h4').text
        price = car.find('div',{'class': 'adPrice'}).text
        car_info = {
            'name': name,
            'price': price
        }
        w211.append(car_info)
    print('Used W211 Found:', len(w211))
    time.sleep(1)

df = pd.DataFrame(w211)
print(df.head())

df.to_csv('w211.csv')