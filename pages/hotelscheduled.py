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
        return HotelScheduled(self.mini)

    def goto_order_detail(self):
        """
        跳转到订单列表页面
        :return:
        """
        self.mini.app.navigate_to("/pages/order/list/list")
        return "True"
