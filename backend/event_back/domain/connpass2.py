import os
import requests
import datetime
from dateutil.relativedelta import relativedelta

from bs4 import BeautifulSoup
from typing import List
from model.event import Event, EventTable
from model.bases import Bases
from domain.searchbase import SearchBase
domain = "https://connpass.com/api/v1/event/"
key = "python"
keyword = f"?keyword={key}"


search = f"{domain}{keyword}"


class Connpass(SearchBase):
    def __init__(self):
        self.__domain = "https://connpass.com/search/"

    def convert(self, data: Event):
        if data.address:
            address = "&" + \
                '&'.join([f"prefectures={value}" for value in data.address])
        else:
            address = ""
        start = f"&start_from={data.start_from}"
        end = f"&start_to={data.start_to}"
        keyword = f"?q={data.keyword[0]}" + r"+" + \
            "+".join([f"{value}" for value in data.keyword[1:]])
        url = f"{self.__domain}{keyword}{start}{end}{address}"
        return url, data.limit

    def get(self, url, limit=100):
        # events = requests.get(url).json()["events"]
        # events = requests.get(
        #     "https://connpass.com/api/v1/event/?keyword=python&keyword_or=osaka,=online&order=1").json()["events"]
        # print(len(events))
        # events = requests.get(
        #     "https://connpass.com/api/v1/event/?keyword=python&keyword=osaka&order=1").json()["events"]
        # print(len(events))

        # res = requests.get(
        #     "https://connpass.com/search/?q=python&start_from=2021/01/18&start_to=2021/07/05&prefectures=osaka&selectItem=osaka")
        res = requests.get(url)
        print(url)
        soup = BeautifulSoup(res.text, "html.parser")
        tablelist: List[EventTable] = []
        while(True):
            events = soup.select(".event_list")
            for event in events:
                # 両端の改行、タブ、空白を削除
                schedule_area = event.select_one('.event_schedule_area')
                event_detail_area = event.select_one('.event_detail_area')
                day = f"{schedule_area.select('.year')[0].text}/{schedule_area.select('.date')[0].text}"
                time = (event_detail_area.select_one('.event_label_area').select_one(".time").text).replace("~", "").replace("〜", "")
                address = event_detail_area.select_one(".icon_place").text.strip()
                title = event_detail_area.select_one(
                    ".event_title").select_one("a").text
                if event_detail_area.select_one(".series_title"):
                    group = event_detail_area.select_one(".series_title").text
                else:
                    group = ""
                img = event_detail_area.select_one(
                    '.image_link').select_one("img")['src']
                link = event_detail_area.select_one(".event_title").a.get("href")
                tablelist.append(EventTable(
                    address=address, title=title, day=day, time=time, group=group, img=img, link=link))
                if len(tablelist) >= limit:
                    return tablelist
            if len(soup.select(".to_next")) > 0:
                next_page = soup.select_one(".to_next").a.get("href")
                url = self.__domain + next_page
                res = requests.get(url)
                soup = BeautifulSoup(res.text, "html.parser")
            else:
                return tablelist


# abc = Connpass()
# ev = {
#     "address": ["osaka", "online"],
#     "start_from": '2019-11-03',
#     "start_to": '2021-11-03',
#     "keyword": ["python", "api"],
#     "limit": 1
# }
# daddd = Event(**ev)
# tmp = abc.convert(daddd)
# abc.get(tmp)


class Factory:
    def __init__(self, strategy: SearchBase):
        self.strategy = strategy()
        print(strategy)
        # self.base = SearchBase()

    def check_strategy(self):
        print(self.strategy.__class__.__name__)
        return self.strategy.__class__.__name__

    def get_event(self, data: Bases):
        return self.strategy.get_event(data)


# def main():
#   a = Connpass()
#   b = {"key": "python", "address": "osaka"}
#   # print(b)
#   # res = a.get(a.convert(b))
#   # print(res)

#   fac = Factory(Connpass)
#   print(fac.get_event(b))
#   # print(fac.check_strategy())


# if __name__ == "__main__":
#   main()
