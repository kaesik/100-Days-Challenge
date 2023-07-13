import os
import requests as rq
import smtplib as smtp
from bs4 import BeautifulSoup

TWILLIO_SID = os.environ.get("TWILLIO_SID")
TWILLIO_TOKEN = os.environ.get("TWILLIO_TOKEN")
USER = "kaes100day@gmail.com"
ADRS = "kamil.sobania.97@gmail.com"
PASSWORD = os.environ.get("PASSWORD")
URL = "https://www.amazon.com/dp/B01NBKTPTS?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "Accept-Language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7",
}

response = rq.get(URL, headers=headers)
amazon_site = response.text
soup = BeautifulSoup(amazon_site, "html.parser")
# print(soup.prettify())
price = float(soup.find_all(name="span", class_="a-offscreen")[0].getText().split("$")[1])
title = soup.find_all(name="img", class_="a-lazy-loaded", id="comparison_image")[0].get("alt")

if price < 99.99:
    with smtp.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=USER, password=PASSWORD)
        connection.sendmail(from_addr=USER, to_addrs=ADRS,
                            msg=f"Subject:Sale!\n\n"
                                f"Your {title} is on Sale.\n"
                                f"Its cost {price}$\n"
                                f"Here is link: {URL}".encode("UTF-8"))