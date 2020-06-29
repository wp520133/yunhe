import unittest
from page.page_base_info_mange.page_units_class_manage import PageUnitsClassManage
from base.get_driver import GetDriver
from parameterized import parameterized
from tools.read_txt import read_txt
import pytest
import allure
import page


class TestDeptManage(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver().get_driver()
        cls.pucm = PageUnitsClassManage(cls.driver)
        cls.pucm.system_login()

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    # 测试点击部件类别管理
    def test_units_class_manage_click(self):
        self.pucm.units_class_manage_click()

    # 测试部件类别管理异常数据新增
    @parameterized.expand(read_txt("base_info_manage/units_class.txt"))
    def test_units_class_manage_insert(self, units_name, desc, success):
        self.pucm.units_class_manage_insert(units_name, desc)
        if success:
            try:
                self.pucm.page_units_class_manage_insert_return_click()
            except:
                self.pucm.base_get_image()

    # 测试新增、查询、编辑
    def test_units_class_manage_edit(self):
        self.pucm.units_class_manage_edit(page.public_value, page.public_value)

    # 测试重置
    def test_units_class_manage_reset(self):
        self.pucm.units_class_manage_reset()


if __name__ == '__main__':
    unittest.main()
