from abc import ABCMeta, abstractmethod
from model.bases import Bases
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

