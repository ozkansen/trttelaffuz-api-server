import json
from typing import TypeVar

import requests
from bs4 import BeautifulSoup

Json = TypeVar("Json")

INFO = {
    "title": "TRT Telaffuz Sözlüğü",
    "site": "http://trttelaffuz.com",
    "description": "Kelimelerin telaffuz, vurgu ve okunuş "
                   "örneklerinin olduğu medya objelerinin olduğu sitedir.",
    "plugin": "TrtTelaffuz"
}


class TrtTelaffuz:
    def __init__(self, keyword):
        self.keyword = keyword

    def search(self) -> bytes:
        """Sayfa html içeriğini getirir"""
        url = f"http://trttelaffuz.com/ara/?q={self.keyword}"
        r = requests.get(url)
        return r.content

    def result_single(self, url: str) -> dict:
        """Kelime detaylarını sözlüğe ekli olarak getirir"""
        content = requests.get(url).content
        soup = BeautifulSoup(content, 'lxml')

        # Container id li div tagını ara
        find = (soup.find_all('div', {'id': 'container'})).pop()

        detail = dict()
        detail["key"] = find.find('p').text
        detail["source"] = INFO["site"] + find.find('audio').source.get('src')

        # Kelime açıklamalarını listeye al
        link = find.find_all('div', {'class': 'description'})
        description = []
        for i in link:
            description.append(i.text.strip())
        detail['description'] = description

        return detail

    def result_list(self) -> dict:
        content = self.search()
        soup = BeautifulSoup(content, 'lxml')

        find = soup.find_all('div', {'class': 'result'})
        collect_data = dict()
        for i in find:
            keyword = i.text.replace("\n", "")
            url_path = i.find('a').get('href')
            url = INFO["site"] + url_path
            collect_data[keyword] = {
                'url': url,
                'detail': self.result_single(url)
            }

        return collect_data

    def return_dict_data(self) -> dict:
        data = self.result_list()
        return data

    def return_json_data(self) -> Json:
        data = self.result_list()
        json_data = json.dumps(data)
        return json_data
