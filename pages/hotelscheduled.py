from pages.basepage import BasePage


class HotelScheduled(BasePage):
    """酒店预订页"""

    def __init__(self, mini):
        self.mini = mini

    def save_order(self):
        """
        预订订单
        :return:
        """
        self.step(self.mini, '../data/hotel_scheduled.yaml')
        return "True"

    def goto_order_detail(self):
        self.mini.app.navigate_to("/pages/order/list/list")
        return "True"
