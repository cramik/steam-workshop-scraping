# importing the modules
import requests
from bs4 import BeautifulSoup
import time
 
 
baseurl = 'https://steamcommunity.com/sharedfiles/filedetails/?id='
i = 1



while True:
  print(i)
  reqs = requests.get(baseurl + str(i))
  soup = BeautifulSoup(reqs.text, 'html.parser')
  for title in soup.find_all('title'):
    if "Error" not in title.get_text():
        f = open("idscrape.txt", "a")
        f.write(str(i) + " - " + title.get_text() + "\n")
        f.close()
  time.sleep(5)
  i+=1