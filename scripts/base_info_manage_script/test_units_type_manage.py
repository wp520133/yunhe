import unittest
from page.page_base_info_mange.page_units_type_manage import PageUnitsTypeManage
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
        cls.putm = PageUnitsTypeManage(cls.driver)
        cls.putm.system_login()

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    # 测试部件型号管理点击

    def test_units_type_manage_click(self):
        self.putm.units_type_manage_click()

    # 测试异常数据部件型号新增
    @parameterized.expand(read_txt("base_info_manage/units_type.txt"))
    def test_units_type_manage_insert(self, units_type, brand_name, effective_time, guarantee_num, desc, success):
        self.putm.units_type_manage_insert(units_type, brand_name, effective_time, guarantee_num, desc)
        if success:
            try:
                self.putm.page_units_type_manage_return_button()
            except:
                self.putm.base_get_image()

    # 测试新增、查询、编辑
    def test_units_type_manage_edit(self):
        self.putm.units_type_manage_edit(page.public_value, page.public_value, page.public_order_num,
                                         page.public_order_num, page.public_value)

    # 测试查看
    def test_units_type_manage_watch(self):
        self.putm.units_type_manage_watch()

    # 测试重置
    def test_units_type_manage_reset(self):
        self.putm.units_type_manage_reset()


if __name__ == '__main__':
    unittest.main()
