import requests

from bs4 import BeautifulSoup


def get_response(url, **kwargs):
    try:
        response = requests.get(url, **kwargs)
        return response
    except requests.exceptions.ConnectionError as e:
        print('Connection Failed!')

URL = 'http://cafe.naver.com/ArticleList.nhn?search.clubid=10050146&search.menuid=387&search.page=1'

resp = get_response(URL)
html_table = BeautifulSoup(resp.text, 'lxml')
tr_list = html_table.select('form[name="ArticleList"] tr[align="center"] td[class="board-list"] span[class="aaa"] a')

for tr in tr_list:
    print(tr)


