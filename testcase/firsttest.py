#!/usr/bin/env python3
import time

import minium


class FirstTest(minium.MiniTest):
    # def test_get_system_info(self):
    #     sys_info = self.app.call_wx_method("getSystemInfo")
    #     self.assertIn("SDKVersion", sys_info.result.result)

    def test_save_order(self):
        # 首页点击【搜索酒店】
        self.page.get_element("button", inner_text="搜索酒店").click()
        time.sleep(3)
        # 酒店页点击【酒店图片】
        self.page.get_element(".img").click()
        time.sleep(3)
        # 选择第一个房型，并点击
        print(self.page.get_elements(".book_btn"))
        self.page.get_elements(".book_btn")[0].click()
        time.sleep(1)
        # # 点击立即预订
        # self.page.get_element('.btn-action').click()
        input_element = self.page.get_elements(".tar.tar.fc-main.fc-main")
        print(input_element)
        input_element[0].input("李福庆")
        input_element[1].input("18516126760")
        self.page.get_element("button", inner_text="去支付").click()
        time.sleep(2)
        result = self.page.get_element(".link").inner_text
        assert "查看订单" == result
        self.page.get_element(".link").click()
        username = self.page.get_element(".color_111A34.fs30.margin_top22.room_info_bottom_line").inner_text
        price = self.page.get_element(".color_111A34.fs26").inner_text
        assert "入住人：李福庆 总价：¥0.00" == f'入住人：{username} 总价：¥{price}'
        print(username,price)

