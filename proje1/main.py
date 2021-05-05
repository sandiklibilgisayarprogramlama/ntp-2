"""
requests
beatifulsoap4
peewee
telegram-send

pip install 
"""

import requests
import bs4 
import telegram_send


from database import *
r = requests.get("https://sandiklimyo.aku.edu.tr").text
#token
# 1695748283:AAFswMVdYK-LrXT6ZeTlWI0ImWxloeYu_GI

soup = bs4.BeautifulSoup(r,"html.parser")
all_news = soup.find_all('div', 'ne-title-created')
for n in all_news:
    haberbaslik=n.find("a").get('title')
    haberlink=n.find("a").get('href')
    query=Haberler.select().where((Haberler.haber==haberbaslik)).limit(1)
    if len(query)==0:
        telegram_send.send(messages=[haberbaslik+" "+haberlink])
        haber = Haberler.create(haber=haberbaslik)
        haber.save()