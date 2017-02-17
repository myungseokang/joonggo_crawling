import requests

from bs4 import BeautifulSoup


def get_response_text(url, **kwargs):
    try:
        response = requests.get(url, **kwargs)
        return response.text
    except requests.exceptions.ConnectionError:
        return 'Connection Failed!'


def crawl_joonggo():
    url = 'http://cafe.naver.com/ArticleList.nhn?search.clubid=10050146&search.menuid=387&search.page=1'
    resp = get_response_text(url)

    html = BeautifulSoup(resp, 'lxml')
    tr_list = html.select('form[name="ArticleList"] tr[align="center"] td[class="board-list"] span[class="aaa"] a')

    for tr in tr_list:
        print(tr)


if __name__ == '__main__':
    crawl_joonggo()
