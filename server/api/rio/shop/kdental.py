import treq
from twisted.internet import threads


def parse(text):
    # soup = BeautifulSoup(text, 'html.parser')
    #
    # a = soup.select('tr[bgcolor=#FFFFFF]')
    #
    # for i in a:
    #     t = i.find_all('td')
    #     for _, j in enumerate(tt for tt in t if len(t) > 15):
    #         if _ == 4:
    #             print(j)

    return 'parse_kdental'


def get_prices(request):
    d = treq.post('http://www.kdental.co.kr/shopping/search_list.php',
                  data={'searchProductKeyWord': request.args.get('item')[0]})
    d.addCallback(lambda resp: resp.text(encoding='utf-8')).addCallback(
        lambda text: threads.deferToThread(parse, text))
    return d
