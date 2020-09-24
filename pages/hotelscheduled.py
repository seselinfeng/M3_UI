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

    def goto_order_detail(self):
        """
        跳转到订单列表页面
        :return:
        """
        self._mini.app.navigate_to("/pages/order/list/list")
        return "True"
