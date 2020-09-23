from pages.basepage import BasePage
from pages.hotellist import HotelList


class Main(BasePage):
    """首页"""
    def __init__(self, mini):
        self.mini = mini

    def goto_hotel_list(self):
        self.step(self.mini, '../data/main.yaml')
        return HotelList(self.mini)
