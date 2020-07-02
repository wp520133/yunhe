import unittest
from page.page_curing_work_manage.page_curing_item_manage import PageCuringItemManage
from base.get_driver import GetDriver
from parameterized import parameterized
from tools.read_txt import read_txt
import page
import allure
import pytest


class TestDeptManage(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver().get_driver()
        cls.pcim = PageCuringItemManage(cls.driver)
        cls.pcim.system_login()

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().quit_driver()

    @allure.step(title="养护项目管理点击")
    def test_curing_item_manage_click(self):
        self.pcim.curing_item_manage_click()

    @parameterized.expand(read_txt("curing_work_manage/curing_item.txt"))
    @allure.step(title="养护项目管理输入异常数据新增")
    def test_curing_item_manage_insert(self, units_name, max_period, main_period, place_desc, remarks, success):
        self.pcim.curing_item_manage_insert(units_name, max_period, main_period, place_desc, remarks)
        if success:
            try:
                self.pcim.page_curing_item_manage_return_click()
            except:
                self.pcim.base_get_image()

    # 测试养护项目管理新增、查看、编辑
    @allure.step(title="养护项目管理新增、查看到编辑")
    def test_curing_item_manage_edit(self):
        self.pcim.curing_item_manage_edit(page.public_value, page.public_order_num, page.public_order_num,
                                          page.public_value, page.public_value)

    # 测试重置
    @allure.step(title="养护项目管理重置")
    def test_curing_item_manage_reset(self):
        self.pcim.curing_item_manage_reset()

    # 测试查看
    @allure.step(title="养护项目管理查看")
    def test_curing_item_manage_watch(self):
        self.pcim.curing_item_manage_watch()


if __name__ == '__main__':
    unittest.main()
