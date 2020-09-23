from pages.basepage import BasePage
from pages.hoteldetail import HotelDetail


class HotelList(BasePage):
    """酒店列表页"""

    def __init__(self, mini):
        self.mini = mini

    def goto_hotel_detail(self):
        self.step(self.mini, '../data/hotel_list.yaml')
        return HotelDetail(self.mini)
