import requests as rq
from bs4 import BeautifulSoup

URL = "https://www.amazon.com/dp/B01NBKTPTS?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "Accept-Language":"pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7",
}

response = rq.get(URL, headers=headers)
amazon_site = response.text
soup = BeautifulSoup(amazon_site, "html.parser")
price = soup.find_all(name="span", class_="a-offscreen")[0].getText().split("$")[1]
print(price)
