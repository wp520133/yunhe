import unittest
from page.page_base_info_mange.page_repair_class_manage import PageRepairClassManage
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
        cls.prcm = PageRepairClassManage(cls.driver)
        cls.prcm.system_login()

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    @allure.step(title="点击备件类别管理")
    def test_repair_class_manage_click(self):
        self.prcm.repair_class_manage_click()

    @parameterized.expand(read_txt("base_info_Manage/repair_class.txt"))
    @allure.step(title="备件类别管理输入异常数据新增")
    def test_repair_class_manage_insert(self, repair_name, desc, success):
        self.prcm.repair_class_manage_insert(repair_name, desc)
        if success:
            try:
                self.prcm.page_repair_class_manage_return_button()
            except:
                self.prcm.base_get_image()

    # 测试新增、查询、修改
    @allure.step(title="备件类别管理新增、查询到修改")
    def test_repair_class_manage_edit(self):
        self.prcm.repair_class_manage_edit(page.public_value, page.public_value)

    # 测试重置
    @allure.step(title="备件类别管理重置")
    def test_repair_class_manage_reset(self):
        self.prcm.repair_class_manage_reset()


if __name__ == '__main__':
    unittest.main()
