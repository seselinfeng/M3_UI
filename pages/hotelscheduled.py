from pages.basepage import BasePage


class HotelScheduled(BasePage):
    """酒店预订页"""

    def save_order(self):
        """
        预订订单
        :return:
        """
        self.step('../data/hotel_scheduled.yaml')
        return HotelScheduled(self._mini)

