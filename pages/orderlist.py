from pages.basepage import BasePage
from pages.hotellist import HotelList


class OrderList(BasePage):
    """订单列表页"""

    def __init__(self, mini):
        """
        初始化订单列表页
        :param mini:
        """
        self.mini = mini

    def goto_order_detail(self):
        """
        跳转到订单详情页
        :return:
        """
        self.step(self.mini, '../data/order_list.yaml')
