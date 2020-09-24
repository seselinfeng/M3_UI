from pages.basepage import BasePage
from pages.hotellist import HotelList


class Main(BasePage):
    """首页"""
    # def __init__(self):
    #     """
    #     初始化首页
    #     :param mini:
    #     """
    #     # self.mini = mini

    def goto_hotel_list(self):
        """
        跳转到酒店列表页
        :return:
        """
        self.step('../data/main.yaml')
        return HotelList(self._mini)
