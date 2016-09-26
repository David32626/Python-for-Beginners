# Reauests module
import requests

# Beautiful Soup module
from bs4 import BeautifulSoup

res = requests.get('https://www.ptt.cc/bbs/PokeMon/index.html', verify=False, cookies={'over18': '1'})
soup = BeautifulSoup(res.text) 

for item in soup.select('.r-ent'):
    print (item.select('.title')[0].text, item.select('.date')[0].text, item.select('.author')[0].text)