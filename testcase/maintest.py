import minium

from pages.main import Main


class MainTest(minium.MiniTest):
    def setUp(self):
        self.main = Main(self)

    # def test_order(self):
    #     res = self.main.goto_hotel_list().goto_hotel_detail().goto_hotel_scheduled().save_order()
    #     assert res == 'True'

    def test_order_list(self):
        res = self.main.goto_hotel_list().goto_hotel_detail().goto_hotel_scheduled().goto_order_detail()
        assert res == 'True'

    def tearDown(self):
        pass
