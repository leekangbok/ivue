import treq
from bs4 import BeautifulSoup
from twisted.internet import threads


def parse(text):
    IMAGE = 2
    products = []
    soup = BeautifulSoup(text, 'html.parser')
    a = soup.select('tr[bgcolor=#FFFFFF]')

    for i in a:
        t = i.find_all('td')
        for _, j in enumerate(tt for tt in t if len(t) > 15):
            # if _ == 4:
            #     print(j)
            if _ == IMAGE:
                products.append({
                    'src' : 'http://www.edent.co.kr{}'.format(j.find_all('img')[0]['src'].replace('_s1_', '_b1_')),
                    'site': 'edent'
                })
    return products


def get_products(product):
    d = treq.get('http://www.edent.co.kr/search/'
                 'search.php?top_search_sca_cookie=&inc_wish=1&'
                 'top_stx={}&top_sca=5'.format(product))
    d.addCallback(lambda resp: resp.text(encoding='utf-8')).addCallback(
            lambda text: threads.deferToThread(parse, text))
    return d
