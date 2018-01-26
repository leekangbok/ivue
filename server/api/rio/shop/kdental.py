import treq
from bs4 import BeautifulSoup
from twisted.internet import threads


def parse(text):
    products = []
    soup = BeautifulSoup(text, 'html.parser')
    f = soup.select('div > form')
    for x in (e for e in f if e['name'].startswith('frmProduct_')):
        products.append({
            'src' : 'http://www.kdental.co.kr{}'.format(x.find_all('a')[0].find('img')['src']),
            'site': 'kdental'
        })
    return products


def get_products(product):
    d = treq.post('http://www.kdental.co.kr/shopping/search_list.php', data={
        'searchProductKeyWord' : product,
        'searchProductType'    : '',
        'searchProductKeyWord2': '',
        'searchCategoryNo'     : '',
        'orderByCol'           : 'a.productCostGen',
        'orderByAD'            : 'Asc',
        'gotoPage'             : 1,
        'listType'             : 'LIST',
        'orderBy'              : 'a.productCostGen | Asc',
        'pageSize'             : 100
    })
    d.addCallback(lambda resp: resp.text(encoding='utf-8')).addCallback(
            lambda text: threads.deferToThread(parse, text))
    return d
