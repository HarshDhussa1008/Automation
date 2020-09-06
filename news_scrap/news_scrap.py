import sys,requests
from bs4 import BeautifulSoup as bs

category=' '.join(sys.argv[1:])
url='https://indianexpress.com/?s='+category
try:
    r=requests.get(url)
except:
    print("Error in fetching the page..")
try:
    r.raise_for_status()
except:
    print("Error in fetching the page..")
try:
    soup=bs(r.content,'html5lib')

    table=soup.findAll('div',{'class':'details'})
    for li in table:    
        pic_div=li.find('div',{'class':'picture'})
        link=pic_div.find('a')
        title_div=li.find('h3')
        title=title_div.find('a')
        print('Title:',title['title'])
        print('URL:',link['href'])
        detail=li.find('p')
        print('Detail',detail.string)
        print()
except:
    print('Nothing Found!')
