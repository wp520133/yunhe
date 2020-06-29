import unittest
from page.page_base_info_mange.page_system_class_manage import PageSystemClassManage
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
        cls.pscm = PageSystemClassManage(cls.driver)
        cls.pscm.system_login()

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    # 点击系统类别管理
    def test_system_class_manage_click(self):
        self.pscm.system_class_manage_click()

    # 实现新增输入异常数据
    @parameterized.expand(read_txt("base_info_manage/system_class.txt"))
    @allure.step(title="系统类别管理异常数据新增")
    def test_system_class_manage_insert(self, system_class, desc, success):
        self.pscm.system_class_manage_insert(system_class, desc)
        if success:
            try:
                self.pscm.page_system_class_manage_return_button()
            except:
                self.pscm.base_get_image()

    # 同时实现新增、查询、编辑
    @allure.step(title="系统类别管理新增、查询与编辑")
    def test_system_class_manage_edit(self):
        self.pscm.system_class_manage_edit(page.public_value, page.public_value)

    # 实现重置
    @allure.step(title="系统类别管理重置")
    def test_system_class_manage_reset(self):
        self.pscm.system_class_manage_reset()


if __name__ == '__main__':
    unittest.main()
