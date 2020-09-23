from pages.basepage import BasePage
from pages.hotelscheduled import HotelScheduled


class HotelDetail(BasePage):
    """酒店列表页"""

    def __init__(self, mini):
        self.mini = mini

    def goto_hotel_scheduled(self):
        self.step(self.mini, '../data/hotel_detail.yaml')
        return HotelScheduled(self.mini)
