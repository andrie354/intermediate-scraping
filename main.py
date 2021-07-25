import requests
from bs4 import BeautifulSoup


url = 'https://mobil.mitula.co.id/searchC/q-mercedes-benz-w211?req_sgmt=REVTS1RPUDtVU0VSX1NFQVJDSDtTRVJQOw=='
headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'
}

r = requests.get(url, headers=headers)
print(r.status_code)