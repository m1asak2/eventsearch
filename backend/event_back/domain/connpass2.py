import os
import requests
import datetime
from dateutil.relativedelta import relativedelta
from abc import ABCMeta, abstractmethod
from bs4 import BeautifulSoup
from typing import List
from model.event import Event, EventTable
from model.bases import Bases
domain = "https://connpass.com/api/v1/event/"
key = "python"
keyword = f"?keyword={key}"


search = f"{domain}{keyword}"


class SearchBase(metaclass=ABCMeta):
    def __init_value(self):
        pass

    @abstractmethod
    def convert(self, data: Bases):
        '''
        取得先に合わせて型変換
        '''
        pass

    @abstractmethod
    def get(self, url):
        pass

    def get_event(self, data: Bases):
        self.__init_value()
        url = self.convert(data)
        print(url)
        tmp = self.get(url)
        return self.terminate(tmp)

    # @abstractmethod
    def terminate(self, data):
        return data

    def day(self, month=None):
        res = datetime.date.today()
        if month:
            res += relativedelta(months=month)
        return res.strftime('%Y%m%d')

    def set_key(self, dic: dict, key: str, head: str, default=""):
        default = default if default == "" else f"{head}{default}"
        return f"{head}{dic[key]}" if key in dic else default

    def set_set(self, data, head: str, default: ""):
        default = default if default == "" else f"{head}{default}"
        if data is List[str]:
            return [f"{head}{value}" for value in data]
        else:
            return f"{head}{data}"


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
        return url, data.count

    def get(self, url, count=100):
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
            for i, event in enumerate(events):
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
                if i + 1 >= count:
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
#     "count": 1
# }
# daddd = Event(**ev)
# tmp = abc.convert(daddd)
# abc.get(tmp)


class Doorkeeper(SearchBase):
    def __init__(self):
        self.__domain = "http://api.doorkeeper.jp/events/"

    def convert(self, dic: dict):
        address = self.set_key(dic, 'address', "&prefecture_id=")
        start = self.set_key(dic, 'start', "&since=", self.day())
        keyword = f"?q={dic['key']}" if dic["key"] != "" else ""
        url = self.__domain
        if keyword != "":
            url += f"{keyword}{address}{start}"
        print(url)
        return url

    def get(self, url):
        events = requests.get(url).json()
        print(type(events))
        # print(events)
        for dic in events:
            print(dic["event"]["title"])


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
