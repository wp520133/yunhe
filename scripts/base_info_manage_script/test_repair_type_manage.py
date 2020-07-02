import unittest
from page.page_base_info_mange.page_repair_type_manage import PageRepairTypeManage
from base.get_driver import GetDriver
from parameterized import parameterized
from tools.read_txt import read_txt
import page
import allure
import pytest


class TestSystemClassManage(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver().get_driver()
        cls.prtm = PageRepairTypeManage(cls.driver)
        cls.prtm.system_login()

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    # 点击
    @allure.step(title="点击备件型号管理")
    def test_repair_type_manage_click(self):
        self.prtm.repair_type_manage_click()

    # 测试新增输入异常数据
    @parameterized.expand(read_txt("base_info_manage/repair_type.txt"))
    @allure.step(title="备件型号管理输入异常数据新增")
    def test_repair_type_manage_insert(self, repair_type, cu, price, price_unit, brand_name, vd, guarantee_num, desc):
        self.prtm.repair_type_manage_insert(repair_type, cu, price, price_unit, brand_name, vd, guarantee_num, desc)

    # 测试新增、查询、编辑
    @allure.step(title="备件型号管理新增、查询到编辑")
    def test_repair_type_manage_edit(self):
        self.prtm.repair_type_manage_edit(page.public_value, page.public_value_num2, page.public_order_num,
                                          page.public_value_num2, page.public_value, page.public_order_num,
                                          page.public_order_num, page.public_value)

    # 测试重置
    @allure.step(title="备件型号管理重置")
    def test_repair_type_manage_reset(self):
        self.prtm.repair_type_manage_reset()

    # 测试查看
    @allure.step(title="备件型号管理查看")
    def test_repair_type_manage_watch(self):
        self.prtm.repair_type_manage_watch()


if __name__ == '__main__':
    unittest.main()
