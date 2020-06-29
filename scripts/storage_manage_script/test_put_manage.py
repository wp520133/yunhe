import unittest
from page.page_storage_manage.page_put_manage import PagePutManage
from base.get_driver import GetDriver
from parameterized import parameterized
from tools.read_txt import read_txt
import page
import pytest
import allure


class TestDeptManage(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver().get_driver()
        cls.ppm = PagePutManage(cls.driver)
        cls.ppm.system_login()

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    # 点击入库管理
    def test_mine_put_bill_click(self):
        self.ppm.mine_put_bill_click()

    # # 我的入库单新增
    # @parameterized.expand(read_txt("storage_manage/mind_put_bill.txt"))
    # def test_mine_put_bill_insert(self, put_part, apply_reason, part_num, price, part_unit, success):
    #     self.ppm.mine_put_bill_insert(put_part, apply_reason, part_num, price, part_unit)
    #     if success:
    #         try:
    #             self.ppm.page_mine_put_bill_insert_return_button()
    #         except:
    #             self.ppm.base_get_image()
    #
    # # 我的入库单查询
    # def test_mine_put_bill_search(self):
    #     self.ppm.mine_put_bill_search(page.public_value, page.public_value, page.public_order_num,
    #                                   page.public_order_num, page.public_value_num2)
    #
    # # 测试入库
    # def test_wait_approval_put_bill_put(self):
    #     self.ppm.wait_approval_put_bill_put(page.public_value2, page.public_value, "10",
    #                                         page.public_order_num, page.public_value_num2)
    #
    # # 入库单管理新增异常数据输入
    # @parameterized.expand(read_txt("storage_manage/put_bill_manage.txt"))
    # def test_put_bill_manage_insert(self, put_part, apply_reason, part_num, price, part_unit, success):
    #     self.ppm.put_bill_manage_insert(put_part, apply_reason, part_num, price, part_unit)
    #     if success:
    #         try:
    #             self.ppm.page_mine_put_bill_insert_return_button()
    #         except:
    #             self.ppm.base_get_image()

    # 测试入库单管理入库
    def test_put_bill_manage_put(self):
        self.ppm.put_bill_manage_put(page.public_value3, page.public_value, "10",
                                     page.public_order_num, page.public_value_num2)


if __name__ == '__main__':
    pytest.main()
