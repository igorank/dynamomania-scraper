import requests
import time
import webbrowser
import re

#from win10toast import ToastNotifier
#from plyer import notification
from bs4 import BeautifulSoup
from win10toast_click import ToastNotifier

toaster = ToastNotifier()

url = 'https://www.dynamomania.com'

html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'html.parser')
contentTable = soup.find('div', { "class" : "news"})

link = contentTable.find('a', attrs={'href' : re.compile("^/news/")})
link_title = link.find('div', { "class" : "text-main bold"})

def open_url():
    webbrowser.open_new(url + link2.get('href'))

def get_nextlink(lnk):
    lnk = lnk.find_next('a')
    return lnk

def get_nexttitle(lnk_title, lnk):
    lnk_title = lnk.find('div', { "class" : "text-main bold"})
    return lnk_title

try:
    link_title.get_text()
except AttributeError:
    link = get_nextlink(link)
    link_title = get_nexttitle(link_title,link)
        
while True:
    # reparse content
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'html.parser')
    contentTable = soup.find('div', { "class" : "news"})
    
    link2 = contentTable.find('a', attrs={'href' : re.compile("^/news/")})
    link2_title = link2.find('div', { "class" : "text-main bold"})
    
    try:
        link2_title.get_text()
    except AttributeError:
        link2 = get_nextlink(link2)
        link2_title = get_nexttitle(link2_title,link2)
   
    if link2_title.get_text() != link_title.get_text():
        toaster.show_toast(
        "Dynamomania.com",
        link2_title.get_text(), 
        icon_path='icon.ico',
        duration=60, 
        threaded=True,  
        callback_on_click=open_url 
        )
        link_title = link2_title
            
    time.sleep(60)
