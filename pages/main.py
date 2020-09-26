from pages.basepage import BasePage
from pages.hotellist import HotelList


class Main(BasePage):
    """首页"""

    def goto_day_hotel_list(self):
        """
        跳转到酒店列表页
        :return:
        """
        self.step('../data/main.yaml')
        return HotelList(self._mini)

    def goto_hour_hotel_list(self):
        """
        选择时租房后，跳转到酒店列表页
        :return:
        """
        self.step('../data/main.yaml')
        return HotelList(self._mini)

    def goto_night_hotel_list(self):
        """
        选择时租房后，跳转到酒店列表页
        :return:
        """
        self.step('../data/main.yaml')
        return HotelList(self._mini)
