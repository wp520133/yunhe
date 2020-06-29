import unittest
from page.page_base_info_mange.page_units_manage import PageUnitsManage
from base.get_driver import GetDriver
from tools.read_txt import read_txt
from parameterized import parameterized
import pytest
import allure
import page


class TestDeptManage(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver().get_driver()
        cls.pum = PageUnitsManage(cls.driver)
        cls.pum.system_login()

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    def test_units_manage_click(self):
        self.pum.units_manage_click()

    @parameterized.expand(read_txt("base_info_manage/units_manage.txt"))
    def test_units_manage_insert(self, units_name, sn, remark, desc, success):
        self.pum.units_manage_insert(units_name, sn, remark, desc)
        if success:
            try:
                self.pum.page_units_manage_return_click()
            except:
                self.pum.base_get_image()

    # 测试新增、查询、编辑
    def test_units_manage_edit(self):
        self.pum.units_manage_edit(page.public_value, page.public_order_num, page.public_value, page.public_value)

    # 测试查看
    def test_units_manage_watch(self):
        self.pum.units_manage_watch()

    # 测试重置
    def test_units_manage_reset(self):
        self.pum.units_manage_reset()


if __name__ == '__main__':
    unittest.main()
