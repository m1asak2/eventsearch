
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

