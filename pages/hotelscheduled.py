from pages.basepage import BasePage


class HotelScheduled(BasePage):
    """酒店预订页"""

    def __init__(self, mini):
        self.mini = mini

    def save_order(self):
        self.step(self.mini, '../data/hotel_scheduled.yaml')
        return "True"
