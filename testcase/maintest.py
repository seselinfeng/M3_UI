import time

import minium

from pages.app import App


class MainTest(minium.MiniTest):
    def setUp(self):
        self.app = App()
        self.main = self.app.start().main()
        self.routing = self.app.start().routing()

    def test_order(self):
        self.main.goto_hotel_list().goto_hotel_detail().goto_hotel_scheduled().save_order()
        self.routing.goto_order_list()

    def test_order_list(self):
        self.routing.goto_main()
        self.main.goto_hotel_list().goto_hotel_detail().goto_hotel_scheduled().save_order()

    def test_demo(self):
        self.routing.goto_order_list()

    def tearDown(self):
        time.sleep(10)
        pass


if __name__ == '__main__':
    minium.unittest.main()
