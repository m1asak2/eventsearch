from model.event import Event, EventTable
from typing import List
import os
from bs4 import BeautifulSoup
import requests
import datetime
from model.bases import Bases
from domain.searchbase import SearchBase
import re


class Doorkeeper(SearchBase):
    def __init__(self):
        self.__domain = "http://api.doorkeeper.jp/events/"

    def convert(self, data: Event):
        if data.address:
            tmp = [f"prefecture={value}" if value != "online" and value is str else ""
                   for value in data.address]
            address = "&" + \
                '&'.join(tmp)
            if address == "&":
                address = ""
        else:
            address = ""
        start = f"&since={data.start_from}"
        end = f"&until={data.start_to}"
        # limit = f"&page={data.limit}"
        sort = "&sort=starts_at"
        keyword = "?q="
        keyword += "+".join([f"{value}" for value in data.keyword])
        url = f"{self.__domain}{keyword}{start}{end}{address}{sort}"
        print(url)
        return url, data.limit

    def get(self, url, limit=0):
        events: list = requests.get(url).json()

        tablelist: List[EventTable] = []
        regex_year = re.compile(r'\d{4}-\d{2}-\d{2}')
        regex_time = re.compile(r'\d{2}:\d{2}')
        # print(events)
        for i, dic in enumerate(events):
            res = dic["event"]
            title = res["title"]
            # day, time = str(res["starts_at"].split("T")[0]), str(res["starts_at"].split("T")[1])
            address = 'オンライン' if res["address"] is None else res["address"]
            # group = res[""]
            img = res["banner"]
            link = res["public_url"]
            res = requests.get(link)
            soup = BeautifulSoup(res.text, "html.parser")
            info_date: str = soup.select_one('.community-event-info-date').text.strip()

            day = regex_year.search(info_date).group(0)
            time = regex_time.search(info_date).group(0)
            group: str = soup.select_one('.community-header-info').select_one('.community-title').select_one('a').text
            tablelist.append(EventTable(
                address=address, title=title, day=day, time=time, group=group, img=img, link=link))
            if i >= limit:
                break
        return tablelist
