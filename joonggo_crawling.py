import requests

from bs4 import BeautifulSoup

BASE_URL = 'http://cafe.naver.com/ArticleList.nhn?search.clubid=10050146&'


def get_response_text(url, **kwargs):
    try:
        response = requests.get(url, **kwargs)
        return response.text
    except requests.exceptions.ConnectionError:
        return 'Connection Failed!'


def crawl_joonggo(category, page):
    url = BASE_URL + 'search.menuid={0}&search.page={1}'.format(category, page)
    resp = get_response_text(url)

    html = BeautifulSoup(resp, 'lxml')
    tr_list = html.select(
        'form[name="ArticleList"] tr[align="center"] td[class="board-list"] span[class="aaa"] a[onmouseover]'
    )
    page_category = html.select(
        'div#sub-tit > h3 > a#favorite'
    )

    print(page_category[0].text)
    for tr in tr_list:
        print(tr.text)


if __name__ == '__main__':
    try:
        category, page = input('Category, Page: ')
    except Exception as e:
        category = 387
        page = 1

    crawl_joonggo(category, page)
