from pages.basepage import BasePage


class OrderList(BasePage):
    """订单列表页"""

    def scroll_to_footer(self):
        """
        滚动到页面底部
        :return:
        """
        self.step('../data/order_list.yaml')

    def goto_order_detail(self):
        """
        跳转到订单详情页
        :return:
        """
        self.step('../data/order_list.yaml')
