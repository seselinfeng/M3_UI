import time
import allure
import pytest

from pages.app import App


class TestDemo:
    def setup(self):
        self.app = App()
        self.main = self.app.start().main()
        self.routing = self.app.start().routing()
        self.order_list = self.app.start().order_list()

    @allure.title("测试demo")
    def test_demo(self):
        with allure.step("跳转到订单列表页"):
            self.routing.goto_order_list()
        time.sleep(3)
        with allure.step("滑动到页面底部"):
            self.order_list.scroll_to_footer()

    def teardown(self):
        self.app.stop()
