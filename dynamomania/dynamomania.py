import requests
import time

from bs4 import BeautifulSoup
from plyer import notification

url = 'https://www.dynamomania.com/'

html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'html.parser')
contentTable = soup.find('div', { "class" : "news"})

news = contentTable.find('div', { "class" : "text-main bold"})

time.sleep(60)

while True:
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'html.parser')
    contentTable = soup.find('div', { "class" : "news"})
    news2 = contentTable.find('div', { "class" : "text-main bold"})
    if news2.get_text() != news.get_text():
            notification.notify(
            title='Dynamomania.com',
            message=news2.get_text(),
            app_icon='icon.ico',
            timeout=10,)
            news = news2
            
    time.sleep(120)
