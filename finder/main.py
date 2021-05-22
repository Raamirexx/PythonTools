import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

class Item:
    def __init__(self, modelo, cat):
        self.alltypes = [{0: 'Placa mãe'}, {1: 'HD'}, {2: 'SSD'}, {3: 'Placa de vídeo'}, {4: 'Memória RAM'},
                         {5: 'Processador'}, {6: 'Fonte'}]
        self.nome = modelo
        self.tipo = self.alltypes[cat].get(cat)

class Site:
    def __init__(self, link, title, price):
        self.searchlink = link
        self.title = title
        self.price = price

    def getpage(self, page):
        self.srcpage = page

class Search:
    def __init__(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(options=options)
        self.maincount = 0

    def specialreplace(self,str):
        if '.' in str:
            price_format = str.split('.')
            str = (price_format[0] + price_format[1])
        return str.replace(',','.')

    def lowestPrice(self,prices):
        return [float(self.specialreplace(x.text.split()[1])) for x in prices]

    def searchItem(self, site):
        self.driver.get(site.searchlink)
        time.sleep(5)
        site.getpage(self.driver.page_source)
        self.driver.quit()
        soup = BeautifulSoup(site.srcpage, 'html.parser')

        for j,k in site.title.items():
            td = soup.find_all(j, {'class':k})

        for l,m in site.price.items():
            td2 = soup.find_all(l, {'class':m})

        counter = 0
        for i in td:
            print(i.text,td2[counter].text)
            counter += 1

    def formatspace(self,str,index):
        if ' ' in str:
            if index == 0:
                str = str.replace(' ','%20')
            elif index == 1:
                str = str.replace(' ','+')
            elif index == 2:
                str = str.replace(' ', '-')
        return str




Kabum = Site(
    'https://www.kabum.com.br/cgi-local/site/listagem/listagem.cgi?string=gtx+1050+ti&btnG=',
    {"a":'sc-fzoLsD gnrNhT item-nome'},
    {'div':'sc-fznxsB ksiZrQ'})


n = input('Digite o componente que você deseja procurar:' )


MercadoLivre = Site(
    'https://lista.mercadolivre.com.br/{}#D[A:ssd%20240gb]'.format(n),
    {'h2':'ui-search-item__title ui-search-item__group__element'},
    {'span':'price-tag-fraction'})

s = Search()

Aliexpress = Site(
    'https://pt.aliexpress.com/af/{}.html?d=y&origin=n&SearchText={}&catId=0&initiative_id=SB_20210522080158'.format(s.formatspace(n,2),s.formatspace(n,1)),
    {"a":'item-title'},
    {"span":"price-current"})

Shopee = Site(
    'https://shopee.com.br/search?keyword={}'.format(n),
    {'div':'yQmmFK _1POlWt _36CEnF'},
    {'span':'_29R_un'}
)

s.searchItem(Aliexpress)

